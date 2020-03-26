import random
def shuffle():
    'returns shuffled deck'
    suits={'\u2660','\u2661','\u2662','\u2663'}
    ranks={'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    deck=[]
    for suit in suits:
        for rank in ranks:
            deck.append(rank+' '+suit)
    random.shuffle(deck)
    return deck

def deal(deck,player):
    'deal single card from deck to players'
    card=deck.pop()
    player.append(card)
    return card

def total(hand):
    'return the values of the blackjack hand'
    values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
    result=0
    numAces=0
    for card in hand:
        if card[0]=='1':
            result+=values[card[:2]]
        else:
            result+=values[card[0]]
        if card[0]=='A':
            numAces+=1
    while result>21 and numAces>0:
        result-=10
        numAces-=1
    return result

def compare(house,player):
    "compares the total of the house's and player's cards"    
    if total(house)>total(player):
        print('You Lose')
    elif total(house)<total(player):
        print('You Win')
    elif total(house)==21 and 2==len(house)<len(player):
        print('You Lose')
    elif total(player)==21 and 2==len(player)<len(house):
        print('You Win')
    else:
        print('A tie')
    print('\nwanna play again?')
    rstr=input("Press 'R' to restart\t")
    if rstr=='r' or rstr=='R':
        print("\n-----------------------------\n")
        blackjack()

def blackjack():
    'simulates the house'
    deck=shuffle()
    house=[]
    player=[]
    for i in range(2):
        deal(deck,player)
        deal(deck,house)
    print('House:{:>7}{:>7}'.format(house[0],house[1]))
    print('player:{:>7}{:>7}'.format(player[0],player[1]))

    answer=input('Hit or Stand? (default:Hit):\t')
    while answer in {'','h','H','hit','Hit'}:
        card=deal(deck,player)
        print('You got{:>7}'.format(card))

        if total(player)>21:
            print('You went over....You Lose')
            print('\nwanna play again?')
            rstr=input("Press 'R' to restart\t")
            if rstr=='r' or rstr=='R':
                print("\n-----------------------------\n")
                blackjack()
            return
        answer=input('Hit or Stand? (default:Hit):\t')
    while total(house)<17:
        card=deal(deck,house)
        print('House got{:>7}'.format(card))

        if total(house)>21:
            print('House went over....You Win')
            print('\nwanna play again?')
            rstr=input("Press 'R' to restart\t")
            if rstr=='r' or rstr=='R':
                print("\n-----------------------------\n")
                blackjack()
            return

    compare(house,player)
blackjack()
