# Project 2 README

*You are a Rice Fintech Bootcamp student tasked with a group project on showcasing the skills you've learned thus far in class. Below is what your readme file might look like for your second project.*

# Group 1 - Intelligent Derivations



####

####
#### Our business case is creating a practical application to test historic stock data and predict future performance applying lessons learned throughout the course. Our primary question is to determine the optimal combination and weightings of a user's input portfolio and capital while respecting their risk tolerance.
####
#### Stocks chosen for this project are the following: AMAT, AMD, BHP, DDD, F, FCX, INTC, MSFT, NVDA, QCOM, RIO, TSLA, TSM, and VALE. VOO was used as a control in our project to compare the results of our model to VOO.
---

## Technologies

The programming language for this project is Python. This project was run in VSCode with Jupyter Notebook extension. Additionally, we used Alpaca accounts in order to pull real time data for stocks. We implemented PyPortfolioOpt library that implements portfolio optimization strategies.



---

## Installation Guide

It is extremely important that you install the dependencies listed below, before running this application.

The installations for this application are as follows:
```python
pip install pandas
pip install load_dotenv
pip install alpaca_trade_api
pip install csv
pip install matplotlib.pyplot
pip install requests
pip install pyportfolioopt
pip install classification_report
pip install fire
pip install questionary
```
User will need to launch cli.py in order to launch the portfolio optimization application.


The following steps are required to be followed to make the PyPortfolioOpt package work: Install C++ on your computer from Visual Studio and pip install pyportfolioopt .
Futher installation instructions for PyPortfolioOpt can be found here: https://pyportfolioopt.readthedocs.io/en/latest/index.html

---

## Examples

What the cleaned full calendar year of closing prices for chosen stocks will look like.
![Calendar Yr Closing Prices](https://user-images.githubusercontent.com/85652410/136720277-535ac9c8-7bd1-4387-a6a1-a580780ce352.png)



---

## Usage

We found that using pyportfolioopt is a great tool to be more competitive when comparing to VOO.

An example of what your outputs will look like with pyportfolioopt:

![usage1](https://user-images.githubusercontent.com/85652410/136723182-eb972e18-bf42-4a51-926e-81fc23a8b10a.PNG)



---

## Contributors

This current project was a combined effort of the Rice University Fintech Bootcamp Group 1 members: Ashley Guidot, Vishwanath Subramanian, Forrest Surles, and John Weldon. This project was also unofficially sponsored by chip manufactures and Alpaca.

---

## License

The license for this project is MIT. The MIT License requires copyright and license notices must be preserved.
