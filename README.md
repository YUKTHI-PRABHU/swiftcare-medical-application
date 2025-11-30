# Patient Dashboard with AI Chatbot

A **web application** for patients to upload medical reports, view AI-powered analysis, track doctor remarks, and interact with a **health assistant chatbot** for basic medical guidance.

---

## 🧰 Features

- **Patient Uploads:** Patients can upload PDF or image-based medical reports.  
- **AI Analysis:** Dummy AI analysis provides a brief summary of report insights.  
- **Doctor Dashboard:** Doctors can view pending reports, review them, and add comments.  
- **Chatbot:** Interactive chatbot below AI Analysis for answering basic health queries.  
- **Reports Table:** Displays uploaded reports, status, and doctor remarks.  

---

## 💻 Tech Stack

- **Frontend:** HTML, CSS, Bootstrap 5  
- **Backend:** Python, Flask  
- **Database:** SQLite (stores uploads, status, and doctor comments)  
- **Chatbot:** Rule-based Python Flask API (`/chatbot` route)  

---

## 🏗️ Project Structure

project/
│
├─ uploaded_reports/ # Folder for storing uploaded files
├─ templates/
│ ├─ patient_dashboard.html
│ ├─ patient_form.html
│ ├─ doctor_dashboard.html
│ └─ index.html
├─ app.py # Flask backend
├─ database.db # SQLite database (auto-generated)
└─ README.md


---

## ⚡ Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/patient-dashboard-chatbot.git
cd patient-dashboard-chatbot


Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install Flask


Run the Flask application:

python app.py


Open in browser:

http://127.0.0.1:5000/

🚀 Usage

Patient Portal:

Fill in your name and upload a medical report.

View AI analysis and interact with the chatbot below the analysis.

Doctor Portal:

Visit /doctor to view pending reports.

Add comments to reports which will update the patient dashboard.

Chatbot:

Ask questions about common health issues (fever, cough, headache, etc.).

Receives responses from a Flask-based AI assistant.