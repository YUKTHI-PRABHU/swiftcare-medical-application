import streamlit as st
from utils.table_extraction import extract_tables_from_pdf
from utils.summarization import initialize_llm_pipeline, summarize_table
from utils.chatbot import chatbot_response
from utils.summary_visualization import visualize_summary

import pandas as pd
import os
import uuid
import base64


def main():
    st.set_page_config(
        page_title="📄 PDF Table Extraction & Summarization",
        layout="wide",
        page_icon="📈",
    )

    st.title("📄 PDF Table Extraction and Summarization")

    # Sidebar Upload
    with st.sidebar:
        st.header("Upload PDF")
        uploaded_file = st.file_uploader("Choose a PDF", type="pdf")
        temp_filename = None
        
        if uploaded_file:
            temp_filename = f"temp_{uuid.uuid4().hex}.pdf"
            with open(temp_filename, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("PDF Uploaded Successfully!")

    if uploaded_file:
        try:
            # -------- PDF PREVIEW --------
            st.subheader("📖 PDF Preview")
            try:
                with open(temp_filename, "rb") as f:
                    pdf_bytes = f.read()
                    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
                pdf_display = f"""
                    <iframe src="data:application/pdf;base64,{base64_pdf}" 
                            width="100%" height="600"></iframe>
                """
                st.markdown(pdf_display, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"⚠️ Error previewing PDF: {e}")

            # -------- Extract Tables --------
            st.subheader("📊 Extracted Tables")
            try:
                dfs, _ = extract_tables_from_pdf(temp_filename)
            except Exception as e:
                st.error(f"⚠️ Error extracting tables: {e}")
                return

            if dfs:
                for idx, df in enumerate(dfs):
                    st.write(f"### Table {idx + 1}")
                    st.dataframe(df)
            else:
                st.warning("⚠️ No tables found.")
                return

            # -------- Summarization --------
            st.subheader("📝 Table Summaries")

            client = initialize_llm_pipeline()
            st.session_state["summaries_list"] = []

            for idx, df in enumerate(dfs):
                table_text = df.to_string(index=False)

                try:
                    summary = summarize_table(client, table_text)
                except Exception as e:
                    st.error(f"❌ Error summarizing Table {idx + 1}: {e}")
                    continue

                st.write(f"### Summary for Table {idx + 1}")
                st.success(summary)

                # Save summary for chatbot
                st.session_state["summaries_list"].append(summary)

                # ---- VISUALIZE SUMMARY (LINE GRAPH) ----
                visualize_summary(summary, idx)

            # -------- CHATBOT SECTION --------
            st.subheader("💬 Chatbot: Ask Questions Based on Summaries")

            all_summaries_text = "\n\n".join(st.session_state["summaries_list"])

            user_question = st.text_input("Ask something about the summarized data:")

            if user_question:
                try:
                    reply = chatbot_response(client, all_summaries_text, user_question)
                    st.write("### 🤖 Chatbot Response:")
                    st.info(reply)
                except Exception as e:
                    st.error(f"❌ Chatbot Error: {e}")

        finally:
            # Delete temporary PDF file
            if temp_filename and os.path.exists(temp_filename):
                try:
                    os.remove(temp_filename)
                except:
                    pass


if __name__ == "__main__":
    main()
