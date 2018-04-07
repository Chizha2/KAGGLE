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
        if k % 1 == 0: # условие усреднения
            result.append(f / 1) # добавление результата
            f = 0 # обнуление счетчика
    k = 0
    price_2 = []
    for i in range(len(price)):
        k += 1
        f += price[i]
        if k % 1 == 0:
            price_2.append(f / 1)
            f = 0
    return result, price_2 # вернуть данные для графика

def graph_data2(file): # получение данных для графика
    file = file.sort_values("SalePrice") # сортировка по цене
    pricelst = file["SalePrice"].rolling(1, min_periods=1, win_type='boxcar').sum().tolist() #подготовка данных для графика и преобразование в лист
    spacelst = file["GrLivArea"].rolling(1, min_periods=1, win_type='boxcar').sum().tolist() # преобразование в лист
    return pricelst, spacelst # вернуть данные для графика

def graph_print(result, price_2): # вывод графика
    p.Figure() # создание фигуры
    p.title("Площадь / цена") # заголовок графика
    p.gcf().canvas.set_window_title("Площадь / цена") # название окна
    p.plot(price_2, result, label = "Соотношение", color = "r") # график
    p.show() # отображение фигуры

def graph_print2(price, space, chlst, price2): # вывод графика
    p.Figure() # создание фигуры
    figure, bars = p.subplots(2)
    p.title("Цена / площадь") # заголовок графика
    p.gcf().canvas.set_window_title("Цена / площадь") # название окна
    bars[0].plot(price, space, label = "jok", color = "r", alpha=0.7) # график
    bars[1].plot(price2, chlst, label="chizha", color="g", alpha=0.7)
    bars[0].ticklabel_format(useOffset=False)
    bars[0].ticklabel_format(style='plain')
    p.legend(mode="expand", borderaxespad=0)
    p.show() # отображение фигуры

def to_categorial(file, code): # перевод категориальных фич в числовые
    for i in file.select_dtypes(include = ["object"]): # по объектным фичам
        file[i] = code.fit_transform(file[i]) # перевод 
    return file # вернуть таблицу

def overturn(storage): # переворот матрицы
    storage_2 = [] # временное хранилище
    temp = [] # промежуточный список для переворота
    for i in range(len(storage[0])): # формирует строки
        for j in range(len(storage)): # формирует 1 строку
            temp.append(storage[j][i]) # добавление во временную матрицу
        storage_2.append(temp) # добавление результата
        temp = [] # обновление временного списка
    return storage_2 # вернуть перевёрнутое хранилище

def data_share(storage): # разделение данных
    x_datas = storage[:-1] # отделение данных
    y = storage[-1] # отделение цены
    return x_datas, y # вернуть 2 набора данных