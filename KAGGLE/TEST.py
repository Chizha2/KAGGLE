from imports import * # импорт пакетов и модулей
from functions import * # импорт функций
warnings.filterwarnings("ignore") # отключение предупреждений

print("1. KAGGLE\n2. KUIP") # даём пользователю выбрать
data_code = int(input("Выберите набор данных: ")) # Выбор набора данных
print()

if(data_code == 1): # в случае выбора набора KAGGLE
    file = pd.read_csv("../zadanie/train.csv", na_values = "NA") # чтение файла, пустые значения = "NA", kaggle
    y_col_name = 'SalePrice' # Указания имени столбца для y части
elif(data_code == 2): # в случае выбора набора KUIP
    file = pd.read_csv("../zadanie/kuip_train.csv", na_values = "NA") # чтение файла, пустые значения = "NA", kuip
    y_col_name = 'LUX' # Указания имени столбца для y части
else:
    exit() # в остальных случаях
    
proportion = float(input("Доля обучающей выборки: ")) # Выбор типа разделения
print()

random = input("Включить рандом? ") # Выбор типа разделения
print()

if (random != "no"):
    random = True
else:
    random = False

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
  
    options_1, options_2, result_1, result_2 = train_test_split(file.drop(columns = [y_col_name]), file[y_col_name], test_size = proportion, shuffle = random)

#    if(splitd == 1): # в случае выбора метода разделения train_test_split
#        x_train, x_test, y_train, y_test = train_test_split(file.drop(columns = [y_col_name]), file[y_col_name], test_size = 0.2) # разделение на 4 части (2 тестовых и 2 валидационных)
#    if(splitd == 2): # в случае выбора разделение попалам
#        splint_cof = int(len(file)/2) # расчёт и округление половины строк
#        x_train = file.head(splint_cof) # отделение 1 части от массива, с начала
#        x_test = file.tail(len(file)-splint_cof) # отделение 2 части, с конца
#        y_train = x_train[y_col_name] # отделение y части
#        y_test = x_test[y_col_name] # отделение y части
#        x_train = x_train.drop(columns = [y_col_name]) # оставляем только x части
#        x_test = x_test.drop(columns = [y_col_name]) # оставляем только x части
    
    result_1 = result_1.reshape(-1, 1) # фикс
    result_2 = list(result_2)

    options_scaler = StandardScaler().fit(options_1) # скейлер для X
    result_scaler = StandardScaler().fit(result_1) # скейлер для Y
    options_1 = options_scaler.transform(options_1) # скайлирование X тренировки
    result_1 = result_scaler.transform(result_1) # скайлирование Y тренировки
    options_2 = options_scaler.transform(options_2) # скайлирование X тестирования
    model.fit(options_1, result_1) # обучение модели
    predictions = model.predict(options_2) # предположения
    predictions = list(map(lambda x: x * (-1) if x < 0 else x, result_scaler.inverse_transform(predictions))) # дешифровка предположений
    if (mean_absolute_error(result_2, predictions) < 50000): # ошибки нет
        k += 1 # увеличение счетчика
        rmsle_k += rmsle(result_2, predictions) # rmsle
        mae_k += mean_absolute_error(result_2, predictions) # mae
    else: # иначе
        errors += 1 # + ошибка

print("rmsle:", rmsle_k / k, ", mae:", mae_k / k, ", suc_cicles:", k, ", errors:", errors) # вывод
