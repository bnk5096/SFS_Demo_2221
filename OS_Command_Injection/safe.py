import os

def main():
    search = input("What files should I search? ")
    print(os.listdir(search))


if __name__ == '__main__':
    main()

