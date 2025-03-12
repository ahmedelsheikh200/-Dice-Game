from die import *  


class Player :
    def __init__(self , die , is_computer = False):
        self.__die = die
        self.__is_computer = is_computer
        self.__counter = 5

    @property
    def die (self):
        return self.__die
    @property
    def is_computer(self):
        return self.__is_computer
    @property
    def counter (self):
        return self.__counter
    
    def increment_counter (self):
        self.__counter += 1

    def decrement_counter (self):
        self.__counter -= 1
    
    def roll_die (self):
        return self.__die.roll()

        



#die = Die()
#player = Player(die)
# print(player.die.roll())
# print (player.roll_die())
# print (player.die)

