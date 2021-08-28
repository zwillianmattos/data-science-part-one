import math

def vector_subtract(v, w):
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]
def dot(v, w):
    return sum(v_i * w_i
            for v_i, w_i in zip(v, w))
def sum_of_squares(v):
    return dot(v, v)
def magnitude(v):
    return math.sqrt(sum_of_squares(v))
def distance(v, w):
    return magnitude(vector_subtract(v, w))
