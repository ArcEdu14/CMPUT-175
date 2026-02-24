import random
from stack import Stack

FILES = ["config1.txt", "config2.txt", "config3.txt"]

"""
Plan:

Terminology:
cap: the maximum capacity of each stack
stacks: the number of stacks in the game
Each stack is displayed on a single line. Empty stacks are not displayed. 

Game mechanics:
1. Randomly choose a start state config file
2. Initialize stacks based on the start state
2. (Loop until complete) The user moves fruit between stacks
3. Once a stack is full with all fruit of the same type, it is completed
4. Complete all the stacks to win
"""

class Game:
    """
    A class representing the Fruit Sorter game engine
    """

    def __init__(self):
        """
        Initializes the game engine.
        Chooses a random file and creates empty stacks.
        """

        filename = FILES[random.randint(0, 2)]
        with open(filename, "r") as file:
            self.data = file.readlines()

        # strip whitespace
        for i in range(len(self.data)):
            self.data[i] = self.data[i].strip()

        # split into 2d list
        for i in range(2, len(self.data)):  # skip 1st and 2nd line
            self.data[i] = self.data[i].split()

        self.stacks = []
        self.cap = None
        self.size = None
        self.gameOver = False

        # get cap
        try:
            self.cap = int(self.data[0][-1])
        except Exception as e:
            print(f"Error: Stack initialization | capacity: {e.args}")

        # get size
        try:
            self.size = int(self.data[1][-1])
        except Exception as e:
            print(f"Error: Stack initialization | number of stacks: {e.args}")

        # initialize empty stacks
        while len(self.data - 2) < self.size:  # skip 1st and 2nd line
            self.stacks.append(Stack(self.cap))  # create empty stacks of specified cap

    def initialize_stacks(self):
        """
        Initializes empty stacks with contents from file
        :return: None
        """

        for stack in self.stacks:
            for i in range(2, len(self.data)):  # skip 1st and 2nd line
                for j in range(self.data[i]):
                    stack.push(self.data[i][j])  # push the fruit emoji

    def show_stacks(self):
        """
        Displays the stacks
        :return: None
        """

        print("Current Stacks")
        for i in range(len(self.stacks)):
            print(f"Stack {i+1}: {self.stacks[i].__str__()}")



if __name__ == "__main__":
    fruit_sorter = Game()
    fruit_sorter.show_stacks()




