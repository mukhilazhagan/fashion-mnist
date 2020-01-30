# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

def check_version():
    print(tf.__version__)

def load_db():
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    return (train_images, train_labels),( test_images, test_labels) 

def test_load(index, dataset):
    
    if dataset.size == 0:
        print("Dataset load error")
    elif dataset.ndim > 1:
        plt.imshow(dataset[index,:,:])
    else:
        print("label :", dataset[index])
        

(train_images, train_labels), (test_images, test_labels) = load_db()

test_load(1, test_images)