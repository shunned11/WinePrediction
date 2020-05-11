import tensorflow as tf
import pandas as pd
import numpy as np
from Model import le, X_train_pad
from tensorflow.keras.models import model_from_json
import Visualization as vis

json_file = open('Model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("Model/model.h5")

print(loaded_model.summary())
X_test=np.load("X_test.npy")

Y_test=loaded_model.predict_classes(X_test)
Y_test=le.inverse_transform(Y_test)

Y_train_pred=loaded_model.predict_classes(X_train_pad)
Y_train_real=pd.read_csv("Data/train.csv")["variety"].values
Y_train_real=le.fit_transform(Y_train_real)


vis.plot_cm(Y_train_real,Y_train_pred)
# df=pd.read_csv("test.csv")
# df["variety"]=Y_test
# df.to_csv("Updated Test.csv",index=False)