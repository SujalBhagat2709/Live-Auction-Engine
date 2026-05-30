import time

class Auction:

    def __init__(
        self,
        item_name,
        starting_price,
        duration
    ):

        self.item_name = item_name
        self.highest_bid = starting_price
        self.highest_bidder = None
        self.duration = duration

    def place_bid(
        self,
        bidder,
        amount
    ):

        if amount > self.highest_bid:

            self.highest_bid = amount

            self.highest_bidder = bidder

            return "Bid Accepted"

        return "Bid Rejected"

    def start(self):

        print(
            f"Auction Started For "
            f"{self.item_name}"
        )

        for remaining in range(
            self.duration,
            0,
            -1
        ):

            print(
                f"Time Left: "
                f"{remaining}s"
            )

            time.sleep(1)

        print("\nAuction Ended")