from libraries_test import * # импорт тестовых библиотек

def rmsle(y, y_pred): # rmsle
	assert len(y) == len(y_pred) # чужой код
	terms_to_sum = [(math.log(y_pred[i] + 1) - math.log(y[i] + 1)) ** 2.0 for i, pred in enumerate(y_pred)] # чужой код
	return (sum(terms_to_sum) * (1.0 / len(y))) ** 0.5 # чужой код
