"""Brut algorithm maximizing benefits from stocks."""
import time
import csv


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
        self.combinations = self.get_combinations()
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

    def get_combinations(self) -> tuple[list[Stock], int]:
        """Get all possible combinations.

        Returns:
            tuple[list[Stock], int]: A tuple with all stocks in a list, and a total profit.
        """
        all_combinations = []
        for stock in self.stocks:
            combination = [stock]
            for other_stock in self.stocks:
                if (
                    other_stock != stock
                    and (self.get_total_price(combination) + other_stock.price) < 500
                ):
                    combination.append(other_stock)

            all_combinations.append((combination, self.get_total_profit(combination)))
        return all_combinations

    def get_best_combination(self) -> tuple[list[Stock], int]:
        """Get the best combination out of all combinations.

        Returns:
            tuple[list[Stock], int]: A tuple with all stocks in a list, and a total profit, for the best combination
        """
        best_combination_profit = 0
        best_combination = ()
        for combination in self.combinations:
            if combination[1] > best_combination_profit:
                best_combination = combination
                best_combination_profit = combination[1]
        return best_combination


def main():
    """Run main program."""
    start_time = time.time()

    filename = "dataset1.csv"

    stocks_list = []
    line = 0
    with open(filename, "r") as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if line == 0:
                line += 1
                continue
            stocks_list.append(Stock(row[0], float(row[1]), float(row[2])))
        combination = StocksCombination(stocks_list)

    for stock in combination.best_combination[0]:
        print(stock)
    print(f"Total profit : {combination.best_combination[1]}")

    print(time.time() - start_time)


if __name__ == "__main__":
    main()
