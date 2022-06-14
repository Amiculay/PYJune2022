class SLNode: # Making a node
    def __init__(self, value):
        self.value = value # This is the value of the node
        self.next = None # This is where we create the next value?

class SList:
    def __init__(self):
        self.head = None # Initialize the head, where we start (Head starts off as None)
    
    def add_to_front(self, value):
        new_node = SLNode(value) # Create the node with the value given and the next node with a value of None
        current_head = self.head # Updates head, so when we do start current_head = None
        new_node.next = current_head # Sets the next node from line 11 as head
        self.head = new_node # Now new node value is updated as head, with next being current_head?
        return self
    
    def print_values(self):
        runner = self.head # Initialize runner to start from the beginning (Imagine as: while (i < length) i++)
        while (runner != None): # Traverse until we hit the tail, which has the value of none
            print(runner.value) # Print the runner's value as we go through the list
            runner = runner.next # Iterates runner by +1 so we can move from head to tail
        return self # Allows chaining
    
    def add_to_back(self, value):
        new_node = SLNode(value) # Creates a new node
        runner = self.head # Initialize runner to start from the beginning
        while (runner.next != None): # Runner goes to tail
            runner = runner.next # Iterates runner by +1 so we can move from head to tail
        runner.next = new_node # Changes tail to new_node and creates another node with a value of None
        return self

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked Lists").add_to_back("fun!").print_values()