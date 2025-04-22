"""
File with useful debugging functions
Allows ro get an overview on the project
Uncomment function lines to use (lazy me)
"""

from menu import get_availible_games



def print_game_status(game_name:str = False):
    """
        prints all game status if no parameter is passed
        :param game: game name. If passed it print only the particular file's status.
    """
    for game in games.values():
        if not game_name:
            print(f"{game}: hey")
        elif game == game_name:
            print(f"{game}: holla")




def print_game_list():
    for index,item in games.items():
        print(f"{index}: {item}")



if __name__ == "__main__":
    games = get_availible_games()
    print("_________________hello world!______________")
    print_game_status("snake_game")
    print("____________________________")
    print_game_list()
