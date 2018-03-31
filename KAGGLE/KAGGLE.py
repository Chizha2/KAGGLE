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

price = [] # цены
square = [] # площади
result = [] # результат
for i in file["SalePrice"]: # по столбцу цены
    price.append(int(i / 100)) # добавление в список
for i in file["LotArea"]: # по столбцу площади
    square.append(i) # добавление в список
price.sort() # сортировка
square.sort() # сортировка
for i in range(len(price)): # по массивам
    result.append(price[i] / square[i]) # занесение результата

p.Figure() # создание фигуры
p.title("Цена / площадь") # заголовок
p.gcf().canvas.set_window_title("Цена / площадь") # название окна
p.plot(result, label = "Соотношение", color = "r") # график соотношения
p.show() # отображение фигуры