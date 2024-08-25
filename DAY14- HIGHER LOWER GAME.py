import higher_lower_art as art
import higher_lower_gamedata as data
import random
print(art.logo)

score=0
answer=''
first_value=random.choice(data.data)
second_value=random.choice(data.data)
while first_value==second_value:
    second_value=random.choice(data.data)
print(f"Compare A : {first_value['name']}, {first_value['description']} from {first_value['country']}")
print(art.vs)
print(f"Compare B : {second_value['name']}, {second_value['description']} from {second_value['country']}")

play_again=True
while play_again==True:
    user_choice=input("Who has more followers ? Type 'A' or 'B' : ").lower()
    if first_value['follower_count']<second_value['follower_count']:
        answer='b'
    elif first_value['follower_count']>second_value['follower_count']:
        answer='a'
    if answer==user_choice:
        score+=1
        if answer=='b':
            first_value=second_value
        second_value=random.choice(data.data)
        while second_value==first_value:
            second_value=random.choice(data.data)
        print(f"you are right.current score : {score}.")
        play_again=True
    else:
        print(f"Sorry, that's wrong. your score : {score}.")
        play_again=False
        break
    print(f"Compare A : {first_value['name']}, {first_value['description']} from {first_value['country']}")
    print(art.vs)
    print(f"Compare B : {second_value['name']}, {second_value['description']} from {second_value['country']}")
    
    
    
    
    
    


    
    
    
    
    
    

