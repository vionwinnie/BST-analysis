import BSTDataModel

bst = BSTDataModel.BSTDataModel() 

def add(value): # add a node with the value, value iff cur node in null (if you break the BST properties it's on you)
        if bst.current is None:
                bst.current = BSTDataModel.Node(value)
def std_remove(): # preforms a standard BST remove and remains on the last node traversed too (NULL?)
        if bst.current is None:
                return False  # empty node cannot be removed
        elif bst.current.l is not None and bst.current.r is not None:
                bst.current = None # Directly remove node
                return True
        elif 
        successor = bst.current.r
        while successor.l is not None:
                
def read_closure():
        pass                  # returns the closure for the node you are currently on
def write_closure(cl):
        pass               # sets the closure for the current node 
def read_gclosure():
        pass                 # reads the global closure
def write_gclosure(cl):
        pass              # writes the closure
def is_null():
        pass                       # is the current node null?
def read_value():
        pass                    # returns the value of the current node
def write_value(val):
        pass                # sets the value of cur node
def move_right():
        pass                    # sets cur node to right child
def move_left():
        pass                     # ---------------- left ----- 
def move_parent():
        pass                   # ------------------ parent 