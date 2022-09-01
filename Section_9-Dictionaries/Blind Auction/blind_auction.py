isBidding = True

bid_log = []


def add_new_bid(name, bid):
    new_bidder = {
        "bidder_name": name,
        "amount_bid": bid
    }

    bid_log.append(new_bidder)


def find_highest_bidder():
    highest_bid = 0
    highest_bidder = ""
    for key in bid_log:

        if key['amount_bid'] > highest_bid:
            highest_bid = key['amount_bid']
            highest_bidder = key['bidder_name']

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


while isBidding:
    bidder = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    add_new_bid(name=bidder, bid=bid_amount)
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

    if continue_bid == 'no':
        isBidding = False
        find_highest_bidder()
