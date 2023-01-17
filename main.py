import os
import art

print(art.logo)
print("Welcome to the secret auction program.")

bids = []
bidders = True

while bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))

    log = {name: bid}
    bids.append(log)

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if other_bidders == 'no':
        bidders = False

    # on windows
    os.system('cls')
    # on linux / os x
    # os.system("clear")

max_bid = 0

for bid in bids:
    for bidder in bid:
        bid_amount = bid[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder

print(f"The winner is {winner} with a bid of ${max_bid}.")