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
    p.ticklabel_format(useOffset = False) # настройка графика
    p.ticklabel_format(style = "plain") # настройка графика
    p.legend(mode = "expand", borderaxespad = 0) # настройка графика
    p.show() # отображение фигуры

def rmsle(y, y_pred): # rmsle
	assert len(y) == len(y_pred)
	terms_to_sum = [(math.log(y_pred[i] + 1) - math.log(y[i] + 1)) ** 2.0 for i, pred in enumerate(y_pred)]
	return (sum(terms_to_sum) * (1.0 / len(y))) ** 0.5
