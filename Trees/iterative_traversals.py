from stack.linked_list_stack import LinkedListStack
from Trees.tree_class import Tree


def iter_pre_order(p):
    stk = LinkedListStack()

    while p or not stk.is_empty():
        if p:
            print(p.data, end=' ')
            stk.push(p)
            p = p.left
        else:
            p = stk.pop()
            p = p.right
    print()


def iter_in_oder(p):
    stk = LinkedListStack()
    while p or not stk.is_empty():
        if p:
            stk.push(p)
            p = p.left
        else:
            p = stk.pop()
            print(p.data, end=' ')
            p = p.right
    print()


def iter_post_order(p):
    stk = LinkedListStack()
    last_visited = None
    while p or not stk.is_empty():
        if p:
            stk.push(p)
            p = p.left
        else:
            peekNode = stk.st_top()
            #  if right child exists and traversing node
            #  from left child, then move right
            if peekNode.right is not None and last_visited is not peekNode.right:
                p = peekNode.right
            else:
                print(peekNode.data, end=' ')
                last_visited = stk.pop()
    print()


def main():
    tree = Tree()
    tree.create()
    print("Pre order iteratively:", end=' ')
    iter_pre_order(tree.root)
    print("In order tree traversal iteratively:", end=' ')
    iter_in_oder(tree.root)
    print("Post order traversal iteratively:", end=' ')
    iter_post_order(tree.root)


if __name__ == '__main__':
    main()
