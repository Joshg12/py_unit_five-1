def sequence(number):
    """
    If the number n is odd - 3*n + 1
    If the number n is even n / 2
    :param number: The starting number for the Hailstone sequence
    :return: The number of steps taken to reach 1
    """
    while number % 2 ==0:
        number= number * 3
    while number % 2 ==1:
        number = number / 3
    print(number)
def main():
    number = int(input("Enter a number."))
    sequence(number)
if __name__ == '__main__':
    main()