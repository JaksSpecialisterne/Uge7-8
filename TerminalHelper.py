import os

#A collection of small general methods that helps doing terminal related stuff.
class TerminalHelper:
    #Take a min and max number, and keep running until a number between the given min and max is given
    #Returns an int between the given min and max, including both
    def NumberInput(minNum: int, maxNum: int) -> int:
        while True:
            num = input("\nPlease enter a number ")
            try:
                val = int(num)
                if val <= maxNum and val >= minNum:
                    return val
                else:
                    print("Not a valid number...")
            except ValueError:
                print("Not a number...")

    #Takes a seachterm, that gives the user some more info on what they currently doing
    #Returns an inputted number
    def IntInput(searchT):
        while True:
            num = input(f"\nPlease enter {searchT}, it must be a number: ")
            try:
                val = int(num)
                return val
            except ValueError:
                print("Not a number...")

    #Takes a seachterm, that gives the user some more info on what they currently doing
    #Returns a string
    def StringInput(searchT):
        return input(f"\nPlease enter {searchT}: ")
            
    #A method that stalls the current terminal window, waiting for any kind of input, after which it clears the terminal
    def KeyToContinue():
        print("\nPress a key to continue...")
        input()
        os.system('cls')