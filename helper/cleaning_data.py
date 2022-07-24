import numpy as np
import pandas as pd

def cleaning_data(df, rename, datetime, drop_columns):
    '''
    Parameters
    ----------
    df : pd.DataFrame
    rename : dict: {old name : new name}
    datetime : str or list of columns to change to datetime type
    drop :  str or list of columns to remove
    
    Returns
    -------
    data : pd.DataFrame
        Data for modeling
    '''
    
    # rename kolom
    df.rename(columns=rename, inplace=True)
    
    # change to datetime
    for i in datetime:
        df[i] = pd.to_datetime(df[i])
    
    # change string to int
    df["price"] = df["price"].str.replace(",","")
    df["odometer"] = df["odometer"].str.replace(",","")

    df["price"] = df["price"].str.replace("$","", regex=False).astype("int64")
    df["odometer"] = df["odometer"].str.replace("km","").astype("int64")
    
    # drop kolom spesifik
    for i in drop_columns:    
        df.drop([i], axis=1, inplace=True)
    
    # remove outlier
    df = df[(df['price'] >= 500) & (df['price'] <= 40000)] # Inputkan kode disini
    
    # fill null values
    for kol in df.columns:
        if df[kol].dtype == 'object':
            kol_modus = df[kol].mode()[0]
            kol_null_index = df[kol].isna()     
            df.loc[kol_null_index, kol] = kol_modus
        if df[kol].dtype == 'int64':
            kol_median = df[kol].median()
            kol_null_index = df[kol].isna()
            df.loc[kol_null_index, kol] = kol_median
    
    return df