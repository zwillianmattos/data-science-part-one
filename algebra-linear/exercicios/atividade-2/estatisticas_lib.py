from collections import Counter
import math

def media(x):
    return sum(x)/len(x)

def mediana(v):
    n = len(v)
    v_ordenado = sorted(v)
    i_centro = n // 2
    if n % 2 == 1:
        return v_ordenado[i_centro]
    else:
        i_centro_2 = i_centro - 1
        return (v_ordenado[i_centro_2] + v_ordenado[i_centro]) / 2

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
        if count == max_count]

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    x_bar = media(x)
    return [x_i - x_bar for x_i in x]

def sum_of_squares(x):
    return sum([x_i * x_i for x_i in x])

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def desvio_padrao(x):
    return math.sqrt(variance(x))

def dot(v, w):
    return sum(v_i * w_i
        for v_i, w_i in zip(v,w))

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stdev_x = desvio_padrao(x)
    stdev_y = desvio_padrao(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0
