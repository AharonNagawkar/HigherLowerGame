import art
from game_data import data
from os import system
from random import randint


index_pool = []


def pull_random_index():
    index = randint(0, len(data)-1)
    while index in index_pool:
        index = randint(0, len(data)-1)
    index_pool.append(index)
    return index


def stats(index):
    return data[index]['name'], data[index]['description'], data[index]['country']


def higher(index_a, index_b):
    if data[index_a]['follower_count'] > data[index_b]['follower_count']:
        return 'A'
    return 'B'


def play():
    win = True
    score = 0
    index_a = pull_random_index()
    while len(index_pool) < 50 and win:
        index_b = pull_random_index()
        system('clear')
        print(art.logo)

        # hint for me, delete later
        # print(data[index_a]['follower_count'])
        # print(data[index_b]['follower_count'])

        print(f"Compare A: {stats(index_a)[0]}, a {stats(index_a)[1]} from {stats(index_a)[2]}.")
        print(art.vs)
        print(f"Against B: {stats(index_b)[0]}, a {stats(index_b)[1]} from {stats(index_b)[2]}.")
        player_choice = input("Who has more followers? Type 'A' or 'B':").upper()
        answer = higher(index_a, index_b)

        if player_choice == answer and player_choice in ['A', 'B']:
            score += 1
            if answer == 'B':
                index_a = index_b
        else:
            system('clear')
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            win = False

        if score == 49:
            system('clear')
            print(art.logo)
            print(f"You won the game with Max {score} points.")


play()
