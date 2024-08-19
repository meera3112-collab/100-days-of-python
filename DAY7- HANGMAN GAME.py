import hangman_art
import hangman_word
import random

print(hangman_art.logo)
chosen_word=random.choice(hangman_word.word_list)

lives=6
game_over=False
correct_letter=[]

while not game_over:
    guess=(input("Guess an letter:")).lower()


    display=''
    for i in chosen_word:
        if i==guess:
            correct_letter.append(i)
            display+=i
        elif i in correct_letter:
            display+=i
        else:
            display+='-'
    if guess not in chosen_word:
        lives-=1
    print(hangman_art.stages[lives])
    print(display)

    if '-' not in display:
        game_over=True
        print("YOU WIN!!!")
    if lives==0:
        game_over=True
        print("YOU LOOSE!!!")
        print("THE WORD IS :",chosen_word.upper())
        


        
    

