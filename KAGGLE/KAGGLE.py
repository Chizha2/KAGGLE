import pandas as pd # для обработки данных
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

file = pd.read_csv('../zadanie/train.csv', na_values="NA") # чтение файла


for i in file.head():
    if int(file[i].notnull().sum() / len(file) * 100) < 80: # рассчитываем коэффициент валидных данных
        del file[i]
    else:
        file[i] = file[i].fillna(file[i].value_counts().idxmax())

#file = file.fillna(method='pad')

# file_obj = file.select_dtypes(include=['object']).copy() # копируем поля object в новый data set

for i in file.select_dtypes(include=['object']):
    if