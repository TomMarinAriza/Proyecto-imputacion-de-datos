
def check_missing_data(data_frame):
    missing_values = data_frame.isnull().sum()
    return missing_values


def description (df):
    description = df.describe()
    return  description


def general_stats (df):
    general_stats = df.info()
    return general_stats
