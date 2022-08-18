# Solve problems using algorithms in Python - Openclassrooms project 7

This project is about optimizing investment strategies in order to clients' profits through algorithms

## Installation

Clone the repository on your computer.

`git clone https://github.com/Bricevne/P7_investmentalgorithm.git` 

Set your virtual environment under python 3.10

Create the virtual environment and install the dependencies:

`pipenv install` 

Activate the virtual environment:

`pipenv shell`

Install the necessary libraries in the virtual environnement:

`pipenv install -r requirements.txt`


## Usage

### 1. bruteforce.py :

This program checks every possible combination of stocks from the "dataset1.csv" file in order to obtain the combination with the best profitability.

Run the code :

`python3 bruteforce.py`

### 2. optimized.py :

This program uses a greedy algorithm in order to solve a knapsack like problem efficiently. Only one combination is obtained.
2 csv files are used for Sienna's files:

- 'dataset2.csv'
- 'dataset3.csv'

Run the code :

`python3 optimized.py`

## License

MIT