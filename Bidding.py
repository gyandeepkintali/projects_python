bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid: $"))
    bids[name] = price
    should_continue = input("Do I have any other bids: yes or no: ")
    if should_continue.lower() == "no":
        continue_bidding = False
        
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
    
find_highest_bidder(bids)
