import sys
sys.set_int_max_str_digits(0)


def fibonachi(n):
    n_1 = 0
    n_2 = 1
    count = 1
    while count < n:
        yield n_1
        result = n_1 + n_2
        n_1 = n_2
        n_2 = result
        count += 1


def number_fib(n):
    i = 1
    for number in fibonachi(1000000):
        if i == n:
            print(number)
            break
        i += 1


number_fib(6)
number_fib(201)
number_fib(1001)
number_fib(100001)
