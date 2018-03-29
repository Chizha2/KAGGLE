import pandas as pd # для обработки даных
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

file = pd.read_csv('../zadanie/train.csv', na_values="NA") # чтение файла
file_obj = file.select_dtypes(include=['object']).copy() # копируем поля object в новый data set

for i in file.head():
    print("Head: "+ str(i) + ", valid: " + str( file[i].notnull().sum()/len(file) )) # рассчитываем коэффициент валидных данных
