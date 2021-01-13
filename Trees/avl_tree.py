class AVLNode:
    def __init__(self, data=None):
        self.left = None
        self.data = data
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def node_height(p):
        hl = p.left.height if p and p.left else 0
        hr = p.right.height if p and p.right else 0
        return hl + 1 if hl > hr else hr + 1

    @staticmethod
    def balance_factor(p):
        hl = p.left.height if p and p.left else 0
        hr = p.right.height if p and p.right else 0
        return hl - hr

    def ll_rotation(self, parent):
        pl = parent.left
        plr = pl.right

        pl.right = parent
        parent.left = plr
        parent.height = self.node_height(parent)
        pl.height = self.node_height(pl)

        if self.root == parent:
            self.root = pl

        return pl

    def lr_rotation(self, parent):
        pl = parent.left
        plr = pl.right

        pl.right = plr.left
        parent.left = plr.right

        plr.left = pl
        plr.right = parent

        pl.height = self.node_height(pl)
        parent.height = self.node_height(parent)
        plr.height = self.node_height(plr)

        if self.root == parent:
            self.root = plr

    def __rec_insert(self, temp, key):
        if temp is None:
            new_node = AVLNode(key)
            return new_node
        if key < temp.data:
            temp.left = self.__rec_insert(temp.left, key)
        elif key > temp.data:
            temp.right = self.__rec_insert(temp.right, key)

        temp.height = self.node_height(temp)

        if self.balance_factor(temp) == 2 and self.balance_factor(temp.left) == 1:
            self.ll_rotation(temp)
        elif self.balance_factor(temp) == 2 and self.balance_factor(temp.left) == -1:
            self.lr_rotation(temp)

        return temp

    def rec_insert(self, key):
        if self.root is None:
            self.root = self.__rec_insert(self.root, key)
        else:
            self.__rec_insert(self.root, key)


def main():
    tree = AVLTree()
    tree.rec_insert(50)
    tree.rec_insert(10)
    tree.rec_insert(20)
    print(tree.root.right.data)


if __name__ == '__main__':
    main()
