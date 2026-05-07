import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path


DB_PATH = Path("data/llmops_database.db")


st.set_page_config(
    page_title="LLMOps Case Study Explorer",
    layout="wide",
)


def table_exists(conn, table_name):
    query = """
    SELECT name
    FROM sqlite_master
    WHERE type='table' AND name=?
    """
    return conn.execute(query, (table_name,)).fetchone() is not None


@st.cache_data
def load_data(view_mode):
    if not DB_PATH.exists():
        return None

    table_name = (
        "processed_newsletter_items"
        if view_mode == "Processed newsletter items"
        else "llmops_case_studies"
    )

    with sqlite3.connect(DB_PATH) as conn:
        if not table_exists(conn, table_name):
            return None

        df = pd.read_sql_query(
            f"SELECT * FROM {table_name}",
            conn,
        )

    return df


st.title("LLMOps Case Study Explorer")

if not DB_PATH.exists():
    st.error("Database not found. Run `python ingest_dataset.py` first.")
    st.stop()


st.sidebar.header("View Mode")

view_mode = st.sidebar.radio(
    "Choose view",
    [
        "Explore all case studies",
        "Processed newsletter items",
    ],
)


df = load_data(view_mode)

if df is None or df.empty:
    if view_mode == "Processed newsletter items":
        st.error(
            "Processed newsletter table not found. Run `python process_analyze.py` first."
        )
    else:
        st.error("No data found. Run `python ingest_dataset.py` first.")
    st.stop()


st.sidebar.header("Filters")

search_text = st.sidebar.text_input(
    "Search title, company, summary, tags"
)

filtered = df.copy()


if "section" in filtered.columns:
    sections = sorted(filtered["section"].dropna().unique())
    selected_sections = st.sidebar.multiselect("Newsletter section", sections)

    if selected_sections:
        filtered = filtered[filtered["section"].isin(selected_sections)]


if "industry" in filtered.columns:
    industries = sorted(filtered["industry"].dropna().unique())
    selected_industries = st.sidebar.multiselect("Industry", industries)

    if selected_industries:
        filtered = filtered[filtered["industry"].isin(selected_industries)]


if "company" in filtered.columns:
    companies = sorted(filtered["company"].dropna().unique())
    selected_companies = st.sidebar.multiselect("Company", companies)

    if selected_companies:
        filtered = filtered[filtered["company"].isin(selected_companies)]


if search_text:
    search_text_lower = search_text.lower()

    searchable_cols = [
        "title",
        "company",
        "industry",
        "section",
        "short_summary",
        "full_summary",
        "newsletter_summary",
        "tools_tags",
        "techniques_tags",
        "application_tags",
        "extra_tags",
    ]

    existing_cols = [
        col for col in searchable_cols if col in filtered.columns
    ]

    mask = pd.Series(False, index=filtered.index)

    for col in existing_cols:
        mask = mask | (
            filtered[col]
            .fillna("")
            .astype(str)
            .str.lower()
            .str.contains(search_text_lower, regex=False)
        )

    filtered = filtered[mask]


sort_options = []

if "trending_score" in filtered.columns:
    sort_options.append("trending_score")

if "year" in filtered.columns:
    sort_options.append("year")

if "created_at" in filtered.columns:
    sort_options.append("created_at")

if sort_options:
    sort_by = st.sidebar.selectbox("Sort by", sort_options)
    filtered = filtered.sort_values(by=sort_by, ascending=False)


st.subheader(f"Results: {len(filtered)} items")


if view_mode == "Processed newsletter items":
    for _, row in filtered.iterrows():
        title = row.get("title", "Untitled")
        company = row.get("company", "")
        section = row.get("section", "Uncategorized")

        with st.expander(f"{title} — {company}"):
            st.write(f"**Section:** {section}")
            st.write(f"**Company:** {row.get('company', '')}")
            st.write(f"**Industry:** {row.get('industry', '')}")
            st.write(f"**Year:** {row.get('year', '')}")

            if "trending_score" in row:
                st.write(
                    f"**Relevance score:** {row.get('trending_score', '')}")

            if row.get("source_url"):
                st.write(f"**Source:** {row.get('source_url')}")

            st.write("### Newsletter summary")
            st.write(row.get("newsletter_summary", ""))

            st.write("### Tags")
            st.write(f"**Tools:** {row.get('tools_tags', '')}")
            st.write(f"**Techniques:** {row.get('techniques_tags', '')}")
            st.write(f"**Applications:** {row.get('application_tags', '')}")

else:
    for _, row in filtered.iterrows():
        title = row.get("title", "Untitled")
        company = row.get("company", "")

        with st.expander(f"{title} — {company}"):
            st.write(f"**Industry:** {row.get('industry', '')}")
            st.write(f"**Year:** {row.get('year', '')}")
            st.write(f"**Company:** {row.get('company', '')}")

            if row.get("source_url"):
                st.write(f"**Source:** {row.get('source_url')}")

            st.write("### Summary")
            st.write(row.get("short_summary", ""))

            st.write("### Tags")
            st.write(f"**Tools:** {row.get('tools_tags', '')}")
            st.write(f"**Techniques:** {row.get('techniques_tags', '')}")
            st.write(f"**Applications:** {row.get('application_tags', '')}")

            with st.expander("Full summary"):
                st.write(row.get("full_summary", ""))
