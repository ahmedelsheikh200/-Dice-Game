from diceGame import *
def main():
    player_die = Die()
    computer_die = Die()
    my_player = Player (player_die,False)
    computer_player = Player(computer_die , True)
    game = DiceGame(my_player,computer_player)
    game.play()


if __name__ == "__main__":
    main()




