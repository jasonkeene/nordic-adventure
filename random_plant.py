#!/usr/bin/env python

from itertools import chain
from random import SystemRandom
import sys


PLANTS = {
    'Stinging Nettle': 3,
    'Sorrel': 3,
    'Common Wood Sorrel': 3,
    'Angelica': 3,
    'Birch': 3,
    'Wild Onion': 3,
    'Yarrow': 2,
    'Common Bugloss': 2,
    'Mugwort': 2,
    'Heather': 2,
    'Citrus': 2,
    'Eyebright': 2,
    'European Beech': 2,
    'Fennel': 2,
    'Wild Strawberry': 2,
    'Wood Avens': 2,
    'Hyssop': 2,
    'Iris': 2,
    'Common Juniper': 2,
    'Wild Rosemary': 2,
    'Lavender': 2,
    'Marjoram': 2,
    'Lemon Balm': 2,
    'Spearmint': 2,
    'Wild Marjoram': 2,
    'Norway Spruce': 2,
    'Aniseed': 2,
    'Silverweed': 2,
    'Wild Cherry': 2,
    'Blackthorn': 2,
    'Oak': 2,
    'Rosemary': 2,
    'Blackberry': 2,
    'Raspberry': 2,
    'Sage': 2,
    'Elder': 2,
    'Clove': 2,
    'Wild thyme': 2,
    'Bilberry': 2,
    'Ground Elder': 1,
    'Garlic Mustard': 1,
    'Wild Garlic/Ramson': 1,
    'Cow Parsley': 1,
    'Grassleaf Orache': 1,
    'Sea Aster': 1,
    'Field Mustard': 1,
    'Eurpoean Searocket': 1,
    'Shepherd\'s Purse': 1,
    'Caraway': 1,
    'Goosefoot': 1,
    'Chicory': 1,
    'Sea Kale': 1,
    'Wild Carrot': 1,
    'Meadowsweet': 1,
    'Ash': 1,
    'Woodruff': 1,
    'Sea Buckthorn': 1,
    'Juniper': 1,
    'Mallow': 1,
    'White horehound': 1,
    'Pineappleweed': 1,
    'Melilot/Sweet Clover': 1,
    'Spingel': 1,
    'Sweet cicely': 1,
    'Watercress': 1,
    'Nightlight/Evening Primrose': 1,
    'Plantain': 1,
    'Ribwort Plantain': 1,
    'Sea Plantain': 1,
    'Roseroot': 1,
    'Ramanas rose': 1,
    'Sheep Sorrel': 1,
    'Hedge Mustard': 1,
    'Wild Parsnip': 1,
    'European Rowan': 1,
    'Swedish Whitebeam': 1,
    'Chickweed': 1,
    'Sweet Pea': 1,
    'Tansy': 1,
    'Common Dandelion': 1,
    'Pennycress': 1,
    'Wild Thym': 1,
    'Red Clover': 1,
    'White Clover': 1,
    'Sea Arrowgrass': 1,
    'Small Nettle': 1,
    'Blueberr': 1,
    'Tufted Vetch/Cow Vetch': 1,
    'Common Violet': 1,
}


def main(count):
    random = SystemRandom()
    weighted_plants = list(chain(*[[p] * w for p, w in PLANTS.items()]))
    for _ in range(count):
        print random.choice(weighted_plants)


if __name__ == '__main__':
    try:
        count = int(sys.argv[1])
    except (ValueError, IndexError):
        count = 1
    main(count)
