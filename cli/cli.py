"""This script creates an interactive cli for the application.

"""

import fire
from questionary

def portfolio_modeler():
    questions = [
        {
            'type': 'confirm',
            'name': 'no_user_input',
            'message': 'No input was recognized. Please try again.',
            'default': True
        },
        {
            'type': 'text',
            'name': 'user_name',
            'message': 'Please enter your name, and then press [Enter].',
            # validate user input
            'when': lambda x: x['no_user_input'],
            # only accept non-empty string
            'validate': lambda val: val != ''
        }
    ]

        # Welcome the user, or indicate no name provided


if __name__ == '__main__':
    fire.Fire(portfolio_modeler())