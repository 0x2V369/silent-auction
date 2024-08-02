# Silent Auction Program

This is a simple Python program that simulates a silent auction. Users can enter their names and bid amounts, and the program will determine the highest bidder at the end of the auction.

## Features

- **Multiple Bidders**: Allows multiple users to place their bids.
- **Highest Bidder**: Determines and displays the highest bidder and their bid amount.
- **Clear Screen**: Clears the screen after each bid for privacy (compatible with both Windows and Unix-based systems).
- **Input Validation**: Ensures that bid amounts are valid integers.

## Requirements

- Python 3.x

## How to Use

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/0x2V369/silent-auction.git
    cd silent-auction
    ```

2. **Run the Program:**
    ```sh
    python silent_auction.py
    ```

3. **Follow the Instructions:**
    - Enter your name when prompted.
    - Enter your bid amount.
    - Indicate if there are other bidders.

4. **Example Usage:**
    ```
    Welcome to the secret auction program.
    What is your name?
    Alice
    What is your bid amount?
    $100
    Are there any other bidders? (yes/no)
    yes
    (Screen clears)
    What is your name?
    Bob
    What is your bid amount?
    $150
    Are there any other bidders? (yes/no)
    no
    Highest bidder is Bob, with a bid amount of $150.
    ```

## Code Overview

### Functions

- `add_new_bid(name, bid_amount)`: Adds a new bid to the auction list.
- `find_highest_bidder(auction_bids)`: Finds and prints the highest bidder and their bid amount.
- `clear_screen()`: Clears the console screen for privacy.

### Constants

- `GAVEL`: ASCII art of a gavel displayed at the start of the program.
- `ALPHABET`: List of lowercase letters used in the Caesar cipher.

### Main Loop

The program runs in a loop, allowing multiple bids until the auction is concluded by the users.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This silent auction program was developed by [0x2V369](https://github.com/0x2V369).
