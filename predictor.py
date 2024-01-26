from keras.models import load_model
from flask import Flask, request, render_template, jsonify
import cv2
import numpy as np
model = load_model("mymodel2.h5")

app = Flask(__name__)
app.static_folder = "static"

@app.route('/',methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        # Get the uploaded image file
        image_file = request.files["image"]

        # Read the image using cv2
        img = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Preprocess the image using cv2 and numpy
        img = cv2.resize(img, (224,224))  # Resize to target size
        img = img / 255.0  # Normalize between 0 and 1
        img = img.astype("float32")  # Convert to float32 for model input
        x = np.expand_dims(img, axis=0)  # Add batch dimension

        # Predict using the model
        prediction = model.predict(x)[0]
        class_index = prediction.argmax()
        # Get the class label based on the index
        # Replace this with your actual class labels
        
        predicted_class = "Yes" if prediction>0.5 else "No"

        is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

        # Return the appropriate response based on AJAX or non-AJAX request
        if is_ajax:
            return jsonify({"prediction": predicted_class})
        else:
            return render_template("index.html", prediction=predicted_class)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000,debug=True)
