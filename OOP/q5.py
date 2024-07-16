class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.value)
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert_recursive(self.root,value)

    def __insert_recursive(self, node,value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.__insert_recursive(node.left,value)
        elif value >node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.__insert_recursive(node.right,value)


    def search(self, value):
        return self._search_recursive(self.root,value)
    
    def _search_recursive(self,node,value):
        if node is None or node.value == value:
            return node
        if value <node.value:
            return self._search_recursive(node.left,value)
        else:
            return self._search_recursive(node.right,value)
        

bst  = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)
print("Searching of element: ")
print(bst.search(4))
print(bst.search(1))