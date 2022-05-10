import numpy as np
import pandas as pd
import os

def load_data(path):
    db = pd.read_csv(path)
    return db

def percent_missing(db):
    totalCells = np.product(df.shape)
    missingCount = df.isnull().sum()
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The TellCo dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")


def handle_missing_values(db: pd.DataFrame) -> pd.DataFrame:
    perc = 30.0
    min_count = int(((100-perc)/100)*db.shape[0] +1)
    mod_db = db.dropna(axis=1, thresh=min_count)

    return mod_db

def fill_missing_values(mod_db: pd.DataFrame) -> pd.DataFrame:
    #store object type columns and numberic type columns in different lists
    obj_type = [col for col in mod_db.columns.tolist() if mod_db.dtypes[col] == object]
    num_type = [col for col in mod_db.columns.tolist() if mod_db.dtypes[col] == float]

    #for object type columns use mode
    for c in obj_type:
        mod_db[c] = mod_db[c].fillna(mod_db[c].mode()[0])
    #for numeric type columns use median
    for c in num_type:
        mod_db[c] = mod_db[c].fillna(mod_db[c].median())

    return mod_db
    

if __name__== '__main__':
    path = "Week1_challenge_data_source (1).csv"
    db = pd.read_csv(path)
    modified = handle_missing_values(db)
    filled = handle_missing_values(modified)
    
