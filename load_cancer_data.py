import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

def load_data():
    df_cancer = pd.read_csv("data_wiki/NKI_cleaned.csv")
    df_cancer.reset_index
    df_cancer = df_cancer.set_index("ID")

    y = df_cancer.eventdeath
    X = df_cancer[["survival","timerecurrence","chemo","hormonal","amputation"]]
    cancer_inshape = {"data":X.to_numpy(),"target":y.to_numpy(),"feature_names":X.columns}
    return cancer_inshape
'''
    train_X, val_X, train_y, val_y = sklearn.model_selection.train_test_split(
        cancer_inshape["data"], 
        cancer_inshape["target"], 
        train_size=0.80)
    return train_X, val_X, train_y, val_y
'''