from my_module import greet
from my_module import myDouble

def main():
    name = input("What's your name? ")
    greet(name)

    x = input("Input a value:")
    myDouble(int(x))

if __name__ == '__main__':
    main()
