"""Brut algorithm maximizing benefits from stocks."""
import time
import csv
import tracemalloc


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
        self.weigth = self.calculate_weigth()
        self.value = self.weigth * self.profit

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

    def calculate_weigth(self) -> int:
        """Calculate benefit after two years of investment.

        Returns:
            int: Money received
        """
        return self.price * (self.percentage_benefit / 100)


class StocksCombination:
    """Class representing a combination of stocks."""

    def __init__(self, stocks_list: list[Stock]):
        """Initialize combinations instances.

        Args:
            stocks_list (list[stock]): List of available stock instances
        """
        self.stocks = sorted(stocks_list, key=lambda stock: stock.value, reverse=True)
        self.combinations = self.get_combinations()

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

    def get_combinations(self) -> list:
        """Get all possible combinations of stocks.

        Args:
            number (int): Number of stocks in a combination
            all_combinations (list, optional): List of combinations. Defaults to [].

        Returns:
            list: List of all combinations
        """
        total_price = 0
        combination = []
        for i in self.stocks:
            if total_price + i.price <= 500 and i.price > 0:
                combination.append(i)
                total_price += i.price
        return combination, total_price

    def display_best_combination(self) -> None:
        """Display best combinations of stocks."""
        for stock in self.combinations[0]:
            print(stock)
        print(
            f"Total profit : {self.get_total_profit(self.combinations[0])} euros\
            \nTotal price : {self.combinations[1]} euros\
            \nTotal return : {self.get_total_profit(self.combinations[0]) - self.combinations[1]} euros"
        )


def main():
    """Run main program."""
    start_time = time.time()
    tracemalloc.start()

    file_name = "dataset3.csv"
    stocks_list = []

    with open(file_name, "r") as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader)
        for row in data_reader:
            stocks_list.append(Stock(row[0], float(row[1]), float(row[2])))
        combinations = StocksCombination(stocks_list)

    combinations.display_best_combination()
    print(tracemalloc.get_tracemalloc_memory())
    print(f"Total time : {time.time() - start_time} s")


if __name__ == "__main__":
    main()
