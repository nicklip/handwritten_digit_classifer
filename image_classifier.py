#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import download_decompress_save_load
import numpy as np 
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import pickle
import os
from os.path import expanduser

def train_model(path_to_project):
    """Trains and tests the Neural Network, prints its accuracy on the test set"""
    # download, save, and load the data
    try:
        train_feats, train_labels, test_feats, test_labels = download_decompress_save_load.main(path_to_project)
    except Exception as e: 
        print e
    
    # Using a "shallow" NN (MLP) as it's known for being good at image classification and modeling 
    # complex relationships. It also is able to be trained in a reasonable amount of time
    # on my local machine, unlike deep NNs.    
        
    # perform feature scaling for the feature datasets
    # Using minmax version since all values are between 0 and 256
    # This will give us all values between 0 and 1
    # This scaling is critical for the NN to be as accurate as possible
    min_max_scaler = preprocessing.MinMaxScaler()
    X = min_max_scaler.fit_transform(train_feats)
    X_test = min_max_scaler.fit_transform(test_feats)
    y = train_labels
    y_test = test_labels

    ######## Doing crossvalidation to choose good hyperparameter value for alpha to use for model #######
    alpha_params = 10.0 ** -np.arange(1, 7) # Values suggested by Scikit-learn
    alpha_params = alpha_params.tolist()
    parameters = {
        'alpha': alpha_params
    }
    # trying all alpha parameter values from dictionary, This uses parallel processing, will use how many cores you have
    clf = GridSearchCV(MLPClassifier(solver='lbfgs', random_state=1), parameters, n_jobs=-1)
    # fitting the model to do cross-validation
    clf.fit(X, y) # TAKES 9 MINUTES TO TRAIN ON MY 8-CORE MACBOOK PRO
    # predicting the test set
    y_true, y_pred = y_test, clf.predict(X_test)
    # print accuracy
    print "The accuracy of the model on the test set is " + accuracy_score(y_true, y_pred)
    
    #pickle the model so it can be used by the app
    path_to_pickle = os.path.join(path_to_project, "model.pkl")
    pickle.dump(clf, open( path_to_pickle, "wb" ) )
 
def main():
     """Main function to call the train_model function """
     home = expanduser("~")
     project_dir = "handwritten_digit_classifer-master/"
     path_to_project = os.path.join(home, project_dir)
     train_model(path_to_project)

if __name__ == "__main__":
    main()
    







