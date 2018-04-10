from imports import * # импорт пакетов и модулей

def NA_filter(file): # удаление лишних фич и замена "NA"
    for i in file.head(): # по фичам
        if int(file[i].notnull().sum() / len(file) * 100) < 80: # если > 80% "NA"
            del file[i] # удаление фичи
        else: # иначе
            file[i] = file[i].fillna(file[i].value_counts().idxmax()) # замена всех "NA" фичи на самое популярное значение в ней
    return file # вернуть таблицу

def graph_data(file): # получение данных для графика
    file = file.sort_values("SalePrice") # сортировка по цене
    price = list(file["SalePrice"]) # массив цен
    square = list(file["GrLivArea"]) # массив площадей
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

def to_categorial(file, code): # перевод категориальных фич в числовые
    for i in file.select_dtypes(include = ["object"]): # по объектным фичам
        file[i] = code.fit_transform(file[i]) # перевод 
    return file # вернуть таблицу

def rmsle(real, predicted): # rmsle
    sum = 0.0
    for x in range(len(predicted)):
        if predicted[x] < 0 or real[x] < 0: #check for negative values
            continue
        p = np.log(predicted[x] + 1)
        r = np.log(real[x] + 1)
        sum = sum + (p - r)**2
    return (sum / len(predicted))**0.5
