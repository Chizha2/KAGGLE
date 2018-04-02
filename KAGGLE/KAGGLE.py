import pandas as pd # для обработки и анализа данных
import numpy as np # для вычислительных алгоритмов
from sklearn.preprocessing import LabelEncoder # для трансформаций
import warnings # для настройки предупреждений
import matplotlib.pyplot as p # гистограммы
from sklearn import preprocessing
from  sklearn.model_selection  import  train_test_split
import sklearn.linear_model as lm

warnings.filterwarnings("ignore") # отключение предупреждений
file = pd.read_csv("../zadanie/train.csv", na_values = "NA") # чтение файла, пустые значения = "NA"

for i in file.head(): # по столбцам
    if int(file[i].notnull().sum() / len(file) * 100) < 80: # если < 80% "NA"
        del file[i] # удаление стоблца
    else:
        file[i] = file[i].fillna(file[i].value_counts().idxmax()) # замена всех "NA" столбца на самое популярное значение в нем

# file = file.fillna(method = "pad") замена всех "NA" кастомным способом
# file_obj = file_obj.apply(lambda x: d[x.name].fit_transform(x)) # трансформация
# file_obj = file_obj.apply(lambda x: d[x.name].inverse_transform(x)) обратная трансформация

file = file.sort_values("SalePrice")
price = list(file["SalePrice"])
square = list(file["GrLivArea"])
result = []
k = 0
f = 0
for i in range(len(price)): # по массивам
    k += 1
    f += price[i] / square[i] # занесение результата
    if k % 10 == 0:
        result.append(f)
        f = 0

p.Figure() # создание фигуры
p.title("Цена / площадь") # заголовок
p.gcf().canvas.set_window_title("Цена / площадь") # название окна
# x = np.linspace(0, 10, num = 11, endpoint = True)
p.plot(result, label = "Соотношение", color = "r") # график соотношения
p.show() # отображение фигуры

le = LabelEncoder()
for i in file.select_dtypes(include = ["object"]):
    file[i] = le.fit_transform(file[i])

file = preprocessing.scale(file)

train, test =  train_test_split(file,  train_size = 0.9)

file_2 = []
kek = []
for i in range(len(file[0])):
    for j in range(len(file)):
        kek.append(file[j][i])
    file_2.append(kek)
    kek = []
file = file_2

x = file[:-1]
y = file[-1]
skm = lm.LinearRegression()
# y = np.array(y)
# x = np.array(x)
# y = y.reshape((1460, 1))
# print(y.shape)
# print(x.shape)
# skm.fit(x, y)
skm.fit(np.transpose(np.matrix(x)), np.transpose(np.matrix(y)))
print (skm.intercept_, skm.coef_)