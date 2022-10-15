import typing as t

# Vector product with vectors represented as dictionaries
def vector_product_3d(x: t.Dict[int, float], y: t.Dict[int, float]) -> t.Dict[int, float]:
    return {
        0: x[1] * y[2] - x[2] * y[1],
        1: x[2] * y[0] - x[0] * y[2],
        2: x[0] * y[1] - x[1] * y[0]
    }

print(vector_product_3d({0: 1, 1: 2, 2: 3}, {0: 4, 1: 5, 2: 6}))