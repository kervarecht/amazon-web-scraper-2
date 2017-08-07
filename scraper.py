
import requests
from bs4 import BeautifulSoup
import re
import json
import sys

amazon = []


"""The code below successfully extends the passed-in first-page link and extracts:
title, author, and price, the link for each book, as well as the ISBN
It saves deals 1-100 for overall bestsellers so far to deal_response.  If there are any parsing or ISBN/link issues, it
returns the information as best it can and continues iterating.
"""

def amazon_deals(url):
    deal_response = []
    addons = ['ref=zg_bs_pg_2?_encoding=UTF8&pg=2&ajax=1',
              'ref=zg_bs_pg_3?_encoding=UTF8&pg=3&ajax=1',
              'ref=zg_bs_pg_4?_encoding=UTF8&pg=4&ajax=1',
              'ref=zg_bs_pg_5?_encoding=UTF8&pg=5&ajax=1']
    url_list = []
    url_list.append(url)
    for addon in addons:
        url_list.append(url + addon)
    for url in url_list:
        amazon_results = requests.get(url)

        parsed_amazon_results = BeautifulSoup(amazon_results.text, "lxml")

        results_content = parsed_amazon_results.body.find_all('div', attrs={'class', 'zg_itemWrapper'})

        link_content = []
        
        deals = []

        for each in results_content:
            title = each.find('div', attrs={'class', 'p13n-sc-truncate'}).text
            link = each.find('a', attrs={'class', 'a-link-normal'})['href']
            asin = str(re.search('dp/(.+?)\?_encoding', link).group(1))
            details_fodder = list(each.stripped_strings)
            price_var = details_fodder[len(details_fodder) - 1]
            if price_var[0] == "R":
                price_var = details_fodder[len(details_fodder) - 2]
            book_object = {
                'title': details_fodder[0],
                'author': details_fodder[1],
                'price': price_var,
                'asin' : asin
            }
            deals.append(book_object)

        deal_response.append(deals)
        if len(deal_response) == len(url_list):
            return(deal_response)

# leave amazon as the variable in this function as it is the processed
# batch list for the value originally passed in to target
# amazon_deals(amazon)
