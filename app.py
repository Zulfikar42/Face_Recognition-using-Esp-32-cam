from flask import Flask, render_template
from fetch_from_dropbox import fetch_image_from_dropbox
from deepface_model import recognize_face

app = Flask(__name__)

@app.route("/")
def home():
    # Fetch the image from Dropbox
    image_path = fetch_image_from_dropbox()
    
    # Run the face recognition model
    result = recognize_face(image_path)
    
    # Return the result in the HTML template
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

