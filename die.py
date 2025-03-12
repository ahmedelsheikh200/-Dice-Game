import random

class Die:
    def __init__(self):
        self.__value =None

    @property
    def value(self):
        return self.__value
    
    # @value.setter
    # def value(self):

    def roll(self):
        new_value = random.randint(1,6)
        self.__value = new_value
        return new_value


# testing the class
# die = Die ()
# print(die.value)
# print (die.roll())




    