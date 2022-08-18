"""Brut algorithm maximizing benefits from stocks."""
import csv
import itertools
from textwrap import dedent

DATA_PATH = "./data/bruteforce.csv"
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
        return f"{self.name} - Profit {self.profit}"

    def calculate_profit(self) -> int:
        """Calculate profit after two years of investment.

        Returns:
            int: Money received
        """
        return self.price + self.price * (self.percentage_benefit / 100)


class StocksCombinations:
    """Class representing combinations from a list of stocks."""

    def __init__(self, stocks_list: list[Stock]):
        """Initialize combinations instances.

        Args:
            stocks_list (list[stock]): List of available stock instances
        """
        self.stocks = stocks_list
        self.combinations = self.get_all_combinations(len(self.stocks))
        self.best_combination = self.get_best_combination()

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

    def get_all_combinations(
        self, number_of_stocks: int, all_combinations=[]
    ) -> list[list]:
        """Get all possible combinations of stocks.

        Args:
            number_of_stocks (int): Number of stocks in a combination
            all_combinations (list, optional): List of combinations. Defaults to [].

        Returns:
            list[list]: List of all combinations
        """
        if number_of_stocks == 0:
            return all_combinations
        else:
            all_combinations.append(
                list(itertools.combinations(self.stocks, number_of_stocks))
            )
            return self.get_all_combinations(number_of_stocks - 1, all_combinations)

    def get_best_combination(self) -> tuple[list[Stock]]:
        """Get the best combination in terms of profit out of all combinations.

        Returns:
            tuple[list[Stock]]: A tuple with all stocks in a list, for the best combination
        """
        best_combination_profit = 0
        best_combination = ()
        for combination_list in self.combinations:
            for combination in combination_list:
                profit = self.get_total_profit(combination)
                price = self.get_total_price(combination)
                if profit > best_combination_profit and price <= WALLET:
                    best_combination = combination
                    best_combination_profit = profit
        return best_combination

    def display_best_combination(self) -> None:
        """Display best combinations of stocks."""
        print("Stocks to purchase :\n")
        for stock in self.best_combination:
            print(stock)
        profit = round(self.get_total_profit(self.best_combination), 2)
        price = round(self.get_total_price(self.best_combination), 2)
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
    combination = StocksCombinations(stocks_list)
    combination.display_best_combination()


if __name__ == "__main__":
    main()
