def get_sum(number):
    total = 0
    for x in range(number):
        if x % 3 == 0:
            print("The number is a multiple.")
            total += x
            print(x)

get_sum(100)
print