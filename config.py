'''This config module contains all the sensitive configuration values needed to run the send_email module
and the ebay_buy_it_now_search_tool.
'''

import json

class Config():
    '''The Config class reads a JSON file that contains the configuration values for the 'send_email' module and
    the 'ebay_buy_it_now_search_tool.py' module.'''
    def __init__(self):
        with open('config.json', 'r') as json_object:
            config = json.load(json_object)
            self.api_key = config['api_key']
            self.sending_email_address = config['sending_email_address']
            self.sending_email_address_password = config['sending_email_address_password']
            self.receiving_email_address = config['receiving_email_address']
            self.wait_time_in_seconds = int(config['wait_time_in_seconds'])

config = Config()



