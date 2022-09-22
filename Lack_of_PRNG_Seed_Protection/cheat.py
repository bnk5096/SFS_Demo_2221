import time
import random

def build_starter_deck():
    values = ['A','K','Q','J']
    for i in range(1,11):
        values.append(str(i))
    deck = []
    for suit in ['H',"S",'D','C']:
        for val in values:
            deck.append(suit + val)
    return deck


def build_collection(start, end):
    master = []
    for i in range(start, end):
        deck = build_starter_deck()
        random.seed(i)
        random.shuffle(deck)
        master.append(deck)
    print("Total Posibilites:", len(master))
    return master


def search(master):
    first = input("Enter the first card: ").strip().lower()
    third = input("Enter the third card: ").strip().lower()
    fourth = input("Enter the fourth card: ").strip().lower()
    limited_set = []
    for entry in master:
        if entry[0].lower() == first and entry[2].lower() == third and entry[3].lower() == fourth:
            limited_set.append(entry)
    print("Only", len(limited_set), " posibilities remain")
    print(limited_set)
        



def main():
    start = int(time.time() * 100)
    input("Press enter to lock in")
    end = int(time.time() * 100)
    master = build_collection(start, end)
    search(master)



if __name__ == '__main__':
    main()