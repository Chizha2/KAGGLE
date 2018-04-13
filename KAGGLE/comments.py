# file = file.fillna(method = "pad") замена всех "NA" кастомным способом
# file_obj = file_obj.apply(lambda x: d[x.name].fit_transform(x)) трансформация
# file_obj = file_obj.apply(lambda x: d[x.name].inverse_transform(x)) обратная трансформация

# x = np.linspace(0, 10, num = 11, endpoint = True) усреднение

# y = np.array(y) преобразование
# x = np.array(x) преобразование
# y = y.reshape((1460, 1)) переворот
# print(y.shape) вывод
# print(x.shape) вывод
# skm.fit(x, y) обучение

# storage = preprocessing.scale(file) стандартизация данных (перевод в хранилище)
# train, test = train_test_split(storage, train_size = 0.9) разделение на обучающую и валидационную выборку
# storage = overturn(storage) переворот матрицы
# x_datas, y = data_share(storage) разделение данных
# model = lm.LinearRegression() создание модели
# model.fit(np.transpose(np.matrix(x_datas)), np.transpose(np.matrix(y))) обучение модели
# print(model.intercept_, model.coef_) вывод параметров модели

# def overturn(storage): переворот матрицы
#     storage_2 = [] временное хранилище
#     temp = [] промежуточный список для переворота
#     for i in range(len(storage[0])): формирует строки
#         for j in range(len(storage)): формирует 1 строку
#             temp.append(storage[j][i]) добавление во временную матрицу
#         storage_2.append(temp) добавление результата
#         temp = [] обновление временного списка
#     return storage_2 вернуть перевёрнутое хранилище

# def data_share(storage): разделение данных
#     x_datas = storage[:-1] отделение данных
#     y = storage[-1] отделение цены
#     return x_datas, y вернуть 2 набора данных

# print(rmsle(y_test, predictions)) кегл

# print(y_scaler.inverse_transform(predictions)) скайлирование предположений в нормальный вид
# print(y_scaler.inverse_transform(y_test)) скайлирование идеала в нормальный вид
# p.plot([0, 800000], [0, 800000], color = "r") прямая
# p.scatter(y_scaler.inverse_transform(y_test), y_scaler.inverse_transform(predictions)) точечная диаграмма из скалированных в нормальный вид идеала и предположения
# p.xlabel("True Values") по X - идеал
# p.ylabel("Predictions") по Y - предсказания
# p.show() отобразить

# y_test = y_scaler.transform(y_test) скайлирование Y тестирования
# y_test = y_scaler.inverse_transform(y_test) дешифрока идеала
# del model

# def rmsle_old(real, predicted): rmsle
#     sum = 0.0
#     for x in range(len(predicted)):
#         if predicted[x] < 0 or real[x] < 0: #check for negative values
#             continue
#         p = np.log(predicted[x] + 1)
#         r = np.log(real[x] + 1)
#         sum = sum + (p - r) ** 2
#     return (sum / len(predicted)) ** 0.5

# predictions = y_scaler.inverse_transform(predictions) дешифровка предположений
# rmsle_k += rmsle_old(y_test, predictions) rmsle

# , kaggle
# from collections import Counter
# import sklearn.linear_model as lm
# from sklearn import preprocessing

# def NA_filter(file): # удаление лишних фич и замена "NA"
#    for i in file.head(): # по фичам
#        if int(file[i].notnull().sum() / len(file) * 100) < 80: # если > 80% "NA"
#            del file[i] # удаление фичи
#        else: # иначе
#            file[i] = file[i].fillna(file[i].value_counts().idxmax()) # замена всех "NA" фичи на самое популярное значение в ней
#    return file # вернуть таблицу

# def to_categorial(file): # перевод категориальных фич в числовые
#    code = LabelEncoder()  # словарь для кодировки
#    for i in file.select_dtypes(include = ["object"]):  # по объектным фичам
#        file[i] = code.fit_transform(file[i])  # перевод
#    return file # вернуть таблицу

# коммит

# def graph_print(result, price_2): # вывод графика
#     p.Figure() # создание фигуры
#     p.title("Площадь / цена") # заголовок графика
#     p.gcf().canvas.set_window_title("Площадь / цена") # название окна
#     p.plot(price_2, result, label = "Соотношение", color = "r") # график
#     p.show() # отображение фигуры

# def graph_print2(real, predict): вывод графика
#     p.Figure() создание фигуры
#     p.title("Цена / площадь") заголовок графика
#     p.gcf().canvas.set_window_title("Цена / площадь") название окна
#     p.plot(real, label = "real", color = "r", alpha = 0.7) график
#     p.plot(predict, label = "predict", color = "b", alpha = 0.7) график
#     p.ticklabel_format(useOffset = False) настройка графика
#     p.ticklabel_format(style = "plain") настройка графика
#     p.legend(mode = "expand", borderaxespad = 0) настройка графика
#     p.show() отображение фигуры

# def graph_data(train): получение данных для графика
#     train = train.sort_values("SalePrice") сортировка по цене
#     price = list(train["SalePrice"]) массив цен
#     square = list(train["GrLivArea"]) массив площадей
#     result = [] результирующий массив
#     k = 0 счетчик 1
#     f = 0 счетчик 2
#     for i in range(len(price)): по строкам
#         k += 1 увеличение счетчика
#         f += square[i] / price[i] занесение результата
#         if k % 10 == 0: условие усреднения
#             result.append(f / 10) добавление результата
#             f = 0 обнуление счетчика
#     k = 0 обнуление счетчика
#     price_2 = [] пустой список для цен
#     for i in range(len(price)): по строкам
#         k += 1 увеличить счетчик
#         f += price[i] изменение промежуточного значения
#         if k % 10 == 0: каждые 10 элементов
#             price_2.append(f / 10) поместить в результат
#             f = 0 обнулить
#     return result, price_2 вернуть данные для графика

# result, price = graph_data(file) получение данных для графика
# graph_print(result, price) вывод графика

# result, price = graph_data(file) # получение данных для графика
# graph_print(result, price) # вывод графика

#    if(splitd == 1): # в случае выбора метода разделения train_test_split
#        x_train, x_test, y_train, y_test = train_test_split(file.drop(columns = [y_col_name]), file[y_col_name], test_size = 0.2) # разделение на 4 части (2 тестовых и 2 валидационных)
#    if(splitd == 2): # в случае выбора разделение попалам
#        splint_cof = int(len(file) / 2) # расчёт и округление половины строк
#        x_train = file.head(splint_cof) # отделение 1 части от массива, с начала
#        x_test = file.tail(len(file)-splint_cof) # отделение 2 части, с конца
#        y_train = x_train[y_col_name] # отделение y части
#        y_test = x_test[y_col_name] # отделение y части
#        x_train = x_train.drop(columns = [y_col_name]) # оставляем только x части
#        x_test = x_test.drop(columns = [y_col_name]) # оставляем только x части