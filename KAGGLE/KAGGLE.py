from imports import * # импорт пакетов и модулей
from functions import * # импорт функций
warnings.filterwarnings("ignore") # отключение предупреждений

file = pd.read_csv("../zadanie/train.csv", na_values = "NA") # чтение файла, пустые значения = "NA", kaggke

file = NA_filter(file) # удаление лишних фич и замена "NA"
#result, price = graph_data(file) # получение данных для графика
#graph_print(result, price) # вывод графика
code = LabelEncoder() # словарь для кодировки
file = to_categorial(file, code) # перевод категориальных фич в числовые


x_train, x_test, y_train, y_real = train_test_split(file.drop(columns = ['SalePrice']), file['SalePrice'], test_size = 0.25) # разделение на 4 части (2 тестовых и 2 валидационных), kaggle

y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

from sklearn.preprocessing import StandardScaler

x_scaler = StandardScaler().fit(x_train) #Настройка для входных данны
y_scaler = StandardScaler().fit(y_train) #настройка для результирующих данных

x_train = x_scaler.transform(x_train) # преобразование обучающих входных данны
y_train = y_scaler.transform(y_train) # преобразование обучающих результирующих данных
x_test = x_scaler.transform(x_test) # преобразование тестовых входных данны
#y_test = y_scaler.transform(y_test) # преобразование тестовых результирующих данных

from sklearn import linear_model

model = linear_model.LinearRegression() # Создание модели линейной регрессии
model.fit(x_train, y_train) # Обучение модели

modelsgd = linear_model.SGDRegressor() # Создание ломели статистического градиента
modelsgd.fit(x_train, y_train) # Обучение модели


y_predict = y_scaler.inverse_transform(model.predict(x_test)) # Предсказание и инвертирование трансформации

#y_real = y_scaler.inverse_transform(y_test) # Инвертирование трансформации, валидационных данных, НУЖНО ЛИ?

from sklearn.metrics import mean_absolute_error
print("Linear")
mae_linear=int(mean_absolute_error(y_real, y_predict)) # Расчёт MAE
rmsle_linear = rmsle(y_real, y_predict) # Расчёт RMSLE
print(mae_linear)
print(rmsle_linear)

print("SGD")
y_predict_sgd = y_scaler.inverse_transform(modelsgd.predict(x_test)) # Предсказание и инвертирование трансформации
mae_sgd=int(mean_absolute_error(y_real, y_predict_sgd)) # Расчёт MAE
rmsle_sgd = rmsle(y_real, y_predict_sgd) # Расчёт RMSLE
print(mae_sgd)
print(rmsle_sgd)

p.Figure()  # создание фигуры
p.title("Сравнение типов регрессий")  # заголовок графика
p.gcf().canvas.set_window_title("Regrassions types compare")  # название окна
p.plot(y_real, label="real", color="r", alpha=0.7)  # график
p.plot(y_predict, label="predict liner, mae:"+str(mae_linear)+", rmsle:"+str(rmsle_linear), color="b", alpha=0.7)  # график
p.plot(y_predict_sgd, label="predict sgd, mae:"+str(mae_sgd)+", rmsle:"+str(rmsle_sgd), color="g", alpha=0.7)  # график
p.ticklabel_format(useOffset=False)
p.ticklabel_format(style='plain')
p.legend(mode="expand", borderaxespad=0)
p.show()  # отображение фигуры

p.scatter(y_real, y_predict)
p.xlabel("True Values")
p.ylabel("Predictions")
p.show()
