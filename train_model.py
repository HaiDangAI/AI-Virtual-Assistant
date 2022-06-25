import json
from nltk_utils import *
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten
from tensorflow.keras.optimizers import SGD
from tensorflow import keras

with open('content.json','r') as f:
    intents = json.load(f)

all_words = []
tags = []
patterns_tags = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        patterns_tags.append((w, tag))
        
        
ignore_words = ['?', '!', '.', ',']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))

X_train = []
y_train = []

for (pattern_sentence, tag) in patterns_tags:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train, dtype=np.float32)
y_train = np.array(y_train, dtype=np.float32)

model = Sequential([
    Dense(128, input_shape=(len(X_train[0]),), activation='relu'),
    Dense(64, activation='relu'),
    Dense(7, activation='softmax')
])

sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='sparse_categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.summary()
model.fit(np.array(X_train), np.array(y_train), epochs=1000, batch_size=8, verbose=1)
model.save('chatbot_model.h5')