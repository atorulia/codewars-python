def productFib(prod: int) -> list:
    """
    :param prod: prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
    :return: array with 2 fib numbers and bool
    """
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]
