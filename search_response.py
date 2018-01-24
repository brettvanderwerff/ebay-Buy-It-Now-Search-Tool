'''
The search_response module contains the class 'SearchResponse'.
The SearchResponse class is intended for use with the Finding class of the ebaySDK module
 and has methods that parse responses from the Finding class when it is being used to search ebay by UPC.
'''


class SearchResponse:
    def __init__(self, response_dictionary):
        self.response_dictionary = response_dictionary

    def get_listings(self, listing_number):
        '''The get_listings method searches the ebaySDK Finding class response and returns a list of the cheapest products
         containing a'buyitnow' option. This function handles a some exceptions for commonly missing data in the
         Finding class response.
         '''
        items_description = []
        for listing_number in range(listing_number):
            try:
                item = self.response_dictionary['searchResult']['item'][listing_number]
                title = item['title']
                url = item['viewItemURL']
                try:
                    shipping_price = item['shippingInfo']['shippingServiceCost']['value']
                    shipping_price_currency = item['shippingInfo']['shippingServiceCost']['_currencyId']
                except KeyError:
                    shipping_price = 'Sorry no shipping price found, please follow link for complete shipping ' \
                                     'information.'
                    shipping_price_currency = ''
                if item['listingInfo']['listingType'] == 'FixedPrice' or item['listingInfo'][
                    'listingType'] == 'StoreInventory':
                    item_price = item['sellingStatus']['currentPrice']['value']
                    item_price_currency = item['sellingStatus']['currentPrice']['_currencyId']
                elif item['listingInfo']['listingType'] == 'AuctionWithBIN':
                    item_price = item['listingInfo']['buyItNowPrice']['value']
                    item_price_currency = item['listingInfo']['buyItNowPrice']['_currencyId']
                item_description = {}
                item_description['title: '] = title
                item_description['item_price: '] = item_price
                item_description['item_price_currency: '] = item_price_currency
                item_description['shipping_price: '] = shipping_price
                item_description['shipping_price_currency: '] = shipping_price_currency
                item_description['url: '] = url
                items_description.append(item_description)
            except IndexError:
                print('Sorry the request exceeds the 100 listing limit, only the 100 cheapest listings will be shown.')
        return items_description

    def prettify_listings_list(self, listing_number=5):
        '''The prettify_listings_list method transforms the output of the get_listings_list method to a format that
         is amenable to email. This method accepts listing_number as an argument, which dictates the number of responses
         returned in the listing list. By default listing_number is set to 5.
         '''
        cheapest_listings_list = self.get_listings(listing_number)
        if listing_number == 1:
            string = 'Here is the cheapest listing we found on ebay: \n\n\n'
        elif listing_number <= 100:
            string = 'Here are the top {} cheapest listings we found on ebay: \n\n\n'.format(listing_number)
        else:
            string = 'Here are the 100 cheapest listing we found on ebay: \n\n\n'
        for item in cheapest_listings_list:
            for k, v in item.items():
                string = (string + k + v + '\n')
            string = (string + '\n\n\n')
        return string.replace(u'\xa0',
                              u' ')
