from operator import truediv
import time
import random


def build_deck():
    values = ['A','K','Q','J']
    for i in range(1,11):
        values.append(str(i))
    deck = []
    for suit in ['H',"S",'D','C']:
        for val in values:
            deck.append(suit + val)
    random.seed(int(time.time() * 100))
    random.shuffle(deck)
    return deck


def get_value(hand):
    results = [0]
    for c in hand:
        card = c[1:]
        if card == 'A':
            for i in range(len(results)):
                results.insert(i*2+1, results[i*2] + 11)
                results[i*2] += 1
        elif card in ['K', 'Q', 'J']:
            for i in range(len(results)):
                results[i] += 10
        else:
            for i in range(len(results)):
                results[i] += int(card)
    results = list(set(results))
    results.sort()
    for i in range(len(results)):
        if i > len(results) - 1:
            continue
        if results[i] > 21:
            results = results[:i]
    return results


def nice_printing(hand, results, player):
    print()
    if len(hand) == 1:
        hand.insert(0, "?")
    print(player, "hand:", *hand)
    if len(results) == 0:
        print("Busted!")
    elif len(results) == 1:
        print("Value:", results[0])
    else:
        print("Possible values:", *results)


def play(deck):
    dealer_hand = []
    player_hand = []
    
    #Initial Player Deal
    temp_card = deck.pop(0)
    print("You draw: " + temp_card)
    player_hand.append(temp_card)
    temp_card = deck.pop(0)

    # down card for dealer
    print("Dealer Draws")
    dealer_hand.append(temp_card)

    # Player & Dealer second deals
    temp_card = deck.pop(0)
    print("You draw: " + temp_card)
    player_hand.append(temp_card)

    temp_card = deck.pop(0)
    print("The Dealer draws: " + temp_card)
    dealer_hand.append(temp_card)

    p_res = get_value(player_hand)
    d_res = get_value(dealer_hand[1:])

    nice_printing(player_hand, p_res, "Player")
    nice_printing(dealer_hand[1:], d_res, "Dealer")
    print()

    player_busted = False
    dealer_busted = False
    done = False
    p_stood = False
    d_stood = False
    round = 0
    while not done:
        if round > 0 :
            time.sleep(1)
        choice = "None"
        while choice not in ['h', 's'] and not p_stood:
            choice = input("H to hit or S to stand: ").strip().lower()
        if choice == 'h':
            temp_card = deck.pop(0)
            print("You draw: " + temp_card)
            player_hand.append(temp_card)
        elif choice == 's':
            print("You Stand")
            choice = "DONE"
            p_stood = True
        p_res = get_value(player_hand)
        nice_printing(player_hand, p_res, "Player")
        if round == 0:
            print("The dealer reveals their first draw:", dealer_hand[0])
            d_res = get_value(dealer_hand)
            nice_printing(dealer_hand, d_res, "Dealer")
        if len(p_res) == 0:
            done = True
            player_busted = True
            break
        print()
        d_res = get_value(dealer_hand)
        flag = False
        for vals in d_res:
             if vals >= 17:
                flag = True
        if not d_stood:
            if flag:
                print("The dealer stands")
                # nice_printing(dealer_hand, d_res, "Dealer")
                d_stood = True
            else:
                temp_card = deck.pop(0)
                print("The Dealer draws: " + temp_card)
                dealer_hand.append(temp_card)
            d_res = get_value(dealer_hand)
            nice_printing(dealer_hand, d_res, "Dealer")        
            if len(d_res) == 0:
                done = True
                dealer_busted = True
                break
        print()
        round += 1
        print("-"*20)
        if p_stood and d_stood:
            break

    p_res = get_value(player_hand)
    nice_printing(player_hand, p_res, "Player")
    
    d_res = get_value(dealer_hand)
    nice_printing(dealer_hand, d_res, "Dealer") 
    if dealer_busted:
        print("You Win!")
    elif player_busted:
        print("You Lost!")
    else:
        player_current = 99999
        p_res = get_value(player_hand)
        for value in p_res:
            if 21 - value < player_current:
                player_current = 21 - value
        dealer_current = 99999
        d_res = get_value(dealer_hand)
        for value in d_res:
            if 21 - value < dealer_current:
                dealer_current = 21 - value
        if player_current == dealer_current:
            print("It's a tie!")
        elif player_current < dealer_current:
            print("You win!")
        else:
            print("You lose!")


def main():
    deck = build_deck()
    play(deck)


if __name__ == '__main__':
    main()