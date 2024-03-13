from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
model = load_model('mnist_model.h5')  # Load your trained MNIST model

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        if 'image' in request.files:
            img = request.files['image']
            img_path = 'static/uploaded_image.png'  # Save the uploaded image
            img.save(img_path)

            # Preprocess the image for the model
            img = image.load_img(img_path, target_size=(28, 28), color_mode='grayscale')
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0  # Normalize

            # Make prediction
            prediction_array = model.predict(img_array)
            prediction = np.argmax(prediction_array)

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
