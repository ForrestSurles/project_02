#!~/.conda/envs/algo/python.exe
# coding: utf-8

# In[169]:


#Import the Python libraries
from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# In[170]:


def portfolio_final(tickers):
    #Get the stock tickers
    print(tickers)
    # In[171]:

    temp_list = []
    #Assign weights for stocks
    for idx in enumerate(tickers):
        temp_list.append(0.066667)
        weights = np.array(temp_list)


    # In[172]:


    #Set portfolio start date
    stockStartDate = '2019-01-01'


    # In[173]:


    #Set portfolio end date
    today = datetime.today().strftime('%Y-%m-%d')


    # In[174]:


    #Dataframe to store adjusted close price of the stock
    stocks_df = pd.DataFrame()

    for stock in tickers:
        stocks_df[stock] = web.DataReader(stock, data_source='yahoo', start= stockStartDate, end = today)['Adj Close']    


    # In[175]:


    #Review dataframe
    stocks_df.head()


    # In[176]:


    #Review dataframe
    stocks_df.tail()


    # In[177]:


    #Create daily returns DF
    daily_returns_df = stocks_df.pct_change()
    daily_returns_df


    # In[195]:


    #Plot density curves for the portfolio
    daily_returns_df.plot.density(title="Density Plot for Daily Returns")


    # In[178]:


    #Generate the annualized covariance matrix
    annual_cov_matrix = daily_returns_df.cov() * 252
    annual_cov_matrix


    # In[179]:


    #Generate the Portfolio Variance
    portfolio_variance = np.dot(weights.T, np.dot(annual_cov_matrix, weights))
    portfolio_variance


    # In[180]:


    #Generate the Risk MAtrix (Std. Deviation OR Volatility)
    portfolio_volatility = np.sqrt(portfolio_variance)
    portfolio_variance


    # In[181]:


    #Calculate the Annual Portfolio Return
    annual_portfolio_return = np.sum(daily_returns_df.mean() * weights) * 252
    annual_portfolio_return


    # In[182]:


    #Display Expected Annual Return, Volatility (Risk) &  Variance
    percent_variance = str(round(portfolio_variance, 2) * 100) + '%'
    percent_volatility = str(round(portfolio_volatility, 2) * 100) + '%'
    percent_returns = str(round(annual_portfolio_return, 2) * 100) + '%'

    print('Expected Annual Return: '+ percent_returns)
    print('Annual Volatility: '+ percent_volatility)
    print('Annual Variance: '+ percent_variance)


    # In[183]:


    #Import libraries from PyPortfolioOpt
    from pypfopt.efficient_frontier import EfficientFrontier
    from pypfopt import risk_models
    from pypfopt import expected_returns


    # In[184]:


    #Portfolio Optimization for Max Sharpe Ratio
    #Calculate he expected returs, annualized sample covarinace matrix of asset returns
    mu = expected_returns.mean_historical_return(stocks_df)
    S = risk_models.sample_cov(stocks_df)

    #Optimize for the max Sharpe Ratio
    ef = EfficientFrontier(mu, S)
    ef.add_constraint(lambda w: sum(w[0:]) == 1)
    weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()

    print(cleaned_weights)
    ef.portfolio_performance(verbose = True)


    # In[185]:


    #Get the Discrete Allocation  of each share per stock
    from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

    latest_prices = get_latest_prices(stocks_df)
    weights = cleaned_weights

    da = DiscreteAllocation(weights, latest_prices, total_portfolio_value= 1000000)

    allocation, leftover = da.lp_portfolio()

    print('Discrete Allocation:', allocation)
    print('Funds Balance: ${:.2f}'. format(leftover))


    # In[186]:


    #Import modules for plotting
    import copy
    from pypfopt import risk_models, exceptions
    from pypfopt import EfficientFrontier, CLA
    from pypfopt import plotting
    import scipy.cluster.hierarchy as sch
    import warnings


    # In[187]:


    #Plot the Markov Efficient Frontier for Max Sharpe
    #Portfolio Optimization
    #Calculate he expected returns, annualized sample covarinace matrix of asset returns
    mu = expected_returns.mean_historical_return(stocks_df)
    S = risk_models.sample_cov(stocks_df)

    #Optimize for the max Sharpe Ratio
    ef = EfficientFrontier(mu, S)
    ef.add_constraint(lambda w: sum(w[0:]) == 1)

    #Plot instance 
    fig, ax = plt.subplots()
    plotting.plot_efficient_frontier(ef, ax=ax, show_assets=False)

    #Find the Tangency Portfolio
    ef.max_sharpe()
    ret_tangent, std_tangent, _ = ef.portfolio_performance()
    ax.scatter(std_tangent, ret_tangent, marker="*", s=100, c="r", label="Max Sharpe")


    # Generate random portfolios
    n_samples = 10000
    w = np.random.dirichlet(np.ones(len(mu)), n_samples)
    rets = w.dot(mu)
    stds = np.sqrt(np.diag(w @ S @ w.T))
    sharpes = rets / stds
    ax.scatter(stds, rets, marker=".", c=sharpes, cmap="viridis_r")

    # Output
    ax.set_title("Efficient Frontier with random portfolios")
    ax.legend()
    plt.tight_layout()
    plt.savefig("ef_scatter.png", dpi=200)
    plt.show()


    # In[191]:


    # Plot the Markov Efficient Frontier for Min. Risk (Volatility)
    #Portfolio Optimization
    #Calculate he expected returns, annualized sample covarinace matrix of asset returns
    mu = expected_returns.mean_historical_return(stocks_df)
    S = risk_models.sample_cov(stocks_df)

    #Optimize for the minimum risk (volatility)
    ef = EfficientFrontier(mu, S)
    ef.add_constraint(lambda w: sum(w[0:]) == 1)

    #Plot instance 
    fig, ax = plt.subplots()
    plotting.plot_efficient_frontier(ef, ax=ax, show_assets=False)

    #Find the Tangency Portfolio
    ef.min_volatility()
    ret_tangent, std_tangent, _ = ef.portfolio_performance()
    ax.scatter(std_tangent, ret_tangent, marker="*", s=100, c="r", label="Minimum Risk")


    # Generate random portfolios
    n_samples = 10000
    w = np.random.dirichlet(np.ones(len(mu)), n_samples)
    rets = w.dot(mu)
    stds = np.sqrt(np.diag(w @ S @ w.T))
    sharpes = rets / stds
    ax.scatter(stds, rets, marker=".", c=sharpes, cmap="viridis_r")

    # Output
    ax.set_title("Efficient Frontier with random portfolios")
    ax.legend()
    plt.tight_layout()
    plt.savefig("ef_scatter.png", dpi=200)
    plt.show()


    # In[189]:


    #Portfolio Optimization for Max Sharpe Ratio
    #Calculate he expected returs, annualized sample covarinace matrix of asset returns
    mu = expected_returns.mean_historical_return(stocks_df)
    S = risk_models.sample_cov(stocks_df)

    #Optimize for the max Sharpe Ratio
    ef = EfficientFrontier(mu, S)
    ef.add_constraint(lambda w: sum(w[0:]) == 1)
    clean_weights = ef.min_volatility()
    cleaned_weights = ef.clean_weights()

    print(cleaned_weights)
    ef.portfolio_performance(verbose = True)

    #Get the Discrete Allocation  of each share per stock
    from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

    latest_prices = get_latest_prices(stocks_df)
    weights = cleaned_weights

    da = DiscreteAllocation(weights, latest_prices, total_portfolio_value= 1000000)

    allocation, leftover = da.lp_portfolio()

    print('Discrete Allocation:', allocation)
    print('Funds Balance: ${:.2f}'. format(leftover))


    # In[ ]:


    #Get the Discrete Allocation  of each share per stock
    from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

    latest_prices = get_latest_prices(stocks_df)
    weights = cleaned_weights

    da = DiscreteAllocation(weights, latest_prices, total_portfolio_value= 1000000)

    allocation, leftover = da.lp_portfolio()

    print('Discrete Allocation:', allocation)
    print('Funds Balance: ${:.2f}'. format(leftover))


    # In[ ]:


    #Asset clasifcation for Efficient Risk Portfolio
    # Plot the Markov Efficient Frontier for Efficient Risk
    #Portfolio Optimization
    #Calculate he expected returns, annualized sample covarinace matrix of asset returns
    mu = expected_returns.mean_historical_return(stocks_df)
    S = risk_models.sample_cov(stocks_df)

    #Optimize for the Efficient Risk
    ef = EfficientFrontier(mu, S)
    ef.add_constraint(lambda w: sum(w[0:]) == 1)

    #Plot instance 
    fig, ax = plt.subplots()
    plotting.plot_efficient_frontier(ef, ax=ax, show_assets=False)

    #Find the Tangency Portfolio

    ef.efficient_risk(0.30)
    ret_tangent, std_tangent, _ = ef.portfolio_performance()
    ax.scatter(std_tangent, ret_tangent, marker="*", s=100, c="r", label="Efficient Risk")


    # Generate random portfolios
    n_samples = 10000
    w = np.random.dirichlet(np.ones(len(mu)), n_samples)
    rets = w.dot(mu)
    stds = np.sqrt(np.diag(w @ S @ w.T))
    sharpes = rets / stds
    ax.scatter(stds, rets, marker=".", c=sharpes, cmap="viridis_r")

    # Output
    ax.set_title("Efficient Frontier with random portfolios")
    ax.legend()
    plt.tight_layout()
    plt.savefig("ef_scatter.png", dpi=200)
    plt.show()


    # In[192]:


    #Portfolio Optimization for Efficient Risk (User input)
    #Calculate he expected returs, annualized sample covarinace matrix of asset returns
    mu = expected_returns.mean_historical_return(stocks_df)
    S = risk_models.sample_cov(stocks_df)

    #Optimize for the max Sharpe Ratio
    ef = EfficientFrontier(mu, S)
    ef.add_constraint(lambda w: sum(w[0:]) == 1)
    clean_weights = ef.efficient_risk(0.30)
    cleaned_weights = ef.clean_weights()

    print(cleaned_weights)
    ef.portfolio_performance(verbose = True)


    #Get the Discrete Allocation  of each share per stock
    from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

    latest_prices = get_latest_prices(stocks_df)
    weights = cleaned_weights

    da = DiscreteAllocation(weights, latest_prices, total_portfolio_value= 1000000)

    allocation, leftover = da.lp_portfolio()

    print('Discrete Allocation:', allocation)
    print('Funds Balance: ${:.2f}'. format(leftover))


    # In[193]:


    #Get the Discrete Allocation  of each share per stock
    from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

    latest_prices = get_latest_prices(stocks_df)
    weights = cleaned_weights

    da = DiscreteAllocation(weights, latest_prices, total_portfolio_value= 1000000)

    allocation, leftover = da.lp_portfolio()

    print('Discrete Allocation:', allocation)
    print('Funds Balance: ${:.2f}'. format(leftover))

