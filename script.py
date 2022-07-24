import numpy as np
import pandas as pd

from helper.read_data import read_data
from helper.cleaning_data import cleaning_data
from helper.constant import PATH, CHANGE_COLUMN, DATETIME, DROP_COLUMNS
from helper.preprocessing import normal_scaler2
from helper.preprocessing import CategoricalFeatures


from sklearn import preprocessing
from sklearn.preprocessing import normalize
from sklearn.preprocessing import MinMaxScaler

def script():
    # pembacaan dan pengecekan data
    df = read_data(PATH)
    
    # cleaning data
    df = cleaning_data(df, CHANGE_COLUMN, DATETIME, DROP_COLUMNS)
    print("Start Saving Result Feature Engineering!")
    df.to_csv("artifacts/df_clean.csv")
    
    # encoding data kategorical
    kategori = [kol for kol in df.columns if df[kol].dtype == 'object']
    x = CategoricalFeatures(df[kategori], kategori, encoding_type="get_dum")
    df_encoding = x.fit_transform()
    df_encoding.to_csv("artifacts/df_encoding.csv")

    # normalisasi data integer
    numeric_cols = [col for col in df.columns if (df[col].dtype == "int64" and col not in ("price"))]
    df_scaled = normal_scaler2(df[numeric_cols])
    df_scaled.to_csv("artifacts/df_scaled.csv")

    # show training result
    print("------------------------------")
    print("Script selesai dijakankan")

script()