from imports import * # импорт пакетов и модулей

def NA_filter(train, test, y_name): # удаление лишних фич и замена "NA"
    for i in train.drop(columns = [y_name]).head(): # по фичам без SalePrice
        if int(train[i].notnull().sum() / len(train) * 100) < 80: # если > 80% "NA" в файле train
            del train[i] # удаление фичи
            del test[i] # удаление фичи
        elif int(test[i].notnull().sum() / len(test) * 100) < 80: # если > 80% "NA" в файле test
            del train[i] # удаление фичи
            del test[i] # удаление фичи
        else: # иначе
            train[i] = train[i].fillna(train[i].value_counts().idxmax()) # замена всех "NA" фичи на самое популярное значение в ней
            test[i] = test[i].fillna(test[i].value_counts().idxmax()) # замена всех "NA" фичи на самое популярное значение в ней
    return train, test # вернуть таблицы

def to_categorial(train, test): # перевод категориальных фич в числовые
    encoder = LabelEncoder()  # словарь для кодировки
    for i in train.select_dtypes(include = ["object"]):  # по объектным фичам
        train[i] = encoder.fit_transform(train[i]) # обучение и преобразование
        test[i] = encoder.transform(test[i]) # преобразование
    return train, test # вернуть таблицы



# используется только в TEST.py:
def NA_filter(file): # удаление лишних фич и замена "NA"
    for i in file.head(): # по фичам
        if int(file[i].notnull().sum() / len(file) * 100) < 80: # если > 80% "NA"
            del file[i] # удаление фичи
        else: # иначе
            file[i] = file[i].fillna(file[i].value_counts().idxmax()) # замена всех "NA" фичи на самое популярное значение в ней
    return file # вернуть таблицу
def graph_data(train): # получение данных для графика
    train = train.sort_values("SalePrice") # сортировка по цене
    price = list(train["SalePrice"]) # массив цен
    square = list(train["GrLivArea"]) # массив площадей
    result = [] # результирующий массив
    k = 0 # счетчик 1
    f = 0 # счетчик 2
    for i in range(len(price)): # по строкам
        k += 1 # увеличение счетчика
        f += square[i] / price[i] # занесение результата
        if k % 10 == 0: # условие усреднения
            result.append(f / 10) # добавление результата
            f = 0 # обнуление счетчика
    k = 0 # обнуление счетчика
    price_2 = [] # пустой список для цен
    for i in range(len(price)): # по строкам
        k += 1 # увеличить счетчик
        f += price[i] # изменение промежуточного значения
        if k % 10 == 0: # каждые 10 элементов
            price_2.append(f / 10) # поместить в результат
            f = 0 # обнулить
    return result, price_2 # вернуть данные для графика

def graph_print(result, price_2): # вывод графика
    p.Figure() # создание фигуры
    p.title("Площадь / цена") # заголовок графика
    p.gcf().canvas.set_window_title("Площадь / цена") # название окна
    p.plot(price_2, result, label = "Соотношение", color = "r") # график
    p.show() # отображение фигуры

def graph_print2(real, predict): # вывод графика
    p.Figure() # создание фигуры
    p.title("Цена / площадь") # заголовок графика
    p.gcf().canvas.set_window_title("Цена / площадь") # название окна
    p.plot(real, label = "real", color = "r", alpha=0.7) # график
    p.plot(predict, label = "predict", color = "b", alpha=0.7) # график
    p.ticklabel_format(useOffset=False)
    p.ticklabel_format(style='plain')
    p.legend(mode="expand", borderaxespad=0)
    p.show() # отображение фигуры

def to_categorial(file): # перевод категориальных фич в числовые
    code = LabelEncoder()  # словарь для кодировки
    for i in file.select_dtypes(include=["object"]):  # по объектным фичам
        file[i] = code.fit_transform(file[i])  # перевод

    return file # вернуть таблицу


def rmsle(y, y_pred):
	assert len(y) == len(y_pred)
	terms_to_sum = [(math.log(y_pred[i] + 1) - math.log(y[i] + 1)) ** 2.0 for i,pred in enumerate(y_pred)]
	return (sum(terms_to_sum) * (1.0/len(y))) ** 0.5
