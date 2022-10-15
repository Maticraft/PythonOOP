import typing as t

# Vector product with vectors represented as lists
def vector_product_3d(x: t.List[float], y: t.List[float]) -> t.List[float]:
    return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0]]

print(vector_product_3d([1, 2, 3], [4, 5, 6]))