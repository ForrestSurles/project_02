"""This script creates an interactive cli for the application.

"""

import fire
from questionary import text, prompt, Separator

user_fail_msg = 'No input was recognized. Please try again.'

def portfolio_modeler():

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
            'type': 'select',
            'name': 'main_menu',
            'message': 'What would you like to do?',
            'choices': function_list,
        },
        {
            'type': 'text',
            'name': 'portfolio_input',
            'message': 'Enter the portfolio tickers',
            'multiline': True,
            'instruction': \
                'one ticker per line, press [Escape] then [Enter] to finish.'
        }
    ]

    # call the menu
    menu_prompt = prompt(options)

    # respond to user input
    if menu_prompt['main_menu'] == function_list[-1] \
        and menu_prompt['are_u_suuure']:

        print('Have a good day.\nNow Exiting...')
        exit()    

    elif menu_prompt['main_menu'] == 'Input Portfolio':
        portfolio_tickers = []
        for ticker in menu_prompt['portfolio_input'].splitlines():
            portfolio_tickers.append(ticker)
        print(f'List of Tickers:\n{portfolio_tickers}')
   elif menu_prompt['main_menu'] == 'Run Model':

    else:
        menu_prompt = prompt(options)
    # input portfolio

    # require portfolio to run model
    # option to redirect to portfolio if none when run model/ if not, menu

    exit()


if __name__ == '__main__':
    fire.Fire(portfolio_modeler())