import os

def main():
    search = input("What files should I search? ")
    os.system("ls -lah " + search)


if __name__ == '__main__':
    main()

