import os

GAVEL = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________'
                         `'-------'`
                       .-------------.
                      /_______________'
'''

print(GAVEL)
print("Welcome to the secret auction program.")


def add_new_bid(name, bid_amount):
    """
   Adds a new bid to the auction_bids list.
   """
    auction_bids.append({
        "name": name,
        "bid_amount": bid_amount
    })


def find_highest_bidder(auction_bids):
    """
    Finds and prints the highest bidder and their bid amount.
    """
    highest_name, highest_bid = "", 0
    for auction_bid in auction_bids:
        if auction_bid["bid_amount"] > 0:
            highest_name = auction_bid["name"]
            highest_bid = auction_bid["bid_amount"]

    print(f"Highest bidder is {highest_name}, with bid amount of ${highest_bid}.")


def clear_screen():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


auction_bids = []
auction_continues = True

while auction_continues:

    name = str(input("What is your name?\n"))
    while True:
        try:
            bid = float(input("What is your bid amount?\n$"))
            break
        except ValueError:
            print("Please enter a valid integer for the bid amount.")

    add_new_bid(name, bid)
    other_bidders = str(input("Are there any other bidders? (yes/no)\n"))

    if other_bidders not in ['y', 'yea', 'yes', 'yeah']:
        auction_continues = False
        find_highest_bidder(auction_bids)
        break

    clear_screen()
