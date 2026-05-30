from auction import Auction
import threading

auction = Auction(
    "Gaming Laptop",
    50000,
    15
)

thread = threading.Thread(
    target=auction.start
)

thread.start()

while thread.is_alive():

    bidder = input(
        "\nBidder Name: "
    )

    amount = int(
        input(
            "Bid Amount: "
        )
    )

    print(
        auction.place_bid(
            bidder,
            amount
        )
    )

print(
    "\nWinner:",
    auction.highest_bidder
)

print(
    "Winning Bid:",
    auction.highest_bid
)