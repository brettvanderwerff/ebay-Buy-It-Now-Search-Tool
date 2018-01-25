# ebay-Buy-It-Now-Search-Tool
A program that uses the ebaySDK module (https://github.com/timotheus/ebaysdk-python) to obtain the cheapest US domestic "Buy it now" listings for items with a given UPC. This works particularly well for monitoring the daily fixed price listings of newly released media items, such as video games, which have expensive prices upon release but drop in price shortly after release. The program is coded to email the listing results to the user once per day (by default).

~~~~~~~~~~~~~~~
Example:
~~~~~~~~~~~~~~~

Input: 883929391462 

Output:https://imgur.com/a/KuarK (taken from my email inbox)

~~~~~~~~~~~~~
Dependencies:
~~~~~~~~~~~~~

ebaysdk==2.1.5

~~~~~~~~~~~~~~~~~~~~~~~~
How to run this program:
~~~~~~~~~~~~~~~~~~~~~~~~

1.	Download repo
2.  Install the dependencies
3.	Configure the program (see below)
4.	Run ebay_buy_it_now_search_tool.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
How to configure this program:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most configuration options are available in the config file.

An ebay App ID production API key is needed, which can be gotten easily from signing up at: https://go.developer.ebay.com/

A Gmail account with an email and password is needed to send email from. The google account settings must be modified to allow sending email via less secure apps, which at the time of writing this was:

https://myaccount.google.com/  - Apps with account access  - Allow less secure apps  - ON

(See https://www.youtube.com/watch?v=mP_Ln-Z9-XY&t=5s for more details.)

A receiving email address will also be needed, but many users will just receive messages at the same address that they are using to send email from.

Users can modify the number of listings they receive by changing the listing_number argument of the prettify_listings_list() method of the SearchResponse class. The default is to send results of the five cheapest listings.

The time delay between API calls to ebay/results emails to user can be changed my modifying the seconds_in_a_day variable in the config.py file

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Additional comments and future directions:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since this program is intended to run continuously and call ebay’s API once per day (or whatever the user sets it to), it seems like it would be a great use for a raspberry pi. I have not tried this yet, but I plan to in the future.

I would like to extend this program to have it check ebay every hour or so and send messages to the user of buy it now listings that are below a user defined price. This is similar to how limit buy orders work on the stock market, but in this case the user would just get the listing as a message when they are below a certain price and decide whether to buy at that time or not.  





