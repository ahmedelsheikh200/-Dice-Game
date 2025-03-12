from player import *
class DiceGame :
    def __init__(self , player , computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("================================")
        print("🎲🎲Welcome to  the Dice Game!")
        print("================================")
        while True:
            self.play_round()
            if self._player.counter ==0 or self._computer.counter ==0:
                break
        self.check_winner()



    def play_round(self):
        #welcome
        print('----- New Round ----- ')
        input ('🎲🎲 Press any key to roll the dice 🎲🎲')
        
        #roll dice 
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()


        # show results :
        print(f'\nYour die : {player_value}')
        print(f'\ncomputer die : {computer_value}')

        #determine winner and loser
        if player_value > computer_value :
            print ('\nYou win the round!🌺')
            self._player.decrement_counter() #winner
            self._computer.increment_counter() #loser
        elif computer_value > player_value :
            print ('\nSorry! computer win this round💀')
            self._computer.decrement_counter()
            self._player.increment_counter()
        else:
            print("It is a tie😎")
        print (f'\nYour counter :{self._player.counter}')
        print(f'\nComputer counter: {self._computer.counter}')

 
    def check_winner (self):
        print ("\n=======================")
        print ("GAME OVER ✅")
        if self._player.counter ==0 :
            print ("\nYou are the WINNER 🎈🏅")
        else :
            print ("\nComputer is the WINNER ❗❗")
        print("\n=======================")

    
        



