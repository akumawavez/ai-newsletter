from datasets import load_dataset
import pandas as pd
import sqlite3
import json
from pathlib import Path


DATASET_NAME = "zenml/llmops-database"
OUTPUT_DIR = Path("data")

DB_PATH = OUTPUT_DIR / "llmops_database.db"
PARQUET_PATH = OUTPUT_DIR / "llmops_database.parquet"
JSONL_PATH = OUTPUT_DIR / "llmops_documents.jsonl"


def normalize_tag_field(value):
    if value is None:
        return ""

    if isinstance(value, list):
        return ", ".join(str(v).strip() for v in value if v)

    return str(value).strip()


def build_rag_text(row):
    """
    This text is what your LLM/RAG system will retrieve.
    Keep it rich enough for semantic search.
    """

    parts = [
        f"Title: {row.get('title', '')}",
        f"Company: {row.get('company', '')}",
        f"Industry: {row.get('industry', '')}",
        f"Year: {row.get('year', '')}",
        f"Application Tags: {row.get('application_tags', '')}",
        f"Tools Tags: {row.get('tools_tags', '')}",
        f"Techniques Tags: {row.get('techniques_tags', '')}",
        f"Extra Tags: {row.get('extra_tags', '')}",
        "",
        f"Short Summary: {row.get('short_summary', '')}",
        "",
        f"Full Summary: {row.get('full_summary', '')}",
    ]

    return "\n".join(str(p) for p in parts if p is not None).strip()


def ingest():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Loading Hugging Face dataset: {DATASET_NAME}")

    dataset = load_dataset(DATASET_NAME)

    split_name = list(dataset.keys())[0]
    df = dataset[split_name].to_pandas()

    print(f"Loaded records: {len(df)}")
    print(f"Columns found: {list(df.columns)}")

    expected_columns = [
        "created_at",
        "title",
        "industry",
        "year",
        "source_url",
        "company",
        "application_tags",
        "tools_tags",
        "extra_tags",
        "techniques_tags",
        "short_summary",
        "full_summary",
    ]

    available_columns = [col for col in expected_columns if col in df.columns]
    df = df[available_columns].copy()

    if "created_at" in df.columns:
        df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

    if "year" in df.columns:
        df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")

    tag_columns = [
        "application_tags",
        "tools_tags",
        "extra_tags",
        "techniques_tags",
    ]

    for col in tag_columns:
        if col in df.columns:
            df[col] = df[col].apply(normalize_tag_field)

    if "title" in df.columns:
        df = df[df["title"].notna()].copy()
        df["title"] = df["title"].astype(str).str.strip()

    df["rag_text"] = df.apply(build_rag_text, axis=1)

    # Save queryable version
    df.to_parquet(PARQUET_PATH, index=False)

    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql("llmops_case_studies", conn,
                  if_exists="replace", index=False)

    # Save RAG-friendly JSONL
    with open(JSONL_PATH, "w", encoding="utf-8") as f:
        for idx, row in df.iterrows():
            doc = {
                "id": f"llmops-{idx}",
                "text": row["rag_text"],
                "metadata": {
                    "title": row.get("title", ""),
                    "company": row.get("company", ""),
                    "industry": row.get("industry", ""),
                    "year": str(row.get("year", "")),
                    "source_url": row.get("source_url", ""),
                    "tools_tags": row.get("tools_tags", ""),
                    "techniques_tags": row.get("techniques_tags", ""),
                    "application_tags": row.get("application_tags", ""),
                },
            }

            f.write(json.dumps(doc, ensure_ascii=False) + "\n")

    print("\nIngestion complete.")
    print(f"SQLite DB: {DB_PATH}")
    print(f"Parquet:   {PARQUET_PATH}")
    print(f"JSONL:     {JSONL_PATH}")


if __name__ == "__main__":
    ingest()
