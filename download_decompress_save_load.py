#!/usr/bin/env python2
# -*- coding: utf-8 -*-"

import urllib2
import StringIO
import gzip
import os
import struct
import numpy as np
from os.path import expanduser

def download_uncompress_save(path, baseURL, filename): 
    """ downloads files, uncompresses, and saves them """
    # download and decompress
    outFilePath = path + filename[:-3]
    response = urllib2.urlopen(baseURL + filename)
    compressedFile = StringIO.StringIO(response.read())
    decompressedFile = gzip.GzipFile(fileobj=compressedFile)
    # read the file and write it in the project directory 
    with open(outFilePath, 'w') as outfile:
        outfile.write(decompressedFile.read())
 
def load_mnist(path, which='train'):
    """ loads training or testing data """
    # load train or test depending on the parameters
    if which == 'train':
        labels_path = os.path.join(path, 'train-labels-idx1-ubyte')
        images_path = os.path.join(path, 'train-images-idx3-ubyte')
    elif which == 'test':
        labels_path = os.path.join(path, 't10k-labels-idx1-ubyte')
        images_path = os.path.join(path, 't10k-images-idx3-ubyte')
    else:
        raise AttributeError('`which` must be "train" or "test"')
    # read labels data
    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II', lbpath.read(8))
        labels = np.fromfile(lbpath, dtype=np.uint8)
    # read image data
    with open(images_path, 'rb') as imgpath:
        magic, n, rows, cols = struct.unpack('>IIII', imgpath.read(16))
        images = np.fromfile(imgpath, dtype=np.uint8).reshape(len(labels), 784)
    # return the images and labels which are now numpy arrays
    return images, labels
    

def main(path_to_project):
    """ call both functions with necessary arguments """
    # download, uncompress, and save files
    download_uncompress_save(path_to_project, 'http://yann.lecun.com/exdb/mnist/', 'train-images-idx3-ubyte.gz')
    download_uncompress_save(path_to_project, 'http://yann.lecun.com/exdb/mnist/', 'train-labels-idx1-ubyte.gz')
    download_uncompress_save(path_to_project, 'http://yann.lecun.com/exdb/mnist/', 't10k-images-idx3-ubyte.gz')
    download_uncompress_save(path_to_project, 'http://yann.lecun.com/exdb/mnist/', 't10k-labels-idx1-ubyte.gz')
    # read the saved files and convert to numpy arrays  
    train_feats, train_labels = load_mnist(path_to_project)
    test_feats, test_labels = load_mnist(path_to_project, which='test')
    # return test and train datasets
    return (train_feats, train_labels, test_feats, test_labels)

if __name__ == "__main__":
    main()
    