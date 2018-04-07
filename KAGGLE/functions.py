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
    k = 0
    price_2 = []
    for i in range(len(price)):
        k += 1
        f += price[i]
        if k % 10 == 0:
            price_2.append(f / 10)
            f = 0
    return result, price_2 # вернуть данные для графика

def graph_print(result, price_2): # вывод графика
    p.Figure() # создание фигуры
    p.title("Площадь / цена") # заголовок графика
    p.gcf().canvas.set_window_title("Площадь / цена") # название окна
    p.plot(price_2, result, label = "Соотношение", color = "r") # график
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

