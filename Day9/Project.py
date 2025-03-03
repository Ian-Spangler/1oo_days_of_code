print("Welcome to tthe secret auction program.")

bids = {}
bidding = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for key in bids:
        if bids[key] > highest_bid:
            highest_bid = bids[key]
            winner = key

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while bidding :
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    bids[name] = bid
    if other_bidders == "yes":
        bidding = True
        print("\n" * 20)
    elif other_bidders == "no":
        bidding = False
        find_highest_bidder(bids)

