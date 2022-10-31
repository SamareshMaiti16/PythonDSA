class Node:
    def __init__(self, data):
        self.item = data #store the actual data for the node.
        self.nref = None #store the reference to the next node.
        self.pref = None #store the reference to the previous node.

class DoublyLinkedList: #contains different doubly linked list related functions.
    def __init__(self):
        self.start_node = None #initializes the doubly linked list.

    def insertion_in_emptylist(self, data): #insert an item in the empty list.
        if self.start_node is None: #if the variable is none it means empty list.
            new_node = Node(data) #value is initialized by data parameter.
            self.start_node = new_node
        else:
            print("list is not empty")

    def insertion_at_start(self, data): # insert an item at the beginning of the doubly linked list .
        if self.start_node is None: #insert the element in an empty list.
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insertion_at_end(self, data): #Inserting an element at the end of the doubly linked list.
        if self.start_node is None: #check if the list is empty
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None: #traverse through the list until the reference to the next node becomes None.
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def insertion_after_node(self, x, data): #insertion after node.
        if self.start_node is None: #check whether or not the list is empty.
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x: #node is found and it is selected .
                    break
                n = n.nref
            if n is None: #node after which we want to insert the new node is not found.
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None: #If the selected node is not the last node.
                    n.nref.prev = new_node
                n.nref = new_node 

    def insertion_before_node(self, x, data): #insertion before a node.
        if self.start_node is None: # check whether or not the list is empty.
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x: #node is found and it is selected.
                    break
                n = n.nref
            if n is None: #node before which we want to insert the new node is not found.
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node                  

    def print_list(self): #print the list.
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.nref       

    def deletion_at_start(self): #deletion at start
        if self.start_node is None: 
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None: #If the list contains only one element.
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None;    

    def deletion_at_end(self): #deletion at end
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None: #iterate through the list until the last node is reached.
            n = n.nref
        n.pref.nref = None      

    def delete_a_node(self, x): #deleting a node.
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None: # if the list has a single element .
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return 

        if self.start_node.item == x: #if item to be deleted is the first item.
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node 
        while n.nref is not None: #if the list contains multiple items and the item to be deleted is not the first item.
            if n.item == x:
                break;
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def search_for_node(self ,item): #searching for a node . 
        temp = self.start_node
        while temp:
            if temp.item == item:
                break
            temp = temp.nref
        if temp==None:
            print("The given element doesn't exist")
            return False
        return True           

    def number_of_nodes(self): #number of nodes in the list.
        if self.start_node is None:
            print(0)
            return 
        count = 0    
        current = self.start_node
        while(current != None):  
            #Increment the counter by 1 for each node  
            count = count + 1;  
            current = current.nref;
        print("No. of total elements in list :",count)           

new_DLL = DoublyLinkedList()

new_DLL.insertion_in_emptylist(50)

new_DLL.insertion_at_start(10)
new_DLL.insertion_at_start(5)
new_DLL.insertion_at_start(18)
new_DLL.insertion_at_end(29)
new_DLL.insertion_at_end(39)
new_DLL.insertion_at_end(49)
new_DLL.insertion_after_node(50, 65)
new_DLL.insertion_before_node(29, 100)
new_DLL.deletion_at_start()
new_DLL.deletion_at_end()
new_DLL.delete_a_node(100)
new_DLL.print_list()
new_DLL.number_of_nodes()
new_DLL.search_for_node(100)

