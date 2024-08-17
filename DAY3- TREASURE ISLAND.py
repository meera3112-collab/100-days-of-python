print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
input1=input("you are in front of 3 doors which one do you want to enter type y for yellow, b for blue, g for green")
if input1=='b':
    input2=input("you are at an turning point do you wanna take right or left type r for right and l for left")
    if input2=='r':
        print("you stepped onto an trap")
        print("GAME OVER !!!")
    else:
        input3=input("you are now before two boxes which one do you wanna open type 1 for box1 or 2 for box2")
        if input3=='1':
            print("congratulations !!! you've found the treasure")
        else:
            print("you've opened an explosive. BOOM!!!")
            print("GAME OVER !!!")

if input1=='y':
    print("you've entered an burning building(ablaze)")
    print("GAME OVER!!!")
if input1=='g':
    input4=input("you've entered an castle which staircase do you wanna choose type r for right and l for left")
    if input4=='r':
        print("you've caught by an guard, you're now an prisoner")
        print("GAME OVER")
    else:
        input5=input("there are two keys infront of you type 1 for key1 and 2 for key 2")
        if input5=='1':
            print("it's an trap.you're exploded")
            print("GAME OVER!!!")
        else:
            input6=input("you have two boxes infront of you which one do u want to open. type 1 for box1 and 2 for box2")
            if input6==1:
                print("congratulations!!! You've found the treasure")
                print("YOU WON !!!")
            else:
                print("it's an trap")
                print("GAME OVER!!!")

                


