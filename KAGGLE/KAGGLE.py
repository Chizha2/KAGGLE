import pandas as pd # для обработки данных
file = pd.read_csv('../zadanie/train.csv', na_values="NA") # чтение файла
file_obj = file.select_dtypes(include=['object']).copy() # копируем поля object в новый data set

for h in file.head():
    k = 0
    print(h)
    for i in file[h]:
        if pd.notnull(i):
           k += 1
    print(k / len(file))