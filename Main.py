import tensorflow as tf
import pandas as pd
import numpy as np
from Model import le
from tensorflow.keras.models import model_from_json

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")

X_test=np.load("X_test.npy")

Y_test=loaded_model.predict_classes(X_test)
Y_test=le.inverse_transform(Y_test)
df=pd.read_csv("test.csv")
df["variety"]=Y_test
df.to_csv("Updated Test.csv",index=False)