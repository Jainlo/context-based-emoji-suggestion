import pickle
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import LabelEncoder

#%%
# load pickled model
f = open('RF_model.pickle', 'rb')
RFmodel = pickle.load(f)
f.close()
#%%
# initalize for embedding input
sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')
#%%
# read dataset to use when fitting the target encoder
emotion_emoji_merged = pd.read_csv('../../../Desktop/capstone-data/emoji_emotion_merged.csv')
y = emotion_emoji_merged['Emoji']
# initialize target decoder
lb = LabelEncoder()
y = lb.fit_transform(y)
# use a decoder to get original data
dicoder = dict(zip(lb.classes_, lb.transform(lb.classes_)))
#%%
# function used to get emoji
def RF_model(text_input):
    embedded_input = sbert_model.encode([text_input])[0] #return numpy array of vectors
    embedded_input = np.expand_dims(embedded_input, 0) # reshape from (768,) to (1,768)
    RF_y_pred = RFmodel.predict(embedded_input)# error
    #output = np.argmax(RF_y_pred) # returns a single number which should map to an emoji
    for i in RF_y_pred:
        a = list(dicoder.keys())[list(dicoder.values()).index(i)]
    return a