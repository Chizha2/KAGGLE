from imports import * # импорт пакетов и модулей
from functions import * # импорт функций
warnings.filterwarnings("ignore") # отключение предупреждений

file = pd.read_csv("../zadanie/train.csv", na_values = "NA") # чтение файла, пустые значения = "NA", kaggle

file = NA_filter(file) # удаление лишних фич и замена "NA"
#result, price = graph_data(file) # получение данных для графика
#graph_print(result, price) # вывод графика
code = LabelEncoder() # словарь для кодировки
file = to_categorial(file, code) # перевод категориальных фич в числовые



rmsle_k = 0 # rmsle
mae_k = 0 # mae
k = 0 # счетчик
errors = 0 # ошибки

for j in range(100): # цикл
    model = linear_model.LinearRegression() # создание модели
    x_train, x_test, y_train, y_test = train_test_split(file.drop(columns = ['SalePrice']), file['SalePrice'], test_size = 0.2) # разделение на 4 части (2 тестовых и 2 валидационных)
    y_train = y_train.reshape(-1, 1) # фикс
    y_test = y_test.reshape(-1, 1) # фикс
    x_scaler = StandardScaler().fit(x_train) # скейлер для X
    y_scaler = StandardScaler().fit(y_train) # скейлер для Y
    x_train = x_scaler.transform(x_train) # скайлирование X тренировки
    y_train = y_scaler.transform(y_train) # скайлирование Y тренировки
    x_test = x_scaler.transform(x_test) # скайлирование X тестирования
    model.fit(x_train, y_train) # обучение модели
    predictions = model.predict(x_test) # предположения
    predictions = list(map(lambda x: x * (-1) if x < 0 else x, y_scaler.inverse_transform(predictions))) # дешифровка предположений
    if (mean_absolute_error(y_test, predictions) < 50000): # ошибки нет
        k += 1 # увеличение счетчика
        rmsle_k += rmsle(y_test, predictions) # rmsle
        mae_k += mean_absolute_error(y_test, predictions) # mae
    else: # иначе
        errors += 1 # + ошибка

print("rmsle:", rmsle_k / k, ", mae:", mae_k / k, ", suc_cicles:", k, ", errors:", errors) # вывод