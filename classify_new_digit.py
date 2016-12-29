#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" Assuming that the file to being upload is binary and has metadata
    identical to the MNIST training images data file. Also assuming that
    the file is not zipped, since it's only one image. """

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
    # Load pickled model
    path_to_pickled_model = os.path.join(home, project_dir, "model.pkl")
    clf = pickle.load(open(path_to_pickled_model, 'rb'))
    # load and read image png file, convert to numpy array
    numpy_image = misc.imread(os.path.join(home, project_dir, "uploads", image))
    resized_image = numpy_image.reshape(-1,1).astype(np.float32)
    # feature scaling
    min_max_scaler = preprocessing.MinMaxScaler()
    X = min_max_scaler.fit_transform(resized_image)
    X = X.reshape(1, 784)
    # return the prediction
    return int(clf.predict(X)[0])

def main():
    home = expanduser("~")
    project_dir = "Planet_ML_project"
    path_to_uploads = os.path.join(home, project_dir, "uploads")
    os.chdir(path_to_uploads)
    list_of_pngs = glob.glob('*.png')
    newest_image = max(list_of_pngs, key=os.path.getctime)
    return classify(newest_image, home, project_dir)
    
if __name__ == "__main__":
    main()