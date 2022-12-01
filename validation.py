def get_input():
   while True:
    number = input("Enter a number fron 1-10")
    if int(number) >=1 and int(number) <= 10:
        return number

def main():
    print(get_input())



if __name__ == '__main__':
    main()
