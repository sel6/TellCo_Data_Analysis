import pandas as pd

def format_float(value):
    return f'{value:,.2f}'

def find_agg(db:pd.DataFrame, agg_column:str, agg_metric:str, col_name:str, top:int, order=False )->pd.DataFrame:
    
    new_db = db.groupby(agg_column)[agg_column].agg(agg_metric).reset_index(name=col_name).\
                        sort_values(by=col_name, ascending=order)[:top]
    
    return new_db

def convert_bytes_to_megabytes(db, bytes_data):
    megabyte = 1*10e+5
    db[bytes_data] = db[bytes_data] / megabyte
    
    return db[bytes_data]


def find_total_volume(db, app_names):
    """ This function calculates the total data volume each application"""
    for app_name in app_names:
        db[app_name+' total volume (Bytes)'] = db[app_name+' DL (Bytes)']+db[app_name+' UL (Bytes)']
    return db

pd.options.display.float_format = format_float
