def fibonacci(x):
    """
    Ex. fibonacci(5) returns "1 1 2 3 5 "
    :param number: The number of Fibonacci terms to return
    :return: A string consisting of a number of terms of the Fibonacci sequence.
    """


def fib(number):
    a = 1
    b = 2
    list_of_numbers = "1 1 "
    for x in range(number):
        c = a + b
        list_of_numbers += str(c) + " "
        a = b
        b = c
    print(list_of_numbers)



fib(50)

