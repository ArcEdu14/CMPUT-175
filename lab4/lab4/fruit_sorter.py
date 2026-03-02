import random
from stack import Stack

"""
Title: Lab 4
Author: Alice Cai
Date: 2026-02-24
"""

FILES = ["lab4/config1.txt", "lab4/config2.txt", "lab4/config3.txt"]

"""
Project Description:
A game engine that uses the Stack class to organize fruit. 

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

        filename = FILES[random.randint(0, 2)]  # get random file
        with open(filename, "r", encoding="utf-8") as file:  # open file with encoding
            self.data = file.readlines()

        # strip whitespace
        for i in range(len(self.data)):
            self.data[i] = self.data[i].strip()

        # split into 2d list
        for i in range(2, len(self.data)):  # skip 1st and 2nd line
            self.data[i] = list(self.data[i])

        # initialize attributes
        self.stacks = []
        self.cap = None
        self.size = None
        self.gameOver = False
        self.winning_condition = []

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

        # get unique fruits
        unique_fruits = []
        for i in range(2, len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] not in unique_fruits:
                    unique_fruits.append(self.data[i][j])

        # which fruits are needed to win? put these in a winning_condition list
        for i in range(len(unique_fruits)):
            count = 0
            for j in range(2, len(self.data)):
                count += self.data[j].count(unique_fruits[i])
            if count >= self.cap:
                self.winning_condition.append(unique_fruits[i])

        # initialize empty stacks
        while len(self.stacks) < self.size:
            self.stacks.append(Stack(self.cap))  # create empty stacks of specified cap

    def initialize_stacks(self):
        """
        Initializes empty stacks with contents from file
        :return: None
        """
        for i in range(2, len(self.data)):  # skip the first two lines
            for j in range(len(self.data[i])):
                self.stacks[i-2].push(self.data[i][j])  # push the fruit emoji

    def get_stack_a(self):
        """
        Gets stack_a, the index of the stack being moved from, and does checks.
        :return: stack_a
        """
        # get choice of stack to move from
        stack_a = input(f"Select a stack to move from (1-{self.size}): ")
        try:
            stack_a = int(stack_a)
            if stack_a > 0 and stack_a <= self.size:  # valid choice
                return stack_a
            else:
                print('Invalid stack number. Please try again.')
                return self.get_stack_a()  # ask again
        except Exception:  # non integer input
            raise Exception("Please enter valid integers for stack numbers.")

    def get_stack_b(self):
        """
        Gets stack_b, the index of the stack being moved to, and does checks.
        :return: stack_b
        """
        # get choice of stack to move to
        stack_b = input(f"Select a stack to move to (1-{self.size}): ")
        try:
            stack_b = int(stack_b)
            if stack_b > 0 and stack_b <= self.size:  # valid choice
                return stack_b
            else:
                print('Invalid stack number. Please try again.')
                return self.get_stack_b()  # ask again
        except Exception:
            raise Exception("Please enter valid integers for stack numbers.")  # non integer input


    def move_item(self, stack_a, stack_b):
        """
        Moves the item from stack a to stack b
        :return: None
        """

        # move the item from stack a --> stack b
        # if the stack popping from is empty
        try:
            item = self.stacks[stack_a-1].pop()
        except Exception:
            raise

        # if the stack pushing to is full
        try:
            self.stacks[stack_b - 1].push(item)
        except Exception:
            self.stacks[stack_a - 1].push(item)  # put the popped item back
            raise

    def show_stacks(self):
        """
        Displays the stacks in a menu
        :return: None
        """

        print("Current Stacks")
        for i in range(len(self.stacks)):
            print(f"Stack {i+1}: {self.stacks[i].__str__()}")

    def check_game_over(self):
        """
        Checks if the game is over
        Condition: If there are at least {max capacity} instance of a fruit, a stack is completed when it is filled to its max capacity using that unique fruit
        :return: None
        """
        # Check if there are at least {max capacity} instance of a fruit

        completed = []   # list for completed fruits
        for stack in self.stacks:
            if stack.is_completed() and stack.peek() in self.winning_condition:
                completed.append(stack.peek())

        self.gameOver = True
        for i in range(len(self.winning_condition)):
            if not self.winning_condition[i] in completed:  # to win need all fruits in winning_condition to also be in completed
                self.gameOver = False

    def engine(self):
        """
        Runs the main game loop
        :return: None
        """

        # Welcome message
        print("Welcome to the Fruit Sorter!", end = "\n\n")

        # Initialize stacks
        self.initialize_stacks()

        # Core game loop
        while not self.gameOver:
            self.show_stacks()  # show the game board
            # get the player inputs for moving a fruit
            try:
                stack_a = self.get_stack_a()
                stack_b = self.get_stack_b()
                self.move_item(stack_a, stack_b)
            # attend to any raised exceptions
            except Exception as e:
                print(e.args[0])
            print("")

            # check game over
            # all completed if there are at least {max capacity} instance of a fruit, a stack is completed when it is filled to its max capacity using that unique fruit
            self.check_game_over()

        # show final winning board and display message
        self.show_stacks()
        print("Congratulations! You've won the game!")

def main():
    """
    Runs the program
    """
    fruit_sorter = Game()  # create game class
    fruit_sorter.engine()  # run game

if __name__ == "__main__":
    main()



