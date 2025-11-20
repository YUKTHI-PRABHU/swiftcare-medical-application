import re
import pandas as pd
import streamlit as st

def extract_numbers_from_summary(summary_text):
    """
    Extract numeric metrics from summary text.
    Example:
        'Revenue increased to 1200 while expenses dropped to 800.'
    """
    pattern = r"([A-Za-z ]+?)\s*(\d+\.?\d*)"
    matches = re.findall(pattern, summary_text)

    if not matches:
        return None

    labels = [label.strip() for label, value in matches]
    values = [float(value) for label, value in matches]

    df = pd.DataFrame({"Metric": labels, "Value": values})
    return df


def visualize_summary(summary_text, idx):
    st.markdown(f"## 📈 Line Graph for Summary (Table {idx+1})")

    df = extract_numbers_from_summary(summary_text)

    if df is None:
        st.info("⚠️ No numeric metrics found in the summary to plot.")
        return

    st.write("### Extracted Summary Data:")
    st.dataframe(df)

    # LINE GRAPH
    st.markdown("### 📉 Trend Line Graph")
    st.line_chart(df.set_index("Metric"))
