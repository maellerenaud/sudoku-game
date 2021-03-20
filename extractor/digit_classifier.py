import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras import backend as K
import numpy as np

model = keras.models.load_model('./extractor/digit_classifier.h5')

def toDigit(rect):
    if np.mean(rect) < 6:
        return 0
    
    predictions = model.predict(rect.reshape(1, 28, 28, 1))
    return np.argmax(predictions)