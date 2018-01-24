'''The get UPC module contains the get_UPC function, which gets input from the user in the form of a
UPC. '''


def get_UPC():
    '''Gets a UPC from the user, which will be used to guide the product search.
    '''
    while True:
        user_UPC = input(
            'Please enter the UPC of the product you would like to search for and press \'enter\' when finished! \n'
            'Note that many resources for searching UPC\'s exist such as http://upcdatabase.org/search and note that \n'
            'multiple UPCs may pertain to your product of interest.')
        if not (user_UPC).isdigit():
            print('I\'m sorry we only take numeric input here.')
        if len(user_UPC) != 12:
            print('I\'m sorry UPCs have a length of 12 numbers, please look at your input again.')
        else:
            return user_UPC
