import pandas as pd # для обработки и анализа данных
import numpy as np # для вычислительных алгоритмов
from sklearn.preprocessing import LabelEncoder # для трансформаций
# le = LabelEncoder()                                                                                                                    ЗАЧЕМ?
from collections import defaultdict # для метода словаря
import warnings # для настройки предупреждений
warnings.filterwarnings("ignore") # отключение предупреждений
import matplotlib.pyplot as p # гистограммы
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

for i in file_obj:
    file[i] = i

# file_obj = file_obj.apply(lambda x: d[x.name].inverse_transform(x)) обратная трансформация

data = {"50k-": 0, "50k - 100k": 0, "100k - 150k": 0, "150k - 200k": 0, "200k - 250k": 0, "250k - 300k": 0, "300k+": 0}
for i in file["SalePrice"]:
    if i < 50000:
        data.update({"50k-": data["50k-"] + 1})
    elif i >= 50000 and i < 100000:
        data.update({"50k - 100k": data["50k - 100k"] + 1})
    elif i >= 100000 and i < 150000:
        data.update({"100k - 150k": data["100k - 150k"] + 1})
    elif i >= 150000 and i < 200000:
        data.update({"150k - 200k": data["150k - 200k"] + 1})
    elif i >= 200000 and i < 250000:
        data.update({"200k - 250k": data["200k - 250k"] + 1})
    elif i >= 250000 and i < 300000:
        data.update({"250k - 300k": data["250k - 300k"] + 1})
    else:
        data.update({"300k+": data["300k+"] + 1})

p.Figure()
p.xlabel("Количество")
p.ylabel("Стоимость") 
p.title("Распределение домов")
p.gcf().canvas.set_window_title("Распределение домов")
p.barh(list(data.keys()), list(data.values()))
p.show()