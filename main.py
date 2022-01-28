# Samantha Deshazer
# CS454
# Assignment One - Pokemon Card Scapper.
# This assignment is used for finding pokemon card information and most recent selling prices
# based on the card set chosen - ie first edition base set, jungle, celebrations.
import urllib.request
from bs4 import BeautifulSoup
import csv

data = []
csv_path_all_cards = 'index.csv'
csv_path_expensive_cards = 'pkcardsExpensive.csv'
csv_path_rare_cards = 'pkcardsExpensive.csv'

COLLECTION_SIZE = 13


def get_next_series(series_number):
    series = {
        0: 'swsh08-fusion-strike',
        1: 'celebrations',
        2: 'celebrations-classic-collection',
        3: 'swsh07-evolving-skies',
        4: 'swsh06-chilling-reign',
        5: 'swsh05-battle-styles',
        6: 'first-partner-pack',
        7: 'shining-fates',
        8: 'shining-fates-shiny-vault',
        9: 'swsh04-vivid-voltage',
        10: 'swsh01-sword-and-shield-base-set',
        11: 'skyridge',
        12: 'sandstorm',
        13: 'ruby-and-sapphire'
    }
    return series.get(series_number, 'default series value error')


def grab_series(source, series_number):
    series = get_next_series(series_number)
    print(series)
    source = 'https://shop.tcgplayer.com/price-guide/pokemon/' + series
    return source


def scape_all_series_of_interest(source, series_number):
    csv_path = csv_path_all_cards
    scape_cards(source, series_number, csv_path)
    series_number = 0


def scape_cards(source, series_number, csv_path):
    with open(csv_path, 'w', newline="") as csv_file:
        source = grab_series(source, series_number)
        series = get_next_series(series_number)
        while series_number < COLLECTION_SIZE:
            page = urllib.request.urlopen(source)
            soup = BeautifulSoup(page, 'html.parser')
            attr = soup.find('table', class_="priceGuideTable tablesorter")
            print(source)
            get_Cards(attr, series, csv_file, )
            series_number = series_number + 1
            series = get_next_series(series_number)
            source = grab_series(source, series_number)
        print(source)


def get_Cards(collection, series, csv_file):
    writer = csv.writer(csv_file)
    writer.writerow(["Pokemon Card Collection Data :", series, "source:", source])
    writer.writerow(["Name****", "Rarity*****", "Price****", "Image****"])
    card_collection_odd = collection.findAll('tr', class_="odd")
    card_collection_even = collection.findAll('tr', class_="even")
    card_collection = card_collection_even + card_collection_odd
    for card in card_collection:
        card_name = card.find('div', class_="productDetail")
        card_rarity = card.find('td', class_="rarity")
        card_price = card.find('td', class_="marketPrice")
        card_image = card.find('img')
        card_price_text = card_price.text.strip()
        write_data(writer, card_name.text.strip(), card_rarity.text.strip(), card_price.text.strip(), card_image.get('src'))


def write_data(writer, card_name, card_rarity, card_price, card_image):
    fields = ('Card Name', 'Rarity', 'Market Price')
    writer.writerow([card_name, card_rarity, card_price, card_image])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    source = 'https://shop.tcgplayer.com/price-guide/pokemon/'  # base source to parse
    series_number = 0  # begin with the first set or series of interest.
    scape_all_series_of_interest(source, series_number)
