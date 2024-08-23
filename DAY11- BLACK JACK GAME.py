choice_to_play=input("Do you want to play the game of blackjack ? type 'y' for yes and 'n' for no :").lower()
if choice_to_play=='y':
    Rules="""
    The rules for the game are as below

    1)Our Blackjack Game House Rules
    2)The deck is unlimited in size.
    3)There are no jokers.
    4)The Jack/Queen/King all count as 10.
    5)The Ace can count as 11 or 1.
    6)Use the following list as the deck of cards:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    8)The cards in the list have equal probability of being drawn.
    9)Cards are not removed from the deck as they are drawn.
    10)The computer is the dealer.
    """
    import random
    import black_jack_art as logo
    print(logo.logo)
    print(Rules)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards=[]
    computer_cards=[]
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    sum_of_player_cards=sum(player_cards)
    print(f"Your cards : {player_cards} , current score : {sum_of_player_cards}")

    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    sum_of_computer_cards=sum(computer_cards)
    print(f"Computer's first card : {computer_cards[0]}")

    while sum_of_player_cards<=21 and sum_of_computer_cards<=21:

        another_card=input("Type 'y' to get another card or 'n' to pass :").lower()
        computer_another_card=['y','n']
        computer_choice=random.choice(computer_another_card)

        if another_card=='y':
            player_cards.append(random.choice(cards))
            sum_of_player_cards=sum(player_cards)
            if sum_of_player_cards<=21:
                print(f"Your cards : {player_cards} , current score : {sum_of_player_cards}")
            else:
                print(f"Your cards : {player_cards} , current score : {sum_of_player_cards}")
                print("YOU WENT OVER !!! YOU LOSE")
                break
        else:
            print(f"Your cards : {player_cards} , current score : {sum_of_player_cards}")

        if computer_choice=='y':
            computer_cards.append(random.choice(cards))
            sum_of_computer_cards=sum(computer_cards)
            if sum_of_computer_cards<=21 and sum_of_player_cards<=21:
                print(f"Computer's first card : {computer_cards[0]}")

            if sum_of_player_cards<=21 and sum_of_computer_cards>21:
                print(f"Computer's final hand : {computer_cards}, computer's score = {sum_of_computer_cards}")
                print("COMPUTER WENT OVER !!! YOU WIN ")
                break
        else:
            print(f"Computer's first card : {computer_cards[0]}")

    if sum_of_player_cards<=21 and sum_of_computer_cards<=21:
        if sum_of_player_cards>sum_of_computer_cards:
            print("YOU WIN")
        elif sum_of_player_cards<sum_of_computer_cards:
            print("YOU LOSE")
        else:
            print("TIE")
        
        

        
else:
    print("GOODBYE!!!")
        
        

    


