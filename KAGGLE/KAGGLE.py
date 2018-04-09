from imports import * # импорт пакетов и модулей
from functions import * # импорт функций
warnings.filterwarnings("ignore") # отключение предупреждений
file = pd.read_csv("../zadanie/train.csv", na_values = "NA") # чтение файла, пустые значения = "NA"
file = NA_filter(file) # удаление лишних фич и замена "NA"
result, price = graph_data(file) # получение данных для графика
graph_print(result, price) # вывод графика
code = LabelEncoder() # словарь для кодировки
file = to_categorial(file, code) # перевод категориальных фич в числовые

x_train, x_test, y_train, y_test = train_test_split(file.drop(columns = ['SalePrice']), file['SalePrice'], test_size = 0.2) # разделение на 4 части (2 тестовых и 2 валидационных)
y_train = y_train.reshape(-1, 1) # фикс
y_test = y_test.reshape(-1, 1) # фикс
x_scaler = StandardScaler().fit(x_train) # скейлер для X
y_scaler = StandardScaler().fit(y_train) # скейлер для Y
x_train = x_scaler.transform(x_train) # скайлирование X тренировки
y_train = y_scaler.transform(y_train) # скайлирование Y тренировки
x_test = x_scaler.transform(x_test) # скайлирование X тестирования
y_test = y_scaler.transform(y_test) # скайлирование Y тестирования
model = linear_model.LinearRegression() # создание модели
model.fit(x_train, y_train) # обучение модели

predictions = model.predict(x_test) # предположения
# print(y_scaler.inverse_transform(predictions)) # скайлирование предположений в нормальный вид
# print(y_scaler.inverse_transform(y_test)) # скайлирование идеала в нормальный вид
print(mean_absolute_error(y_test, predictions)) # вывод абсолютной ошибки
p.plot([0, 800000], [0, 800000], color = "r")
p.scatter(y_scaler.inverse_transform(y_test), y_scaler.inverse_transform(predictions)) # точечная диаграмма из скалированных в нормальный вид идеала и предположения
p.xlabel("True Values") # по X - идеал
p.ylabel("Predictions") # по Y - предсказания
p.show() # отобразить