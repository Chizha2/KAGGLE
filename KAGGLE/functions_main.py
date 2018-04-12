from imports import * # импорт пакетов и модулей

def NA_filter(train, test = None, y_name = "SalePrice"): # удаление лишних фич и замена "NA"
    for i in train.drop(columns = [y_name]).head(): # по фичам без SalePrice
        if int(train[i].notnull().sum() / len(train) * 100) < 80: # если > 80% "NA" в файле train
            del train[i] # удаление фичи
            if test is not None: # если не пусто
                del test[i] # удаление фичи
        elif test is not None and int(test[i].notnull().sum() / len(test) * 100) < 80 : # если > 80% "NA" в файле test
            del train[i] # удаление фичи
            del test[i] # удаление фичи
        else: # иначе
            train[i] = train[i].fillna(train[i].value_counts().idxmax()) # замена всех "NA" фичи на самое популярное значение в ней
            if test is not None: # если не пусто
                test[i] = test[i].fillna(test[i].value_counts().idxmax()) # замена всех "NA" фичи на самое популярное значение в ней
    if(test is not None): # если не пусто
        return train, test # вернуть таблицы
    
    return train # вернуть таблицы

def to_categorial(train, test = None): # перевод категориальных фич в числовые
    encoder = LabelEncoder()  # словарь для кодировки
    for i in train.select_dtypes(include = ["object"]): # по объектным фичам
        train[i] = encoder.fit_transform(train[i]) # обучение и преобразование
        if test is not None: # если не пусто
            test[i] = encoder.transform(test[i]) # преобразование
    if(test is not None): # если не пусто
        return train, test # вернуть таблицы
    
    return train # вернуть таблицы