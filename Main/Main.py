import data_set.reader_file
import EDA.data_cleaning
import tables_manage.tables

df = data_set.reader_file.get_data_set()
print("Informacion del data frame antes de hacer limpieza de datos")

print("\nDatos descriptivos del data frame: ")
print(tables_manage.tables.description(df))

print("\nDatos faltantes en el data frame: ")
print(tables_manage.tables.check_missing_data(df))

print ("\n Datos generales del data frame:")
print(tables_manage.tables.general_stats(df))

print ("Haciendo la limpieza de datos \n")

df_imputed = EDA.data_cleaning.imputting_by_mean(df)

print ("\n Datos imputados: ")
print(df_imputed )