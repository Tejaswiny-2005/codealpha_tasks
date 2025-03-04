import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class MusicGenerator:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = keras.Sequential()
        model.add(layers.LSTM(128, input_shape=(None, 88), return_sequences=True))
        model.add(layers.Dense(88, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam')
        return model

    def train(self, training_data, epochs=50):
        self.model.fit(training_data, epochs=epochs)

    def generate(self, seed, num_notes=100):
        generated = []
        for _ in range(num_notes):
            prediction_input = np.reshape(seed, (1, len(seed), 88))
            prediction = self.model.predict(prediction_input, verbose=0)
            generated.append(np.argmax(prediction))
            seed = np.append(seed, prediction)
        return generated
