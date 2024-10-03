
# from random import choice



# coin = choice(['khat', 'shir'])
# print(coin)












# from random import randint


# a_random_number = randint(0,100)
# print(a_random_number)

# from random import shuffle

# cards = ['tak pik', '2lo del', '10 gishniz']
# print(cards)
# shuffle(cards)


# for card in cards:
#     print(card)


# from statistics import mean


# grades = [10, 20, 20 , 20]
# mean_grades = mean(grades)
# print(mean_grades)


# import sys

# print(f'hello {sys.argv}')

# my_list = [1 , 2, 3 ,4]
# print(my_list[:2])


# for name in sys.argv[1:]:
#     print(f'hello {name}')
# try:
#     name = sys.argv[10]
#     print(name)
# except IndexError:
#     print('error out of range')


# import cowsay

# cowsay.dragon('hello asdfasdf')
# cowsay.cow('helloe')


# import requests
# import json 
# response = requests.get('https://itunes.apple.com/search?entity=song&limit=10&term=weezer').json()
# # response = json.dumps(response, indent=2)



# for song in response['results']:
#     print(song['trackName'])

# from libery import hello
import libery
libery.hello('amirali')