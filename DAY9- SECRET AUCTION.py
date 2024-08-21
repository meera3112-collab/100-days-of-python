import secret_auction_logo as logo
print(logo.logo)

try_again='yes'
bidders_data={}
def bidding(bidders_data):
    max_val=0
    winner=''
    for name in bidders_data:
        if bidders_data[name]>max_val:
            max_val=bidders_data[name]
            winner=name
    print(f"The winner is {winner} with a bid of ${max_val}.")


while try_again=='yes':
    name=input("What is your name? ")
    bid=int(input("what is your bid ? $"))
    bidders_data[name]=bid
    try_again=input("Are there any other bidders? type 'yes' or 'no':").lower()
    if try_again=='no':
        bidding(bidders_data)
        print("Thank you for bidding")
    elif try_again=='yes':
        print("\n"*45)
    else:
        print("Invalid input")
        





