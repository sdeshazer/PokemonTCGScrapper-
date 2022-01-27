# Samantha Deshazer
# CS454
# Assignment One - Pokemon Card Scapper.
# This assignment is used for finding pokemon card information and most recent selling prices
# based on the card set chosen - ie first edition base set, jungle, celebrations.
import urllib.request
from bs4 import BeautifulSoup
import csv

html_doc = ['https://shop.tcgplayer.com/price-guide/pokemon/base-set']
data = []
csv_path = 'index.csv'


def scaper_test():
    for pg in html_doc:
        page = urllib.request.urlopen(pg)
        soup = BeautifulSoup(page, 'html.parser')
        attr = soup.find('table', class_="priceGuideTable tablesorter")
        get_Cards(attr)


def get_Cards(collection):
    with open(csv_path, 'w') as csv_file:
        card_collection_odd = collection.findAll('tr', class_="odd")
        card_collection_even = collection.findAll('tr', class_="even")
        card_collection = card_collection_even + card_collection_odd
        for card in card_collection:
            card_name = card.find('div', class_="productDetail")
            card_price = card.find('td', class_="marketPrice")
            print(card_name.text.strip())
            print(card_price.text.strip())
            write_data(csv_file, card_name.text.strip(), card_price.text.strip())
        print("total:")
        print(len(card_collection))


    # data.append((name_of_card, price_of_card.text.strip()))


def write_data(csv_file, card_name, card_price):
    writer = csv.writer(csv_file)
    writer.writerow([card_name, card_price])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scaper_test()
#   parse_Cards(data)
# write_data()
# print(data)
