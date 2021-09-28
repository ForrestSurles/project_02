# project_02

Group Members :

- Forrest Surles
	- Taiwan Semiconductor Manufacturing Company  : TSM
	- Qualcomm  : QCOM
	- Vale  : VALE
	- Advanced Micro Devices  : AMD
- Vishwanath Subramanian 
	- BHP  : BHP
	- Rio Tinto  : RIO
	- Freeport McMoran  : FCX
- John Weldon
	- Intel Corp  : INTC
	- Microsoft  : MSFT
	- 3D Systems Corp  : DDD
- Ashley Guidot
	- TSM  : TSM
	- Nvidia  : NVDA
	- Tesla  : TSLA

FINAL PORTFOLIO :
	- TSM   : Taiwan Semiconductor Manufacturing Company
	- QCOM  : Qualcomm
	- AMAT  : Applied Materials
	- AMD   : Advanced Micro Devices
	- NVDA  : Nvidia
	- DDD   : 3D Systems Corp
	- FCX   : Freeport McMoran
	- RIO   : Rio Tinto
	- TSLA  : Tesla
	- F     : Ford Motor Company
	- VALE  : Vale
	- BHP   : BHP
	- INTC  : Intel Corporation
	- MSFT  : Microsoft
	- VLKAF : Volkswagen

END GOAL:
	- Compare two or more ML models for solving a predictive task 

	1. CLI App
	2. Feed a Portfolio/ X amount of capital / What is the ideal weighting?
	3. Calculate those weights/ trade on the selected equities
	4. Train the ML models w/ different strategies to make the most $$$
	5. Profit?

USER INPUTS:
	- Risk Tolerance Level:
		- Conservative
		- Moderately Conservative (cut for time if necessary)
		- Moderate
		- Moderately Aggressive (cut for time if necessary)
		- Aggressive
	- List of Potential Portfolio Options
	- How many to choose
	- Amount of capital
	
DEVELOPMENT:
	- Test the trading Strategy - Testing & Optimization for which to implement
		- DMAC (Dual Moving Average Crossover)
		- Bollinger Bands
	- CLI Interface
	- Data Collection
		- Alpaca? 
		- Check if any tickers are not available
	- Backtesting framework
	- Train the models

ACTION ITEMS: Reconvene Wednesday (2021-09-29)
	- Ashley:
		- Implementing Alpaca API:
			- Check if ticker available
			- Returning historical data from search
			- How much data can we gain access to?
	- Forrest:
		- User Stories -- Outline the CLI App/project
	- John:
		- Implementing Risk Tolerance selection into Trading Strategy
	- Vish:
		- Structure the outline for backtesting and training ML models		
