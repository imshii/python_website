import requests
from bs4 import BeautifulSoup
import string
import os
from random import sample


def scraper(variable):
    #checks for an empty input
    if variable == '':
        return 'You have to specify your stock'
    # random string
    yikes = string.ascii_letters
    stringify = ''.join(sample(yikes, 4))
    my_savior = f'website_cache{stringify}.html'

    # gets the website data
    stock_data = requests.get(
        #f'https://www.marketwatch.com/investing/stock/AMD/historical?siteid=mktw&date=&x=0&y=0').text
        f'https://www.marketwatch.com/investing/stock/{variable}/historical?siteid=mktw&date=&x=0&y=0').text

    # saves into a file
    file = open(my_savior, 'a')
    file.write(stock_data)

    with open(my_savior) as html_file:
        soup = BeautifulSoup(html_file, 'lxml')

    # finds price per share
    try:
        price = soup.find('p', class_='data bgLast').text
    except Exception:
        os.remove(my_savior)
        return f'{variable.upper()} is not a stock... Please input a real one.'

    # finds extras
    try:
        # name = soup.find('span', class_="label").text
        close_priced = soup.find('p', class_='lastcolumn data bgLast price').text
        highest_price = soup.find('p', class_='data lastcolumn').text
        lowest_price = soup.find('p', class_='column data').text
    except Exception:
        os.remove(my_savior)
        return 'Something went wrong, try again.'

    os.remove(my_savior)
    price_submit =  f'The price per share of {variable.upper()} = ${price}.'
    low_high = f'It had a low of {lowest_price}, with a high of {highest_price} today.'
    close_time = f' and the close time is {close_priced.replace("$ ", "")}'

    return price_submit, low_high, close_time


# https://raw.githubusercontent.com/imshii/stock_data/main/stock%20data.txt
