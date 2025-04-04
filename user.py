from action import Action
from display_utils import header, separator


class User:
    """
    User class to represent a user in the game.
    This class will manage the user's budget, wallet and actions.

    Attributes:
        name (str): The name of the user.
        budget (float): The budget of the user.
        wallet (dict): A dictionary to hold items and their amounts.
    """

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        # Dictionary to hold items and their amounts Example: {ID: [item, amount]}
        self.wallet = {}

    def buy(self, item: Action, amount):
        """Buy an item from the market.
        Args:
            item (Action): The item to buy.
            amount (int): The amount of the item to buy.
        Raises:
            ValueError: If the user doesn't have enough budget to buy the item.
        """

        if self.budget < item.price * amount:
            raise ValueError(
                f"Not enough budget to buy {amount} of {item.name}.")

        self.budget -= item.price * amount
        # Update the wallet

        if item.ID in self.wallet:
            self.wallet[item.ID][1] += amount
        else:
            self.wallet[item.ID] = [item, amount]

        print(f"Bought {amount} of {item.name}.")

    def sell(self, ID, amount):
        """Sell an item from the wallet.
        Args:
            ID (int): The ID of the item to sell.
            amount (int): The amount of the item to sell.
        Raises:
            ValueError: If the user doesn't own the item or doesn't have enough amount to sell.        
        """

        if ID not in self.wallet:
            raise ValueError(f"You don't own {ID}.")
        if self.wallet[ID][1] < amount:
            raise ValueError(
                f"You don't have enough {self.wallet[ID][0].name} to sell.")

        self.wallet[ID][1] -= amount
        self.budget += self.wallet[ID][0].price * amount

        print(
            f"Sold {amount} of {self.wallet[ID][0].name} for {self.wallet[ID][0].price * amount:.2f}.")

        if self.wallet[ID][1] == 0:
            del self.wallet[ID]

    def display_wallet(self):
        """Display the user's wallet."""

        print(f"{self.name}'s Wallet:           R$ {self.budget:.2f}")
        print(separator)
        print(header)
        print(separator)
        if not self.wallet:
            print("No actions in the wallet.")
        for action in self.wallet.values():
            action_obj = action[0]
            shares = action[1]
            print(f"{f'#{action_obj.ID:04d}':<6} | {action_obj.name:<10} | " +
                  f"{f'R$ {action_obj.price:.2f}':<10} | {action_obj.level:<10} | " +
                  f"{action_obj.shares:<13} | {shares:<17}")
