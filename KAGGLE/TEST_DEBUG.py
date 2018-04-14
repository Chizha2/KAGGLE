from module_main import * # импорт основного модуля
from module_test import * # импорт тестового модуля

warnings.filterwarnings("ignore") # отключение предупреждений



file = pd.read_csv("../zadanie/kuip_train.csv", na_values = "NA").drop(columns = ['UNIXTIME']) # чтение файла, пустые значения = "NA", kuip

file = NA_filter(file, y_name = "LUX") # удаление лишних фич и замена "NA"
file = to_categorial(file) # перевод категориальных фич в числовые


x_train, x_test, y_train, y_test = train_test_split(file.drop(columns = ["LUX"]), file["LUX"], test_size = 0.4) # разделение на 4 части (2 тестовых и 2 валидационных), kuip

y_train = y_train.reshape(-1, 1) # фикс

x_scaler = StandardScaler().fit(x_train) #Настройка для входных данны
y_scaler = StandardScaler().fit(y_train) #настройка для результирующих данных

x_train = x_scaler.transform(x_train) # преобразование обучающих входных данны
y_train = y_scaler.transform(y_train) # преобразование обучающих результирующих данных
x_test = x_scaler.transform(x_test) # преобразование тестовых входных данны
y_test = list(y_test) # преобразование в лист

model = linear_model.LinearRegression() # Создание модели линейной регрессии
model.fit(x_train, y_train) # Обучение модели

modelsgd = linear_model.SGDRegressor() # Создание ломели статистического градиента
modelsgd.fit(x_train, y_train) # Обучение модели


print("Linear")
y_predict = y_scaler.inverse_transform(model.predict(x_test)) # Предсказание для линейной модели и инвертирование трансформации
y_predict = list(map(lambda x: x * (-1) if x < 0 else x, y_predict)) # дешифровка предположений

mae_linear = int(mean_absolute_error(y_test, y_predict)) # Расчёт MAE
rmsle_linear = rmsle(y_test, y_predict) # Расчёт RMSLE
print(mae_linear) # вывод MAE
print(rmsle_linear) # вывод RMSLE

print("SGD")
y_predict_sgd = y_scaler.inverse_transform(modelsgd.predict(x_test)) # Предсказание для SGD модели и инвертирование трансформации
y_predict_sgd = list(map(lambda x: x * (-1) if x < 0 else x, y_predict_sgd)) # дешифровка предположений
mae_sgd = int(mean_absolute_error(y_test, y_predict_sgd)) # Расчёт MAE
rmsle_sgd = rmsle(y_test, y_predict_sgd) # Расчёт RMSLE

print(mae_sgd) # вывод MAE
print(rmsle_sgd) # вывод RMSLE

p.Figure() # создание фигуры
p.title("Сравнение типов регрессий") # заголовок графика
p.gcf().canvas.set_window_title("Regrassions types compare") # название окна
p.plot(y_test, label = "real", color = "r", alpha = 0.7)  # график
p.plot(y_predict, label = "predict liner, mae:" + str(mae_linear) + ", rmsle:" + str(rmsle_linear), color = "b", alpha = 0.7) # график
p.plot(y_predict_sgd, label = "predict sgd, mae:" + str(mae_sgd) + ", rmsle:" + str(rmsle_sgd), color = "g", alpha = 0.7) # график
p.ticklabel_format(useOffset = False)
p.ticklabel_format(style = "plain")
p.legend(mode = "expand", borderaxespad = 0)
p.show() # отображение фигуры

p.scatter(y_test, y_predict)
p.xlabel("True Values")
p.ylabel("Predictions")
p.show()
