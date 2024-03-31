import pandas as pd

def get_data_set():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    data_frame = pd.read_csv('../diabetes.csv')
    return data_frame

