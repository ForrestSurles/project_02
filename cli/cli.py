"""This script creates an interactive cli for the application.

"""

import fire
from questionary import text, prompt, Separator
from Portfolio_final import portfolio_final

user_fail_msg = 'No input was recognized. Please try again.'
default_portfolio = [
    "TSM", "QCOM", "VALE", "AMD", "BHP",
    "RIO", "FCX", "INTC", "MSFT", "DDD",
    "NVDA", "TSLA", "AMAT", "F", "VOO"
]

def portfolio_modeler():

    portfolio_tickers= []

    # list of functions for main menu prompt
    function_list = [
        'Input Portfolio',
        'Run Model',
        Separator(),
        'Exit'
    ]

    # ask the user for their name
    user_name = text('Please enter your name, and then press [Enter].').ask()

    # create default response
    name_response = user_fail_msg

    if user_name != '':
        name_response = f'Welcome, {user_name}.'

    # validate a response
    if name_response != user_fail_msg:
        print(name_response)
    else:
        print(f'{user_fail_msg}\nNow Exiting...')
        exit()

    options = [
         {
            'type': 'text',
            'name': 'portfolio_input',
            'message': 'Enter the portfolio tickers',
            'multiline': True,
        },{
            'type': 'select',
            'name': 'main_menu',
            'message': 'What would you like to do?',
            'choices': function_list,
        }
    ]

    confirm_exit = 'N'

    while confirm_exit != 'Y':

        # call the menu
        menu_prompt = prompt(options[1])

        # respond to user input
        if menu_prompt['main_menu'] == function_list[-1]:
            confirm_exit = text('Are you sure you would like to exit? (Y/n)').ask()

        elif menu_prompt['main_menu'] == 'Input Portfolio':
            menu_prompt = prompt(options[0])
            portfolio_tickers = menu_prompt['portfolio_input'].splitlines()
            print(f'List of Tickers:\n{portfolio_tickers}')

        elif menu_prompt['main_menu'] == 'Run Model':
            print('now running, please wait...')
            if len(portfolio_tickers) == 0:
                portfolio_final(tickers=default_portfolio)
            else:
                portfolio_final(tickers=portfolio_tickers)
            print('model complete.')
        else:
            menu_prompt = prompt(options)
        
        if confirm_exit == 'Y':
            print('Have a good day.\nNow Exiting')
            exit()

def main():
    fire.Fire(portfolio_modeler())

if __name__ == '__main__':
    main()