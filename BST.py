class TreeNode:
    def __init__(self, val: int):
        self._val = val
        self._left = None
        self._right = None
    
    def getVal(self):
        return self._val
    
    def getLeft(self):
        return self._left
    
    def getRight(self):
        return self._right

    def setVal(self, val: int):
        self._val = val
    
    def setLeft(self, node):
        self._left = node
    
    def setRight(self, node):
        self._root = node

class BST:
    def __init__(self, root: TreeNode | None):
        self._root = root
    
    def insert(self, val: int):
        node = TreeNode(val)
        if self._root is None:
            self._root = node
            return
        prev = None
        current = self._root
        while current != None:
            if current.getVal() > val:
                prev = current
                current = current.getLeft()
            elif current.getVal() < val:
                prev = current
                current = current.getRight()
        if prev.getVal() > val:
            prev.setLeft(node)
        else:
            prev.setLeft(node)
    
    def search(self, val: int) -> TreeNode | None:
        if self._root is None:
            return None
        current = self._root
        while current != None:
            if current.getVal() < val:
                current = current.getLeft()
            elif current.getVal() > val:
                current = current.getRight()
            else:
                return current
        
        return None
