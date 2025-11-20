# 📄 PDF Table Extraction & Summarization

Welcome to the **PDF Table Extraction & Summarization** project! This application allows you to effortlessly upload PDF documents, extract tables from them, and generate concise summaries using advanced AI models. Built with Streamlit, this tool offers a seamless and interactive user experience.

## 🚀 Features

- **📤 Upload PDFs:** Easily upload your PDF documents through a user-friendly interface.
- **👀 Preview PDFs:** View the content of your PDFs directly within the application.
- **📊 Extract Tables:** Automatically detect and extract tables from your uploaded PDFs.
- **📝 Summarize Tables:** Generate insightful summaries of each extracted table using AI-powered summarization.
- **🧹 Automatic Cleanup:** Ensures temporary files are deleted after processing to maintain security and efficiency.

## 🛠️ Installation

Follow these steps to set up the project locally:

1. **🔀 Clone the Repository:**

   ```bash
   git clone https://github.com/YUKTHI-PRABHU/Analysing_Income_Statement_with_LLM.git
   cd pdf-table-extraction
   ```

2. **🐍 Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   ```

   - **Activate the Virtual Environment:**
     - **Windows:**
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```

3. **📦 Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

Run the Streamlit application using the following command:

streamlit run app.py


Once the application starts, follow these steps:

1. **📂 Upload Your PDF:**
   - Navigate to the sidebar and use the file uploader to select your PDF document.

2. **🔍 Preview the PDF:**
   - After uploading, the application will display a preview of your PDF.

3. **📑 Extract Tables:**
   - The app will automatically extract tables from the PDF. View them in expandable sections.

4. **📝 Summarize Tables:**
   - Generate and view summaries for each extracted table.

## 📁 Project Structure
pdf-table-extraction/
├── app.py                    # Main application file
├── requirements.txt           # Python dependencies
├── utils/                     # Utility scripts for table extraction and summarization
│   ├── table_extraction.py    # Script to handle table extraction from PDF
│   └── summarization.py       # Script to summarize extracted table data
├── README.md                 # Project overview and instructions
└── assets/                    # (Optional) Folder for additional icons or images
    └── icons/                 # Folder for storing icon files

- **`app.py`**: The main Streamlit application file.
- **`requirements.txt`**: Lists all the project dependencies.
- **`utils/`**: Contains utility modules for table extraction and summarization.
- **`assets/`**: (Optional) Directory to store images, icons, or other assets.

## 🧰 Dependencies

The project relies on the following key libraries:

- **[Streamlit](https://streamlit.io/):** For building the interactive web application.
- **[Pandas](https://pandas.pydata.org/):** For data manipulation and analysis.
- **[PyPDF2](https://pypi.org/project/PyPDF2/):** For reading and handling PDF files.
- **[Mistralai](https://pypi.org/project/mistralai/):** For AI-powered summarization (ensure it's correctly installed and configured).

**Full List of Dependencies:**

streamlit
pandas
PyPDF2
mistralai


## 🌐 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository**
2. **Create a New Branch:**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes:**

   ```bash
   git commit -m "Add your message here"
   ```

4. **Push to the Branch:**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📧 Contact

For any inquiries or feedback, please reach out to [YUKTHI PRABHU].

---

<div align="center">
  <img src="https://img.icons8.com/color/48/000000/pdf-2.png" alt="PDF Icon" /> 
  <img src="https://img.icons8.com/color/48/000000/table.png" alt="Table Icon" /> 
<!--   <img src="https://img.icons8.com/color/48/000000/summarize.png" alt="Summarization Icon" /> -->
</div>
