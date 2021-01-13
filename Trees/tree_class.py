from Queue.queue import LinkedListQueue


class TreeNode:
    def __init__(self, data=None):
        self.left = None
        self.data = data
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def create(self):
        q = LinkedListQueue()
        self.root = TreeNode(int(input("Enter root value: ")))
        q.enqueue(self.root)

        while not q.is_empty():
            p = q.dequeue()
            # Left Child
            temp_left = int(input("enter left child of {}: ".format(p.data)))
            if temp_left != -1:
                new_node = TreeNode(temp_left)
                p.left = new_node
                q.enqueue(new_node)
            # Right Child
            temp_right = int(input("enter right child of {}: ".format(p.data)))
            if temp_right != -1:
                new_node = TreeNode(temp_right)
                p.right = new_node
                q.enqueue(new_node)

    def preorder(self, p):
        if p:
            print(p.data, end=' ')
            self.preorder(p.left)
            self.preorder(p.right)

    def pre_order(self):
        self.preorder(self.root)

    def inorder(self, p):
        if p:
            self.inorder(p.left)
            print(p.data, end=' ')
            self.inorder(p.right)

    def in_order(self):
        self.inorder(self.root)

    def postorder(self, p):
        if p:
            self.postorder(p.left)
            self.postorder(p.right)
            print(p.data, end=' ')

    def post_order(self):
        self.postorder(self.root)

    def level_order(self):
        q = LinkedListQueue()
        p = self.root
        q.enqueue(p)
        print(p.data, end=' ')
        while not q.is_empty():
            p = q.dequeue()
            if p.left:
                print(p.left.data, end=' ')
                q.enqueue(p.left)
            if p.right:
                print(p.right.data, end=' ')
                q.enqueue(p.right)
        print()

    def height(self, p):
        if p is None:
            return 0
        else:
            x = self.height(p.left)
            y = self.height(p.right)
            if x > y:
                return x + 1
            else:
                return y + 1

    def Height(self):
        return self.height(self.root)


def main():
    tree = Tree()
    tree.create()

    print("Pre order tree traversal")
    tree.pre_order()
    print()
    print("In order tree traversal")
    tree.in_order()
    print()
    print("Post order tree traversal")
    tree.post_order()
    print()
    print("Level order tree traversal")
    tree.level_order()
    print("Height of tree:", tree.Height())


if __name__ == '__main__':
    main()
