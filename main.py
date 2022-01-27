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
        data = get_Cards(attr)


def get_Cards(collection):
    card_collection =  collection.findAll('td', class_="product")
    for card in card_collection:
        card_name = card.find('div', class_="productDetail")
        print(card.text.strip())
    print("total:")
    print(len(card_collection))
   # print(card_collection)
    return card_collection
    #price_of_card =  collection_cards_odd.find('td', attrs={'class': 'marketPrice'})
    #data.append((name_of_card, price_of_card.text.strip()))

def parse_Cards(data):
   # card_names = data.find_all('div', class_="productDetail")
    card_prices = data.find_all('td', class_="marketPrice")
  #  print(card_names)
    print(card_prices)


def write_data():
    with open(csv_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        print(len(data))
        for name_of_card, price in data:
            print(name_of_card)
            print(price)
            writer.writerow([name_of_card, price])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scaper_test()
 #   parse_Cards(data)
   # write_data()
   #print(data)
