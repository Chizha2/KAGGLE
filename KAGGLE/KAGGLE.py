import pandas as pd # для обработки данных
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

file = pd.read_csv('../zadanie/train.csv', na_values="NA") # чтение файла
file_obj = file.select_dtypes(include=['object']).copy() # копируем поля object в новый data set


for i in file.head():
   if(int(file[i].notnull().sum() / len(file) * 100) < 80):
       del file[i]


for i in file.head():
    print(str(i) + ", " + str(int(file[i].notnull().sum() / len(file) * 100)) + "%") # рассчитываем коэффициент валидных данных

