from imports import * # импорт пакетов и модулей
from functions import * # импорт функций
warnings.filterwarnings("ignore") # отключение предупреждений
file = pd.read_csv("../zadanie/train.csv", na_values = "NA") # чтение файла, пустые значения = "NA"
file = NA_filter(file) # удаление лишних фич и замена "NA"
result, price = graph_data(file) # получение данных для графика
graph_print(result, price) # вывод графика
code = LabelEncoder() # словарь для кодировки
file = to_categorial(file, code) # перевод категориальных фич в числовые

# storage = preprocessing.scale(file) # стандартизация данных (перевод в хранилище)
# train, test = train_test_split(storage, train_size = 0.9) # разделение на обучающую и валидационную выборку
# storage = overturn(storage) # переворот матрицы
# x_datas, y = data_share(storage) # разделение данных
# model = lm.LinearRegression() # создание модели
# model.fit(np.transpose(np.matrix(x_datas)), np.transpose(np.matrix(y))) # обучение модели
# print(model.intercept_, model.coef_) # вывод параметров модели

x_train, x_test, y_train, y_test = train_test_split(file.drop(columns = ['SalePrice']), file['SalePrice'], test_size = 0.25) # разделение на 4 части (2 тестовых и 2 валидационных)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)
from sklearn.preprocessing import StandardScaler
x_scaler = StandardScaler().fit(x_train)
y_scaler = StandardScaler().fit(y_train)
x_train = x_scaler.transform(x_train) 
y_train = y_scaler.transform(y_train)
x_test = x_scaler.transform(x_test)
y_test = y_scaler.transform(y_test)
from sklearn import linear_model
model = linear_model.LinearRegression() 
model.fit(x_train, y_train)

predictions = model.predict(x_test)
print(y_scaler.inverse_transform(predictions))
print("---------------------------------------------------------------------------------------------")
print(y_scaler.inverse_transform(y_test))
from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(y_test, predictions))

p.scatter(y_scaler.inverse_transform(y_test), y_scaler.inverse_transform(predictions))
p.xlabel("True Values")
p.ylabel("Predictions")
p.show()