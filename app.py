from flask import Flask, render_template, request, jsonify
import whisper
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize Whisper model for voice transcription
print("Loading Whisper model...")
whisper_model = whisper.load_model("medium")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files["audio"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        try:
            # First, detect the language to confirm it's Malayalam
            audio = whisper.load_audio(filepath)
            audio = whisper.pad_or_trim(audio)
            
            # Transcribe with enhanced Malayalam settings
            result = whisper_model.transcribe(
                filepath,
                language="ml",  # ISO code for Malayalam
                task="transcribe",
                fp16=False,  # Disable FP16 for better accuracy
                initial_prompt="ഇത് മലയാളം ഓഡിയോ ആണ്. മലയാളത്തിൽ സംസാരിക്കുന്നു.",  # Enhanced Malayalam context
                temperature=0.0,  # Reduce randomness in output
                best_of=3,  # Compare multiple transcription attempts
                condition_on_previous_text=True  # Consider context
            )
            
            transcript = result["text"].strip()

            # Clean up
            os.remove(filepath)

            return jsonify({"transcript": transcript})
        except Exception as e:
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    try:
        print("Server starting... You can access the application at:")
        print("http://localhost:8080")
        print("http://127.0.0.1:8080")
        app.run(host='0.0.0.0', port=8080, debug=True)
    except Exception as e:
        print(f"Error starting server: {e}")
        print("If port 8080 is in use, try modifying the port number in app.py") 