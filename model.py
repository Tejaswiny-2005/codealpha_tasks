import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def create_model(input_shape):
    model = keras.Sequential()
    model.add(layers.LSTM(128, input_shape=input_shape, return_sequences=True))
    model.add(layers.LSTM(128))
    model.add(layers.Dense(88, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model
