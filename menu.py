"""
selection of the game to play

___Browsing availible games___
looks for all the files in the dir.
    if Folder name end with game (it is a game folder)

___starting game___
inside the Folder it looks for a file that ends with "start.py"
and executes it
"""

import os
import subprocess

def menu():
    print("select your minigame:")
    print_game_list()
    chose = get_int(0, len(games)-1)
    print(games[chose])
    if chose != 0:
        running_game(chose)


def get_availible_games():
    game_files = dict()
    i = 1
    for item in os.listdir():
        if item[-4:] == "game":
            game_files[i] = item
            #print(item)
            i += 1
    return game_files


def get_int(min, max) -> int:
    while True:
       try:
            chose = int(input("-> "))
            if min <= chose <= max:
                return chose
            else:
                print(f"please input a number between {min} and {max}")
       except :
            print("Please enter a valid integer")

def print_game_list():
    for index,item in games.items():
        print(f"{index}: {item}")

def running_game(chose):
    # os.listdir(games[chose])
    directory = 'path/to/your/folder'
    for filename in os.listdir(games[chose]):
        if filename.endswith('start.py'):
            filepath = os.path.join(directory, filename)
            subprocess.run(['python', filepath], check=True)
    # os.chdir(new_directory) cahnge dir


if __name__ == "__main__":
    games = get_availible_games()
    menu()