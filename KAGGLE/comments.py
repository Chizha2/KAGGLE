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

#def overturn(storage): переворот матрицы
#    storage_2 = [] временное хранилище
#    temp = [] промежуточный список для переворота
#    for i in range(len(storage[0])): формирует строки
#        for j in range(len(storage)): формирует 1 строку
#            temp.append(storage[j][i]) добавление во временную матрицу
#        storage_2.append(temp) добавление результата
#        temp = [] обновление временного списка
#    return storage_2 вернуть перевёрнутое хранилище

# def data_share(storage): разделение данных
#    x_datas = storage[:-1] отделение данных
#    y = storage[-1] отделение цены
#    return x_datas, y вернуть 2 набора данных

# print(rmsle(y_test, predictions)) кегл

# print(y_scaler.inverse_transform(predictions)) скайлирование предположений в нормальный вид
# print(y_scaler.inverse_transform(y_test)) скайлирование идеала в нормальный вид
# p.plot([0, 800000], [0, 800000], color = "r") прямая
# p.scatter(y_scaler.inverse_transform(y_test), y_scaler.inverse_transform(predictions)) точечная диаграмма из скалированных в нормальный вид идеала и предположения
# p.xlabel("True Values") по X - идеал
# p.ylabel("Predictions") по Y - предсказания
# p.show() отобразить

# y_test = y_scaler.transform(y_test) # скайлирование Y тестирования
# y_test = y_scaler.inverse_transform(y_test) # дешифрока идеала
# del model