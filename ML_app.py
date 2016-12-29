#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
#, send_from_directory
from werkzeug import secure_filename
import classify_new_digit
from os.path import expanduser

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
home = expanduser("~")
project_dir = "Planet_ML_project"
path_to_uploads = os.path.join(home, project_dir, "uploads")
app.config['UPLOAD_FOLDER'] = path_to_uploads

# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
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
    # Add a conditional to check if the uploaded file exists
    # create a new html page (template) to show this and also to
    # show a button that says "See image prediction"
    # upload_success.html
    return render_template('upload_success.html')
    


# create a function that handles a GET method? and outputs a JSON
# (use jsonify function) of the digit prediction from image_classifier
@app.route('/show_prediction', methods=['GET'])
def show_prediction():
    prediction = classify_new_digit.main()
    pred_dict = {'prediction' : prediction}
    return jsonify(pred_dict)
    
    
# REMEMBER TO CREATE A REQUIREMENTS.TXT FILE SO HOLD ALL NAMES OF ALL THE PYTHON
# LIBRARIES USED, WHICH IS USED BY USER TO INSTALL THE NECESSARY LIBRARIES!
    
# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
#@app.route('/uploads/<filename>')
#def uploaded_file(filename):
 #   return send_from_directory(app.config['UPLOAD_FOLDER'],
    #                           filename)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
    )

