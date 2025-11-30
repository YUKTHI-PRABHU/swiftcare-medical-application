from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, jsonify
import os
import sqlite3
import re

app = Flask(__name__)
app.secret_key = "abc123"

UPLOAD_FOLDER = "uploaded_reports"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
DB_FILE = "database.db"

# ---------------- Database Setup ----------------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            filename TEXT,
            status TEXT DEFAULT 'pending',
            doctor_comment TEXT DEFAULT ''
        )
    """)
    conn.commit()
    conn.close()

init_db()

def add_upload(patient_name, filename):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO uploads (patient_name, filename) VALUES (?, ?)", (patient_name, filename))
    conn.commit()
    conn.close()

def get_patient_reports(patient_name):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM uploads WHERE patient_name=?", (patient_name,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_pending_uploads():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM uploads WHERE status='pending'")
    rows = c.fetchall()
    conn.close()
    return rows

def get_reviewed_uploads():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM uploads WHERE status='viewed'")
    rows = c.fetchall()
    conn.close()
    return rows

def update_doctor_comment(upload_id, comment):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE uploads SET doctor_comment=?, status='viewed' WHERE id=?", (comment, upload_id))
    conn.commit()
    conn.close()

# ---------------- Dummy AI Analysis ----------------
def analyze_document(file_path):
    return (
        "🩺 AI Analysis Complete:\n"
        "- Vital signs normal\n"
        "- Mild symptoms detected\n"
        "- First Aid Suggestion: Rest & hydration\n"
        "- Consult doctor if symptoms persist"
    )

# ---------------- Routes ----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/patient", methods=["GET", "POST"])
def patient():
    if request.method == "POST":
        patient_name = request.form.get("name") or "Anonymous"
        session["patient_name"] = patient_name

        file = request.files["file"]
        filename = file.filename.replace(" ", "_")
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        add_upload(patient_name, filename)
        analysis = analyze_document(path)
        reports = get_patient_reports(patient_name)

        return render_template("patient_dashboard.html",
                               name=patient_name,
                               analysis=analysis,
                               reports=reports,
                               filename=filename)

    return render_template("patient_form.html")

@app.route("/doctor")
def doctor_dashboard():
    pending = get_pending_uploads()
    reviewed = get_reviewed_uploads()
    return render_template("doctor_dashboard.html", pending=pending, viewed=reviewed)

@app.route("/doctor/comment/<int:upload_id>", methods=["POST"])
def doctor_comment(upload_id):
    comment = request.form.get("comment")
    update_doctor_comment(upload_id, comment)
    return redirect(url_for("doctor_dashboard"))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# ---------------- Chatbot Logic ----------------
@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_msg = request.json.get("message", "").lower()

    if "report" in user_msg:
        reply = "You can view your uploaded reports above in the dashboard. 😊"
    elif re.search(r"fever|temperature", user_msg):
        reply = "It may be mild fever 🤒. Stay hydrated and rest well."
    elif re.search(r"cough|cold", user_msg):
        reply = "Warm liquids & steam inhalation help for cold/cough 😷."
    elif re.search(r"headache", user_msg):
        reply = "Try resting, reducing screen time, and stay hydrated 💧."
    elif re.search(r"stomach|gas|acid", user_msg):
        reply = "Eat light food and drink ORS. Avoid spicy and oily items 🍽️."
    else:
        reply = "Ask me about symptoms like fever, headache, cough or reports!"

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
