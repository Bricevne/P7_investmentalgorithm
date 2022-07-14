"""Brut algorithm maximizing benefits from stocks."""
import time
import csv
import itertools


class Stock:
    """Class representing financial stocks."""

    def __init__(self, name: str, price: int, percentage_benefit: int):
        """Initialize stock instances.

        Args:
            name (str): Name of a stock
            cost (float): Cost of a stock
            percentage_benefit (float): Benefit in percentage after 2 years of investment
        """
        self.name = name
        self.price = price
        self.percentage_benefit = percentage_benefit
        self.profit = self.calculate_profit()

    def __str__(self) -> str:
        """Represent an action.

        Returns:
            str: Stock's name
        """
        return f"{self.name} - Profit {self.profit}"

    def calculate_profit(self) -> int:
        """Calculate benefit after two years of investment.

        Returns:
            int: Money received
        """
        return self.price + self.price * (self.percentage_benefit / 100)


class StocksCombination:
    """Class representing a combination of stocks."""

    def __init__(self, stocks_list: list[Stock]):
        """Initialize combinations instances.

        Args:
            stocks_list (list[stock]): List of available stock instances
        """
        self.stocks = stocks_list
        self.combinations = self.get_combinations(len(self.stocks))
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

    def get_combinations(self, number: int, all_combinations=[]) -> list:
        """Get all possible combinations of stocks.

        Args:
            number (int): Number of stocks in a combination
            all_combinations (list, optional): List of combinations. Defaults to [].

        Returns:
            list: List of all combinations
        """
        if number == 0:
            return all_combinations
        else:
            all_combinations.append(list(itertools.combinations(self.stocks, number)))
            return self.get_combinations(number - 1, all_combinations)

    def get_best_combination(self) -> tuple[list[Stock], int]:
        """Get the best combination out of all combinations.

        Returns:
            tuple[list[Stock], int]: A tuple with all stocks in a list, and a total profit, for the best combination
        """
        best_combination_profit = 0
        best_combination = ()
        for length in self.combinations:
            for combination in length:
                profit = self.get_total_profit(combination)
                if (
                    profit > best_combination_profit
                    and self.get_total_price(combination) < 500
                ):
                    best_combination = combination
                    best_combination_profit = profit
        return best_combination, best_combination_profit

    def display_best_combination(self) -> None:
        """Display best combinations of stocks."""
        for stock in self.best_combination[0]:
            print(stock)
        print(
            f"Total profit : {self.best_combination[1]} euros\
            \nTotal price : {self.get_total_price(self.best_combination[0])} euros"
        )


def main():
    """Run main program."""
    start_time = time.time()

    file_name = "dataset1.csv"
    stocks_list = []
    line = 0
    with open(file_name, "r") as csv_file:
        data_reader = csv.reader(csv_file)
        for row in data_reader:
            if line == 0:
                line += 1
                continue
            stocks_list.append(Stock(row[0], float(row[1]), float(row[2])))
        combination = StocksCombination(stocks_list)

    combination.display_best_combination()
    print(f"Total time : {time.time() - start_time} s")


if __name__ == "__main__":
    main()
