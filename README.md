# Handwritten digit classifier
## To run code from a Unix-based terminal:
1. Be sure you have Python 2.7 and pip installed on your local machine.
2. Open your terminal and cd into your home (~) directory.
3. Clone the repository by typing ```git clone https://github.com/nicklip/handwritten_digit_classifer.git```. Yes, classifier is misspelled as "classifer", I'll fix this at some point. 
4. cd into the repository. Make sure the directory is named handwritten_digit_classifer, otherwise the app will break! Then use requirements.txt to install all necessary Python libraries by typing ```pip install -r requirements.txt```.
6. Build the machine learning model by typing ```python image_classifier.py```. This takes 9 minutes to run on my 8-core Macbook Pro. This will use all of your cores and so your computer will be slow while it is running.
7. Start the application by typing ```export FLASK_APP=ML_app.py``` hit enter and then type ```flask run```.
8. Now you can use the app. Open a browser and put http://127.0.0.1:5000/ in the address bar. The main page of the app should now appear. Here's how to use the app: 
  * Click 'Choose File', choose which PNG file you'd like to upload. Click upload.
  * You should see 'Upload Successful!', now click on 'See Digit Prediction'
  * A JSON blob consisting of {'prediction' :  digit_the_model_predicted} should now be shown. 