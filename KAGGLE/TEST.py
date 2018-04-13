from module_main import * # импорт основного модуля
from module_test import * # импорт тестового модуля

warnings.filterwarnings("ignore") # отключение предупреждений

print("1. KAGGLE\n2. KUIP") # даём пользователю выбрать
data_code = int(input("Выберите набор данных: ")) # Выбор набора данных
print() # перевод строки

if(data_code == 1): # в случае выбора набора KAGGLE
    file = pd.read_csv("../zadanie/train.csv", na_values = "NA") # чтение файла, пустые значения = "NA", kaggle
    y_col_name = 'SalePrice' # Указания имени столбца для y части
elif(data_code == 2): # в случае выбора набора KUIP
    file = pd.read_csv("../zadanie/kuip_train.csv", na_values = "NA") # чтение файла, пустые значения = "NA", kuip
    y_col_name = 'LUX' # Указания имени столбца для y части
else: # иначе
    exit() # в остальных случаях
    
proportion = float(input("Доля обучающей выборки: ")) # Выбор типа разделения
print() # перевод строки

random = input("Включить рандом? ") # Выбор типа разделения
print() # перевод строки

if (random != "no"): # если нужен рандом
    random = True # присвоить True
else: # иначе
    random = False # присвоить False

file = NA_filter(file, y_name = y_col_name) # удаление лишних фич и замена "NA"
code = LabelEncoder() # словарь для кодировки
file = to_categorial(file) # перевод категориальных фич в числовые

rmsle_k = 0 # rmsle
mae_k = 0 # mae
k = 0 # счетчик
errors = 0 # ошибки


for j in range(100): # цикл
    model = linear_model.LinearRegression() # создание модели
  
    options_1, options_2, result_1, result_2 = train_test_split(file.drop(columns = [y_col_name]), file[y_col_name], test_size = proportion, shuffle = random) # разделение на 4 части
    
    result_1 = result_1.reshape(-1, 1) # фикс
    result_2 = list(result_2) # перевод в список

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
