from imports import * # импорт пакетов и модулей
from functions import * # импорт функций
warnings.filterwarnings("ignore") # отключение предупреждений
file = pd.read_csv("../zadanie/train.csv", na_values = "NA") # чтение файла, пустые значения = "NA"
file = NA_filter(file) # удаление лишних фич и замена "NA"
chlst, price2 = graph_data(file)
graph_print(chlst, price2) # получение данных для графика и его вывод
price, space = graph_data2(file)
graph_print2(price, space, chlst, price2) # получение данных для графика и его вывод
code = LabelEncoder() # словарь для кодировки
file = to_categorial(file, code) # перевод категориальных фич в числовые
storage = preprocessing.scale(file) # стандартизация данных (перевод в хранилище)
train, test =  train_test_split(storage,  train_size = 0.9) # разделение на обучающую и валидационную выборку
storage = overturn(storage) # переворот матрицы
x_datas, y = data_share(storage) # разделение данных
model = lm.LinearRegression() # создание модели
model.fit(np.transpose(np.matrix(x_datas)), np.transpose(np.matrix(y))) # обучение модели
print(model.intercept_, model.coef_) # вывод параметров модели