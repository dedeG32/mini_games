import tictactoe2
def menu():
    print("select your minigame:")
    print("1. tic-tac-toe")
    print("2. ")
    print("3. x")
    chose = get_int(1,3)

    match chose:
        case 1:
            tictactoe2.Tic_tac_toe2().start()

        case 2:
            pass
           #from os.path("C:\Users\dedeb\PycharmProjects\project learning\console_chess\main.py") import(__file__):
        case 3:
            pass

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


if __name__ == "__main__":
    menu()