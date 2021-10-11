"""This script creates an interactive cli for the application.

"""

import fire
import questionary as quest

def portfolio_modeler():

    # start the app
    user_name = quest.text(
        'Please enter your name, and then press [Enter].'
    ).ask()
    #user_name response
    name_response = 'No name was recognized. Please ReLaunch the app.'

    if user_name != '':
        name_response = name_response = f'Welcome, {user_name}.'

    # Welcome the user, or indicate no name provided
    print(name_response)

if __name__ == '__main__':
    fire.Fire(portfolio_modeler())