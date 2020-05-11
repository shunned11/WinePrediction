from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from collections import defaultdict

def plot_cm(y_actu,y_pred,title='Confusion Matrix',cmap=plt.cm.summer):
    
    df_confusion = pd.crosstab(y_actu, y_pred.reshape(y_pred.shape[0],), rownames=['Actual'], colnames=['Predicted'], margins=True)
    print(df_confusion)
    df_conf_norm = df_confusion / df_confusion.sum(axis=1)
    
    plt.matshow(df_confusion, cmap=cmap) # imshow
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(df_confusion.columns))
    plt.xticks(tick_marks, df_confusion.columns, rotation=45)
    plt.yticks(tick_marks, df_confusion.index)
    plt.tight_layout()
    plt.ylabel(df_confusion.index.name)
    plt.xlabel(df_confusion.columns.name)
    plt.show()

def insights(Y_actu,df):

    ratingavg=defaultdict(lambda:0)
    priceavg=defaultdict(lambda:0)
    count=defaultdict(lambda:0)
    print(df.shape)
    variety=df["variety"].values
    rating=df["points"].values
    price=df["price"].values
    for i in range(df.shape[0]):
        var=variety[i]
        count[var]+=1
        ratingavg[var]+=rating[i]
        if(pd.isna(price[i])==False):
            priceavg[var]+=price[i]

    for idx in count:
        ratingavg[idx]/=count[idx]
        priceavg[idx]/=count[idx]

    for idx in count:
        if(ratingavg[idx]==max(ratingavg.values())):
            print("Max avg rating",idx, ratingavg[idx])
        if(ratingavg[idx]==min(ratingavg.values())):
            print("Min avg rating",idx, ratingavg[idx])
        if(priceavg[idx]==max(priceavg.values())):
            print("Max avg price",idx,priceavg[idx])
        if(priceavg[idx]==min(priceavg.values())):
            print("Min avg price",idx,priceavg[idx])
        if(count[idx]==min(count.values())):
            print("Least reviewed wine ",idx, count[idx])
        if(count[idx]==max(count.values())):
            print("Most reviewed wine ",idx, count[idx])
        
        