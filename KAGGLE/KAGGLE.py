import pandas as pd # для обработки и анализа данных
import numpy as np # для вычислительных алгоритмов
from sklearn.preprocessing import LabelEncoder # для трансформаций
# le = LabelEncoder()                                                                                                                    ЗАЧЕМ?
from collections import defaultdict # для метода словаря
import warnings # для настройки предупреждений
warnings.filterwarnings("ignore") # отключение предупреждений
d = defaultdict(LabelEncoder) # создание словаря для трансформаций

file = pd.read_csv("../zadanie/train.csv", na_values = "NA") # чтение файла, пустые значения = "NA"

for i in file.head(): # по столбцам
    if int(file[i].notnull().sum() / len(file) * 100) < 80: # если < 80% "NA"
        del file[i] # удаление стоблца
    else:
        file[i] = file[i].fillna(file[i].value_counts().idxmax()) # замена всех "NA" столбца на самое популярное значение в нем

# file = file.fillna(method = "pad") замена всех "NA" кастомным способом
# file_obj = file.select_dtypes(include = ["object"]).copy() копируем поля object в новый data set                                       ЗАЧЕМ?
# for i in file.select_dtypes(include = ["object"]): по объектным столбцам

file_obj = file.select_dtypes(include = ["object"]) # создаем file_obj, где остаются только объектные столбцы
file_obj = file_obj.apply(lambda x: d[x.name].fit_transform(x)) # трансформация

# file_obj = file_obj.apply(lambda x: d[x.name].inverse_transform(x)) обратная трансформация