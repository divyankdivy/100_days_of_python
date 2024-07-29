print("Welcome to Secret Auction Program")
from art import logo
print(logo)

def highest_bidder(auction_record):
    highest_bid = 0
    for bidder in auction_record:
        bid_amount = auction_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid amount of ${highest_bid}.")


bidding_record = {}
end_auction = False

while not end_auction:
    bidder_name = input("What is your name?\n")
    bidding_price = float(input("What is your bidding price?\n"))
    bidding_record[bidder_name] = bidding_price
    more_bidders = input("Would you like to add more bidders? 'y' or 'n'\n")
    if more_bidders.lower() == 'n':
        end_auction = True
        highest_bidder(bidding_record)
