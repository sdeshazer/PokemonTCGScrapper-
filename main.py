# Samantha Deshazer
# CS454
# Assignment One - Pokemon Card Scapper.
# This assignment is used for finding pokemon card information and most recent selling prices
# based on the card set chosen - ie first edition base set, jungle, celebrations.
import urllib.request
from bs4 import BeautifulSoup
import csv

html_doc = 'https://shop.tcgplayer.com/price-guide/pokemon/base-set'
page = urllib.request.urlopen(html_doc)
soup = BeautifulSoup(page, 'html.parser')
attr = soup.find('div', attrs={'class': 'productDetail'})
name_of_card = attr.text

def scaper_test():
    print('price : ' + name_of_card)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scaper_test()
