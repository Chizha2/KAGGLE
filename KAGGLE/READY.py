from libraries_main import * # импорт пакетов и модулей
from libraries_test import * # импорт пакетов и модулей
from functions_main import * # импорт функций

warnings.filterwarnings("ignore") # отключение предупреждений

train = pd.read_csv("../zadanie/train.csv", na_values = "NA").drop(columns = ['Id']) # чтение train файла, пустые значения = "NA", удаление Id
train = train.sample(frac = 1) # перемешивание строк
test = pd.read_csv("../zadanie/test.csv", na_values = "NA") # чтение test файла, пустые значения = "NA"
result = pd.DataFrame() # таблица для результата
result['Id'] = test['Id'] # копирование Id из test файла в result файл
test = test.drop(columns = ['Id']) # удаление Id из test файла

train, test = NA_filter(train, test) # удаление лишних фич и замена "NA"
train, test = to_categorial(train, test) # перевод категориальных фич в числовые

answer = "no" # предустановленный ответ
while (answer != "yes"): # цикл проверки
    model = linear_model.LinearRegression() # создание модели
    train_options = train.drop(columns = ['SalePrice']) # обучающие параметры
    train_result = train['SalePrice'] # обучающий результат
    train_result = train_result.reshape(-1, 1) # переворот

    fit_pd = pd.merge(train_options, test, how = "outer") # склейка таблиц
    scaler_options = StandardScaler().fit(fit_pd) # обучение скейлера по параметрам
    scaler_result = StandardScaler().fit(train_result) # обучение скейлера по результату
    test_options = scaler_options.transform(test) # преобразование параметров файла test
    train_options = scaler_options.transform(train_options) # преобразование параметров файла train
    train_result = scaler_result.transform(train_result) # преобразование результата файла train

    model.fit(train_options, train_result) # обучение модели
    test_result = model.predict(test_options) # предположения
    test_result = list(map(lambda x: x * (-1) if x < 0 else x, scaler_result.inverse_transform(test_result))) # дешифровка предположений, модуль на отрицательные

    p.Figure() # создание фигуры для проверки адекватности
    p.title("Предсказанные цены") # заголовок графика
    p.gcf().canvas.set_window_title("Предсказанные цены") # название окна
    p.plot(test_result) # график
    p.show() # отображение фигуры
    answer = input("Модель корректна? ") # ввод пользователя

test_result = list(map(lambda x: float(x), test_result)) # перевод предсказаний во float
result['SalePrice'] = test_result # добавление в результат столбца с предсказанными ценами
os.remove("./result.csv") # удаление старого файла
result.to_csv("./result.csv", header = True, index = False) # сохранение результата