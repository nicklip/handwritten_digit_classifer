# Handwritten digit classifier
## To run code:
1. Be sure you have Python 2.7 installed on your local machine
2. Open your terminal and cd into your home (~) directory
3. Clone the repository by typing ```git clone https://github.com/nicklip/handwritten_digit_classifer.git```
4. Use requirements.txt to install necessary Python libraries by typing ```pip install -r requirements.txt```
5. Build the machine learning model by typing ```python image_classifier.py``` This takes 9 minutes to run on my 8-core Macbook Pro. This will use all of your cores and so your computer will be slow while it is running.
6. Start the application by typing ```export FLASK_APP=ML_app.py``` then ```flask run```
7. Now you can use the app. Open a browser and put http://127.0.0.1:5000/ in the address bar. The app has now started. Here's how to use the app: 
  * Click 'Choose File', choose which PNG file you'd like to upload. Click upload.
  * You should see 'Upload Successful!', now click on 'See Digit Prediction'
  * A JSON blurb consisting of {'prediction' :  digit_the_model_predicted} should now be shown. 