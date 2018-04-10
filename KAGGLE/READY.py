from imports import * # импорт пакетов и модулей
from functions import * # импорт функций
warnings.filterwarnings("ignore") # отключение предупреждений
file = pd.read_csv("../zadanie/train.csv", na_values = "NA") # чтение файла, пустые значения = "NA", kaggle
file_2 = pd.read_csv("../zadanie/test.csv", na_values = "NA")
file, file_2 = NA_filter(file, file_2) # удаление лишних фич и замена "NA"
file, file_2 = to_categorial(file, file_2) # перевод категориальных фич в числовые

model = linear_model.LinearRegression() # создание модели
x_train = file.drop(columns = ['SalePrice'])
y_train = file['SalePrice']
y_train = y_train.reshape(-1, 1) # фикс
x_scaler = StandardScaler().fit(x_train) # скейлер для X
y_scaler = StandardScaler().fit(y_train) # скейлер для Y
z_test = x_scaler.transform(file_2)
x_train = x_scaler.transform(x_train) # скайлирование X тренировки
y_train = y_scaler.transform(y_train) # скайлирование Y тренировки
model.fit(x_train, y_train) # обучение модели

predictions = model.predict(z_test) # предположения
predictions = list(map(lambda x: x * (-1) if x < 0 else x, y_scaler.inverse_transform(predictions))) # дешифровка предположений

p.Figure() # создание фигуры
p.title("цена") # заголовок графика
p.gcf().canvas.set_window_title("цена") # название окна
p.plot(predictions,  color = "r") # график
p.show() # отображение фигуры
