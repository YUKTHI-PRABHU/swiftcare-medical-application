import os
from flask import Blueprint, render_template, request
from ai_suggester import analyze_document

patient_bp = Blueprint("patient_bp", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@patient_bp.route("/patient")
def patient_page():
    return render_template("patient_upload.html")


@patient_bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file selected!"

    file = request.files["file"]

    if file.filename == "":
        return "Invalid file name!"

    # Save file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # AI Suggestion
    suggestion = analyze_document(file_path)

    return f"""
    <h3>File uploaded successfully ✔</h3>
    <p><b>File:</b> {file.filename}</p>
    <p><b>AI Suggestion:</b> {suggestion}</p>
    <a href="/">Back to Dashboard</a>
    """
