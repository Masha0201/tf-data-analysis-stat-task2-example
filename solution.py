import pandas as pd
import numpy as np
import math

from scipy.stats import norm


chat_id = 1289160674 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = 0
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 2)/math.sqrt(31), \
           loc - scale * norm.ppf(alpha / 2)/math.sqrt(31)
