def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_test_1(n):
    n = 5 
    expected_value = 8
    calculated_value = fib(5)
    assert expected_value == calculated_value 

