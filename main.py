# Samantha Deshazer
# CS454
# Assignment One - Pokemon Card Scapper.
# This assignment is used for finding pokemon card information and most recent selling prices
# based on the card set chosen - ie first edition base set, jungle, celebrations.
import urllib.request
from bs4 import BeautifulSoup
import csv

Series = 'swsh08-fusion-strike'
html_doc = ['https://shop.tcgplayer.com/price-guide/pokemon/'+Series]
data = []
csv_path = 'index.csv'


def scaper_test():
    for pg in html_doc:
        page = urllib.request.urlopen(pg)
        soup = BeautifulSoup(page, 'html.parser')
        attr = soup.find('table', class_="priceGuideTable tablesorter")
        get_Cards(attr)


def get_Cards(collection):
    with open(csv_path, 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Pokemon Card Collection Data :", Series])
        writer.writerow(["Name", "Rarity", "Price"])
        card_collection_odd = collection.findAll('tr', class_="odd")
        card_collection_even = collection.findAll('tr', class_="even")
        card_collection = card_collection_even + card_collection_odd
        for card in card_collection:
            card_name = card.find('div', class_="productDetail")
            card_rarity = card.find('td', class_="rarity")
            card_price = card.find('td', class_="marketPrice")
            print(card_name.text.strip())
            print(card_price.text.strip())
            write_data(writer, card_name.text.strip(), card_rarity.text.strip(), card_price.text.strip())
        print("total entries:")
        print(len(card_collection))

def write_data(writer, card_name, card_rarity, card_price):
    fields = ('Card Name', 'Rarity', 'Market Price')
    writer.writerow([card_name, card_rarity, card_price])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scaper_test()
#   parse_Cards(data)
# write_data()
# print(data)
