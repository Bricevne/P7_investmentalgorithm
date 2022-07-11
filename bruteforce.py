"""Brut algorithm maximizing benefits from stocks."""

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
        self.combinations = []
        self.best_combination = ()

    @staticmethod
    def get_total_price(stocks_list):
        price = 0
        for stock in stocks_list:
            price += stock.price
        return price

    @staticmethod
    def get_total_profit(combination):
        profit = 0
        for stock in combination:
            profit += stock.profit
        return profit

    def get_combinations(self):
        for stock in self.stocks:
            combination = [stock]
            for other_stock in self.stocks:
                if (
                    other_stock != stock
                    and (self.get_total_price(combination) + other_stock.price) < 500
                ):
                    combination.append(other_stock)

            self.combinations.append((combination, self.get_total_profit(combination)))

    def get_best_combination(self):
        best_combination_profit = 0
        best_combination = ()
        for combination in self.combinations:
            if combination[1] > best_combination_profit:
                best_combination = combination
                best_combination_profit = combination[1]
        self.best_combination = best_combination


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

combination.get_combinations()
combination.get_best_combination()

for stock in combination.best_combination[0]:
    print(stock)
print(f"Total profit : {combination.best_combination[1]}")
