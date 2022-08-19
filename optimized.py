"""Optimized algorithm maximizing benefits from stocks."""
import csv
from textwrap import dedent

DATA_PATH = "./data/sienna2.csv"
WALLET = 500


class Stock:
    """Class representing financial stocks."""

    def __init__(self, name: str, price: int, percentage_benefit: int):
        """Initialize stock instances.

        Args:
            name (str): Name of a stock
            price (float): Price of a stock
            percentage_benefit (float): Benefit in percentage after 2 years of investment
        """
        self.name = name
        self.price = price
        self.percentage_benefit = percentage_benefit
        self.profit = self.calculate_profit()

    def __str__(self) -> str:
        """Represent a stock.

        Returns:
            str: Stock's name
        """
        return f"{self.name} - Profit {round(self.profit, 2)} - Price {self.price}"

    def calculate_profit(self) -> int:
        """Calculate benefit after two years of investment.

        Returns:
            int: Money received
        """
        return self.price + self.price * (self.percentage_benefit / 100)


class StocksCombination:
    """Class representing a combination from a list of stocks."""

    def __init__(self, stocks_list: list[Stock]):
        """Initialize combinations instances.

        Args:
            stocks_list (list[stock]): List of available stock instances
        """
        self.stocks = sorted(
            stocks_list, key=lambda stock: stock.percentage_benefit, reverse=True
        )
        self.combination = self.get_combination()

    @staticmethod
    def get_total_price(stocks_list: list[Stock]) -> int:
        """Get total price of all stocks in the list.

        Args:
            stocks_list (list[Stock]): A list of stocks

        Returns:
            int: Total price
        """
        price = 0
        for stock in stocks_list:
            price += stock.price
        return price

    @staticmethod
    def get_total_profit(combination: list[Stock]) -> int:
        """Get total profit of all stocks in the list.

        Args:
            combination (list[Stock]): A list of stocks

        Returns:
            int: Total profit
        """
        profit = 0
        for stock in combination:
            profit += stock.profit
        return profit

    def get_combination(self) -> list:
        """Get best combination of stocks with a greedy algorithm.

        Returns:
            list: List of stocks
        """
        total_price = 0
        best_combination = []
        for stock in self.stocks:
            if total_price + stock.price <= WALLET and stock.price > 0:
                best_combination.append(stock)
                total_price += stock.price
        return best_combination

    def display_best_combination(self) -> None:
        """Display best combinations of stocks."""
        print("Stocks to purchase :\n")
        for stock in self.combination:
            print(stock)
        profit = round(self.get_total_profit(self.combination), 2)
        price = round(self.get_total_price(self.combination), 2)
        print(
            dedent(
                f"""
                Total profit : {profit} euros
                Total cost : {price} euros
                Total return : {round(profit - price, 2)} euros
                """
            )
        )


def get_data(path: str) -> list:
    """Read data from a csv file and return a list of Stock objects.

    Args:
        path (str): Path to the csv file

    Returns:
        list: list of Stock objects
    """
    stocks_list = []

    with open(path, "r") as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader)
        for row in data_reader:
            stocks_list.append(Stock(row[0], float(row[1]), float(row[2])))
        return stocks_list


def main():
    """Run main program."""
    stocks_list = get_data(DATA_PATH)
    combination = StocksCombination(stocks_list)
    combination.display_best_combination()


if __name__ == "__main__":
    main()
