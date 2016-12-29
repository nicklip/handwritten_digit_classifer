#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np 
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
import pickle
import glob
import os
from os.path import expanduser
from scipy import misc

def classify(image, home, project_dir):
    """Returns the prediction of the label for the handwritten digit"""
    # Load pickled model
    path_to_pickled_model = os.path.join(home, project_dir, "model.pkl")
    clf = pickle.load(open(path_to_pickled_model, 'rb'))
    # load and read image png file, convert to numpy array
    numpy_image = misc.imread(os.path.join(home, project_dir, "uploads", image))
    # resize from 28x28 to 1x784 and convert from ints to floats
    resized_image = numpy_image.reshape(-1,1).astype(np.float32)
    # perform feature scaling
    min_max_scaler = preprocessing.MinMaxScaler()
    X = min_max_scaler.fit_transform(resized_image)
    X = X.reshape(1, 784)
    # return the prediction as an int
    return int(clf.predict(X)[0])

def main():
    """Main function to get the most recently uploaded PNG file and pass it to
    the classify function, returns the classifiers prediction"""
    home = expanduser("~")
    project_dir = "handwritten_digit_classifer"
    path_to_uploads = os.path.join(home, project_dir, "uploads")
    os.chdir(path_to_uploads)
    # get all PNG filenames
    list_of_pngs = glob.glob('*.png')
    # get name of most recently uploaded PNG file
    newest_image = max(list_of_pngs, key=os.path.getctime)
    return classify(newest_image, home, project_dir)
    
if __name__ == "__main__":
    main()