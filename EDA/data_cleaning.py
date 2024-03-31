def imputting_by_mean(df):
    mean_values = df.mean()
    df_imputed = df.fillna(mean_values)
    return df_imputed