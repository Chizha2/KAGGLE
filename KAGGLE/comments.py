# file = file.fillna(method = "pad") замена всех "NA" кастомным способом
# file_obj = file_obj.apply(lambda x: d[x.name].fit_transform(x)) # трансформация
# file_obj = file_obj.apply(lambda x: d[x.name].inverse_transform(x)) обратная трансформация

# x = np.linspace(0, 10, num = 11, endpoint = True)

# y = np.array(y)
# x = np.array(x)
# y = y.reshape((1460, 1))
# print(y.shape)
# print(x.shape)
# skm.fit(x, y)

# storage = preprocessing.scale(file) # стандартизация данных (перевод в хранилище)
# train, test = train_test_split(storage, train_size = 0.9) # разделение на обучающую и валидационную выборку
# storage = overturn(storage) # переворот матрицы
# x_datas, y = data_share(storage) # разделение данных
# model = lm.LinearRegression() # создание модели
# model.fit(np.transpose(np.matrix(x_datas)), np.transpose(np.matrix(y))) # обучение модели
# print(model.intercept_, model.coef_) # вывод параметров модели

#def overturn(storage): # переворот матрицы
#    storage_2 = [] # временное хранилище
#    temp = [] # промежуточный список для переворота
#    for i in range(len(storage[0])): # формирует строки
#        for j in range(len(storage)): # формирует 1 строку
#            temp.append(storage[j][i]) # добавление во временную матрицу
#        storage_2.append(temp) # добавление результата
#        temp = [] # обновление временного списка
#    return storage_2 # вернуть перевёрнутое хранилище

# def data_share(storage): # разделение данных
#    x_datas = storage[:-1] # отделение данных
#    y = storage[-1] # отделение цены
#    return x_datas, y # вернуть 2 набора данных

# print(rmsle(y_test, predictions))