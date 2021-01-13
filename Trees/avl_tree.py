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

        return plr

    def rr_rotation(self, parent):
        pr = parent.right
        prl = pr.left

        pr.left = parent
        parent.right = prl
        parent.height = self.node_height(parent)
        pr.height = self.node_height(pr)

        if self.root == parent:
            self.root = pr

        return pr

    def rl_rotation(self, parent):
        pr = parent.right
        prl = pr.left

        pr.left = prl.right
        parent.right = prl.left

        prl.right = pr
        prl.left = parent

        pr.height = self.node_height(pr)
        parent.height = self.node_height(parent)
        prl.height = self.node_height(prl)

        if self.root == parent:
            self.root = prl

        return prl

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
            return self.ll_rotation(temp)
        elif self.balance_factor(temp) == 2 and self.balance_factor(temp.left) == -1:
            return self.lr_rotation(temp)
        elif self.balance_factor(temp) == -2 and self.balance_factor(temp.right) == -1:
            return self.rr_rotation(temp)
        elif self.balance_factor(temp) == -2 and self.balance_factor(temp.right) == 1:
            return self.rl_rotation(temp)

        return temp

    def rec_insert(self, key):
        if self.root is None:
            self.root = self.__rec_insert(self.root, key)
        else:
            self.__rec_insert(self.root, key)

    def __in_order(self, p):
        if p:
            self.__in_order(p.left)
            print(p.data, end=' ')
            self.__in_order(p.right)

    def in_order(self):
        self.__in_order(self.root)


def main():
    tree = AVLTree()
    tree.rec_insert(10)
    tree.rec_insert(20)
    tree.rec_insert(30)
    tree.rec_insert(25)
    tree.rec_insert(28)
    tree.rec_insert(27)
    tree.rec_insert(5)
    print(tree.root.left.data, tree.root.right.data, tree.root.right.left.data)
    tree.in_order()


if __name__ == '__main__':
    main()
