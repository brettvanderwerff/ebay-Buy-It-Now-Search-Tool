'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ebay Buy It Now Search Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This program uses the ebaySDK module to search ebay for the cheapest 'buy it now'
listings of products with a user defined UPC.The program is coded to run once every 24 hours
and sends an email to the user with the results.
'''

from config import api_key, wait_time
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from get_UPC import get_UPC
from send_email import send_email
from search_response import SearchResponse
from time import sleep


def run():
    user_UPC = get_UPC()
    while True:
        try:

            '''
            input_dictionary contains all the parameters that will be passed to the execute method
             of the Finding class to search ebay via UPC.
             productID defines the search for UPCs. 
             paginationInput defines the search response size. 
             ListingType restricts the search to listing types that are associated with 'buy it now' options. 
             LocatedIn restricts the search the the US.
             sortOrder is set to return the the listings in order from cheapest to more expensive.
             '''
            input_dictionary = {'productId': {'#text': user_UPC, '@attrs': {'type': 'UPC'}},
                                'paginationInput': {'entriesPerPage': 100, 'pageNumber': 1}, 'itemFilter': [
                    {'name': 'ListingType', 'value': ['FixedPrice', 'StoreInventory', 'AuctionWithBIN']},
                    {'name': 'LocatedIn', 'value': 'US'}],
                                'sortOrder': 'PricePlusShippingLowest'}
            api = Finding(appid=api_key, config_file=None)
            response = api.execute('findItemsByProduct', input_dictionary)
            response_dictionary = response.dict()
            response_search = SearchResponse(response_dictionary)
            subject = 'Your daily search results for: {}.'.format(user_UPC)
            try:
                msg = response_search.prettify_listings_list()
            except KeyError:
                print('Sorry no results were found for that UPC, please try a different one.')
                continue
            send_email(subject=subject, msg=msg)
            print('Sleeping for 24 hours. Press \'ctrl + c\' at anytime to exit.')
            '''KeyboardInterrupt exception facilitates the ability to exit the program at anytime when the program is
            run from the terminal.'''
            try:
                sleep(wait_time)
            except KeyboardInterrupt:
                exit()

        except ConnectionError as e:
            print(e)
            print(e.response.dict())
            print('Something went wrong, please try again later.')
            exit()

if __name__ == '__main__':
    run()
