#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from werkzeug import secure_filename
import classify_new_digit
from os.path import expanduser

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
home = expanduser("~")
project_dir = "handwritten_digit_classifer"
path_to_uploads = os.path.join(home, project_dir, "uploads")
app.config['UPLOAD_FOLDER'] = path_to_uploads

# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png'])

def allowed_file(filename):
    """For a given file, return whether it's an allowed type or not"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    """Shows the main page of the app"""
    return render_template('index.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    """ function that checks to make sure image is a PNG and uploads it"""
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded'))
    else:
        # Invalid input should return a 404.
        return abort(404)
        
@app.route('/success')
def uploaded():
    """ Shows that file has been uploaded"""
    return render_template('upload_success.html')
    


# 
@app.route('/show_prediction', methods=['GET'])
def show_prediction():
    """Function that handles a GET method and outputs a JSON
    blob of the digit prediction from image_classifier"""
    prediction = classify_new_digit.main()
    pred_dict = {'prediction' : prediction}
    return jsonify(pred_dict)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
    )

