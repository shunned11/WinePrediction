import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential,model_from_json
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
import Utilities as ut

n=28

train_data=pd.read_csv("Data/train.csv")
test_data=pd.read_csv("Data/test.csv")

X_train=train_data["review_description"].values
Y_train=train_data["variety"].values

X_test=test_data["review_description"].values

tk=Tokenizer(lower=True)
tk.fit_on_texts(X_train)
X_train_seq = tk.texts_to_sequences(X_train)
X_train_pad = pad_sequences(X_train_seq, maxlen=100,padding='post')

X_test_seq = tk.texts_to_sequences(X_test)
X_test_pad = pad_sequences(X_test_seq, maxlen=100,padding='post')

np.save("X_test",X_test_pad)

le=LabelEncoder()
oh = OneHotEncoder(sparse=False)
Y_train=le.fit_transform(Y_train)
Y_train= Y_train.reshape(len(Y_train), 1)
Y_train=oh.fit_transform(Y_train)


def main():
    vocabulary_size = len(tk.word_counts.keys())+1
    emb_matrix=ut.embedding(vocabulary_size,tk)
    model=Sequential()
    model.add(Embedding(vocabulary_size,50,trainable=False))
    model.add(LSTM(128,return_sequences=True))
    model.add(Dropout(0.4))
    model.add(LSTM(128))
    model.add(Dropout(0.4))
    model.add(Dense(n,activation='softmax'))

    model.layers[0].set_weights([emb_matrix])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train_pad,Y_train,batch_size=32,epochs=20,validation_split=0.2)

    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model.h5")

if __name__ == "__main__":
    main()