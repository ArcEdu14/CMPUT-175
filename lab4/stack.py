#----------------------------------------------------
# Lab 4: Fruit Sorter
# 
# Author: CMPUT 175 Team
#----------------------------------------------------

"""
Lab Description
    DONE. Stacks have a max size provided as an arguement when creating a new Stack object.

    Stacks are completed when it is filled to the max capacity with the same item.

    A stack cannot be modified when it is completed. Pushing and Popping in these instances should raise an exception.

    A stack should not exceed its max capacity, raise excpetion.

    Popping or peeking from an empty stack should raise an exception.

    Do not edit main()
"""
class Stack:
    """
    A class representing a stack Abstract Data Type (ADT).
    Modify it slightly to fit the Stack Game requirements.
    Hint:
    It needs to have a maximum capacity and can be marked as 
    completed when all items are the same and the stack is full.
    """

    def __init__(self, capacity):
        """
        Initializes an empty stack.
        """
        self.items = []
        # capacity must be positive and non-zero
        if type(capacity) != int or capacity <= 0:
            raise Exception('Capacity Error')

        self.capacity = capacity # the maximum capacity of the stack

    def push(self, item):
        """
        Adds an item to the top of the stack. (set to nth index)
        Inputs: The item to be added to the stack.
        Returns: None

        Raises:
            Exception: If the stack is full or completed
        """
        # Check completed or full
        if self.size() == self.capacity or self.is_completed():
            raise Exception('Cannot push to a locked or full stack.')

        self.items.append(item)

    def pop(self): 
        """
        Removes and returns the top item from the stack.
        Inputs: None
        Returns: The item removed from the top of the stack.

        Raises:
            Exception: If the stack is empty.
            Exception: If the stack is completed.
        """
        # check if stack is empty
        if self.is_empty():
            raise Exception('Cannot pop from an empty stack.')

        # check if stack is completed
        if self.is_completed():
            raise Exception('Cannot pop from a complete stack.')

        # return item
        return self.items.pop()

    
    def peek(self):  
        """
        Returns the top item of the stack without removing it.
        Inputs: None
        Returns: The top item of the stack.

        Raises:
            Exception: If the stack is empty.
        """

        # check if stack empty
        if self.is_empty():
            raise Exception('Cannot peek at an empty stack.')

        # return item
        return self.items[-1]
         
    
    def is_empty(self):
        """
        Checks if the stack is empty.
        Inputs: None
        Returns: bool - True if the stack is empty, False otherwise.
        """
        return self.items == []

    def is_completed(self):
        """
        Checks if the stack is completed.
        Inputs: None
        Returns: bool - True if stack is completed, False otherwise.
        """
        if self.size() > 0 and self.size() == self.items.count(self.items[0]) and self.size() == self.capacity:
            return True
        else:
            return False
    def size(self):
        """
        Returns the number of items in the stack.
        Inputs: None
        Returns: int - The number of items in the stack.
        """
        return len(self.items)
    
    def show(self):
        """
        Prints the items in the stack.
        Inputs: None
        Returns: None
        """
        print(self.items)
    
    def __str__(self):
        """
        Returns a string representation of the stack.
        Inputs: None
        Returns: str - A string representation of the stack.
        """
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        """
        Removes all items from the stack. Does nothing if the stack is empty.
        Inputs: None
        Returns: None
        """
        self.items = []



def main():
    # ----- Stack tests (formatted) -----
    print("\n=== Stack tests ===")

    # Basic usage
    print("\n-- Basic operations --")
    s = Stack(4)
    print("Initially empty:", s.is_empty())

    s.push('A')
    s.push('B')
    s.push('C')
    print("After pushing A, B, C ->")
    print("  Stack contents:", end=" ")
    s.show()
    print(f"  Size: {s.size()}")
    print(f"  Peek (top): {s.peek()}")
    popped = s.pop()
    print(f"  Popped item: {popped}")
    print("  Stack now:", end=" ")
    s.show()
    print("  Is empty?:", s.is_empty())
    print("  String repr:", str(s))

    # Additional behavioural tests
    print("\n-- Additional tests (capacity & errors) --")
    # Test completed flag when pushing identical items up to capacity
    s2 = Stack(3)
    s2.push('X')
    s2.push('X')
    s2.push('X')
    print("s2 contents:", s2.items)
    print("s2 size:", s2.size())
    print("s2 completed?:", s2.is_completed())

    # Attempting to pop from a completed stack should raise
    try:
        s2.pop()
    except Exception as e:
        print("Expected error (pop completed):", e)

    # Attempting to push to a full/completed stack should raise
    try:
        s2.push('X')
    except Exception as e:
        print("Expected error (push completed/full):", e)

    # Test pop/peek on empty stack raise
    s3 = Stack(2)
    try:
        s3.pop()
    except Exception as e:
        print("Expected error (pop empty):", e)

    try:
        s3.peek()
    except Exception as e:
        print("Expected error (peek empty):", e)

    # Test transitions: push then pop to empty
    s4 = Stack(2)
    print("s4 is_empty initially:", s4.is_empty())
    s4.push('A')
    print("s4 size after one push:", s4.size())
    popped = s4.pop()
    print("s4 popped value:", popped)
    print("s4 is_empty after pop:", s4.is_empty())

    # Test __str__ formatting for multiple items
    s5 = Stack(4)
    s5.push('p')
    s5.push('q')
    print("s5 string repr:", str(s5))

if __name__ == "__main__":
    main()