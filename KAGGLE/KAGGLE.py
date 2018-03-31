import pandas as pd # для обработки и анализа данных
import numpy as np # для вычислительных алгоритмов
from sklearn.preprocessing import LabelEncoder # для трансформаций
# le = LabelEncoder()                                                                                                                    ЗАЧЕМ?
from collections import defaultdict # для метода словаря
import warnings # для настройки предупреждений
warnings.filterwarnings("ignore") # отключение предупреждений
import matplotlib.pyplot as p # гистограммы
import statistics


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

for i in file_obj: # по столбцам объектного файла
    file[i] = i # копируем изменения в исходный файл

# file_obj = file_obj.apply(lambda x: d[x.name].inverse_transform(x)) обратная трансформация

# data = {"50k-": 0, "50k - 100k": 0, "100k - 150k": 0, "150k - 200k": 0, "200k - 250k": 0, "250k - 300k": 0, "300k+": 0} # словарь для графика
# for i in file["SalePrice"]: # по столбцу цены
#     if i < 50000:
#         data.update({"50k-": data["50k-"] + 1})
#     elif i >= 50000 and i < 100000:
#         data.update({"50k - 100k": data["50k - 100k"] + 1})
#     elif i >= 100000 and i < 150000:
#         data.update({"100k - 150k": data["100k - 150k"] + 1})
#     elif i >= 150000 and i < 200000:
#         data.update({"150k - 200k": data["150k - 200k"] + 1})
#     elif i >= 200000 and i < 250000:
#         data.update({"200k - 250k": data["200k - 250k"] + 1})
#     elif i >= 250000 and i < 300000:
#         data.update({"250k - 300k": data["250k - 300k"] + 1})
#     else:
#         data.update({"300k+": data["300k+"] + 1})
#
# p.Figure() # создание фигуры
# p.xlabel("Количество") # Оx
# p.ylabel("Стоимость") # Oy
# p.title("Распределение домов") # заголовок
# p.gcf().canvas.set_window_title("Распределение домов") # название окна
# p.barh(list(data.keys()), list(data.values())) # создание гистограммы
# p.show() # отображение фигуры


# pricelst Список цен
# spacelst Список домов

p.Figure() # создание фигуры
p.title("Распределение домов") # заголовок
p.gcf().canvas.set_window_title("Распределение домов") # название окна
p.plot(pricelst, label="Цены", color="r") # создание гистограммы цен
p.plot(spacelst, label="Площадь", color="g") # создание гистограммы цен
p.show() # отображение фигуры