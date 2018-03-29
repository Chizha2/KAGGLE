import pandas as pd # для обработки даных
file = pd.read_csv('../zadanie/train.csv', na_values="NA") # чтение файла
file_obj = file.select_dtypes(include=['object']).copy() # копируем поля object в новый data set
print(file_obj["Alley"].value_counts())
print("Vsego: " + str(pd.to_numeric(file["Alley"], errors='coerce').sum()) + ", nan: " + str(pd.to_numeric(file["Alley"].isnull(), errors='coerce').sum()))