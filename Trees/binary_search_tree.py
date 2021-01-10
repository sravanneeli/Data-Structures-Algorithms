from Trees.tree_class import Tree, TreeNode


class BST(Tree):
    def __init__(self):
        super().__init__()

    def insert(self, key):
        tail = None
        temp = self.root
        if temp is None:
            new_node = TreeNode(key)
            self.root = new_node
            return
        while temp is not None:
            tail = temp
            if key < temp.data:
                temp = temp.left
            elif key > temp.data:
                temp = temp.right
            else:
                return
        new_node = TreeNode(key)
        if new_node.data < tail.data:
            tail.left = new_node
        else:
            tail.right = new_node

    def search(self, key):
        temp = self.root
        while temp:
            if temp.data == key:
                return temp
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def __rec_insert(self, temp, key):
        if temp is None:
            new_node = TreeNode(key)
            return new_node
        if key < temp.data:
            temp.left = self.__rec_insert(temp.left, key)
        elif key > temp.data:
            temp.right = self.__rec_insert(temp.right, key)
        return temp

    def rec_insert(self, key):
        self.__rec_insert(self.root, key)

    @staticmethod
    def __inorder_predecessor(p):
        while p and p.right is not None:
            p = p.right
        return p

    @staticmethod
    def __inorder_successor(p):
        while p and p.left is not None:
            p = p.left
        return p

    def __delete_node__(self, temp, key):
        if temp is None:
            return None
        if temp.left is None and temp.right is None:
            if temp == self.root:
                self.root = None
            del temp
            return None
        if key < temp.data:
            temp.left = self.__delete_node__(temp.left, key)
        elif key > temp.data:
            temp.right = self.__delete_node__(temp.right, key)
        else:
            if self.height(temp.left) > self.height(temp.right):
                predecessor = self.__inorder_predecessor(temp.left)
                temp.data = predecessor.data
                temp.left = self.__delete_node__(temp.left, predecessor.data)
            else:
                successor = self.__inorder_successor(temp.right)
                temp.data = successor.data
                temp.right = self.__delete_node__(temp.right, successor.data)
        return temp

    def delete_node(self, key):
        self.__delete_node__(self.root, key)


def main():
    bst = BST()
    bst.insert(9)
    bst.insert(15)
    bst.insert(5)
    bst.insert(20)
    bst.insert(16)
    bst.insert(8)
    bst.insert(12)
    bst.insert(3)
    bst.insert(6)
    bst.rec_insert(7)  # using recursive insertion

    if bst.search(20):
        print("Key found")
    else:
        print("Key not found")
    if bst.search(25):
        print("Key found")
    else:
        print("Key not found")
    if bst.delete_node(16):
        print("Element is deleted")
    print("Sorted order of bst is given by inorder traversal:", end=' ')
    bst.in_order()


if __name__ == '__main__':
    main()
