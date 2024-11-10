from flask import Flask, render_template, request, jsonify
import base64
import os
from gpt import diagnose, recommend_products, recommend_routine  # Import the diagnose function from gpt.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    # Retrieve the base64 image data from the request
    data_url = request.form['image']
    # Decode the base64 image and save it temporarily
    image_data = base64.b64decode(data_url.split(",")[1])
    image_path = "captured_image.png"
    
    with open(image_path, "wb") as f:
        f.write(image_data)
    
    # Call the diagnose function from gpt.py
    skin_issue = diagnose(image_path)
    specific_products = recommend_products(skin_issue)
    routines = recommend_routine(specific_products)
    
    # Remove the temporary image if you don’t need to keep it
    os.remove(image_path)
    
    # Return the diagnosis to the frontend
    return jsonify({"status": "success", "diagnosis": skin_issue, "products": specific_products, 'routines': routines})

if __name__ == '__main__':
    app.run(debug=True)
