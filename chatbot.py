from tensorflow import keras
from nltk_utils import *
import json
import random


model = keras.models.load_model('chatbot_model.h5')

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

def preprocess_sentences(sentence):
    token_sentence = tokenize(sentence)
    bag = bag_of_words(token_sentence, all_words)
    return bag

def get_user_typed():
    return input('Enter: ')

def predict_tag(sentence):
    X_predict = np.array([preprocess_sentences(sentence)], dtype=np.float32)
    idx = np.argmax(model.predict(X_predict[0:1]))
    return tags[idx]

def response(tag):
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

def chatbot(user_input):
    pred_tag = predict_tag(user_input)
    pred_res = response(pred_tag)
    return pred_res

if __name__ == '__main__':
    for i in range(5):
        typed = get_user_typed()
        pred_tag = predict_tag(typed)
        pred_res = response(pred_tag)
        print('Responce: ', pred_res)