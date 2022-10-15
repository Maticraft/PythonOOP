# Recursive version of binomial coefficient
def newton_binomial_recursive(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return newton_binomial_recursive(n - 1, k - 1) + newton_binomial_recursive(n - 1, k)


# Iterative verions of binomial coefficient
def newton_binomial_iter(n, k):
    if k == 0 or k == n:
        return 1
    else:
        result = 1
        for i in range(1, k + 1):
            result *= (n - i + 1) / i
        return result



assert newton_binomial_recursive(5, 2) == newton_binomial_iter(5, 2)
print(newton_binomial_recursive(5, 2))
print(newton_binomial_iter(5, 2))