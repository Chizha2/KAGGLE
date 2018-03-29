import pandas as pd # для обработки даных
file = pd.read_csv('../zadanie/train.csv', na_values="NA") # чтение файла
file_obj = file.select_dtypes(include=['object']).copy() # копируем поля object в новый data set
print(file_obj["Alley"].value_counts())
print("Vsego: " + str(file["Alley"].sum()) + ", nan: " + str(file["Alley"].isnull().sum()))