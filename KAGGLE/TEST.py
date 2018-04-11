from imports import * # импорт пакетов и модулей
from functions import * # импорт функций
warnings.filterwarnings("ignore") # отключение предупреждений

print(" 1.KAGGLE\n 2.KUIP\n") # даём пользователю выбрать
data_code = int(input("Выбирите набор данных:")) # Выбор набора данных

if(data_code == 1): # в случае выбора набора KAGGLE
    file = pd.read_csv("../zadanie/train.csv", na_values = "NA") # чтение файла, пустые значения = "NA", kaggle
    y_col_name = 'SalePrice' # Указания имени столбца для y части
elif(data_code == 2): # в случае выбора набора KUIP
    file = pd.read_csv("../zadanie/kuip_train.csv", na_values = "NA") # чтение файла, пустые значения = "NA", kuip
    y_col_name = 'LUX' # Указания имени столбца для y части
else:
    exit() # в остальных случаях
    
print(" 1.train_test_split\n 2.пополам\n") # даём пользователю выбрать
splitd = int(input("Выберите тип разделения:")) # Выбор типа разделения

file = NA_filter(file, y_name = y_col_name) # удаление лишних фич и замена "NA"
# result, price = graph_data(file) # получение данных для графика
# graph_print(result, price) # вывод графика
code = LabelEncoder() # словарь для кодировки
file = to_categorial(file) # перевод категориальных фич в числовые

rmsle_k = 0 # rmsle
mae_k = 0 # mae
k = 0 # счетчик
errors = 0 # ошибки


for j in range(100): # цикл
    model = linear_model.LinearRegression() # создание модели
    
    if(splitd == 1): # в случае выбора метода разделения train_test_split
        x_train, x_test, y_train, y_test = train_test_split(file.drop(columns = [y_col_name]), file[y_col_name], test_size = 0.2) # разделение на 4 части (2 тестовых и 2 валидационных)
    if(splitd == 2): # в случае выбора разделение попалам
        splint_cof = int(len(file)/2) # расчёт и округление половины строк
        x_train = file.head(splint_cof) # отделение 1 части от массива, с начала
        x_test = file.tail(len(file)-splint_cof) # отделение 2 части, с конца
        y_train = x_train[y_col_name] # отделение y части
        y_test = x_test[y_col_name] # отделение y части
        x_train = x_train.drop(columns = [y_col_name]) # оставляем только x части
        x_test = x_test.drop(columns = [y_col_name]) # оставляем только x части
    
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
