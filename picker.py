import random
import argparse

FOOD = {
    'korean': ['Woorijib', 'B WON', 'San Maru', 'Goodfella', 'Majista Grill'],
    'chinese': ['Nanjing', 'Mandarin Wok', 'Chinatown Buffet', 'Lao 4 chuan', 'Golden Harbor'],
    'thai': ['My Thai', 'Thara Thai', 'Basil Thai'],
    'bbq': ['hickory river', 'blackdog', "Bobo's bbq", 'Wood n Hog'],
    'other': ['cook']
}

# not sure if 2x or 3x is actually right, but whatever
FAVORED = ['korean', 'chinese', 'thai'] # 2x more likely than not favored
MOST_FAVORED = ['korean', 'chinese'] # 3x more likely 

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, default='all', help='{0} and all'.format([*FOOD]))
args = parser.parse_args()

foodType = args.type
foodList = []

if foodType == 'all':
    for ethnicity in FOOD:
        foodList.extend(FOOD[ethnicity])

        if ethnicity in FAVORED:
            foodList.extend(FOOD[ethnicity])

            if ethnicity in MOST_FAVORED:
                foodList.extend(FOOD[ethnicity])
else:
    foodList = FOOD[foodType]

print(foodList[random.randint(0, len(foodList) - 1)])
