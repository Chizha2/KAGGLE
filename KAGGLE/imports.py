import pandas as pd # обработка и анализ данных
import numpy as np # вычислительные алгоритмы
from sklearn.preprocessing import LabelEncoder # перевод категориальных в числовые
from sklearn.preprocessing import StandardScaler # скейлеры
from sklearn import linear_model # модель
import matplotlib.pyplot as p # графики
import warnings # настройка предупреждений
import os



# используется только в TEST.py:

from sklearn.metrics import mean_absolute_error # mae
from sklearn.model_selection import train_test_split # разделение на обучающую и валидационную
import math # rmsle