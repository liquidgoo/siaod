class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        node = self.Node(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            previous = current
            is_left = False
            while current is not None:
                previous = current
                if data < current.data:
                    current = current.left
                    is_left = True
                elif data > current.data:
                    current = current.right
                    is_left = False
                else:
                    return -1
            if is_left:
                previous.left = node
            else:
                previous.right = node
        return 0

    def contains(self, data):
        current = self.root
        while current is not None:
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return True
        return False

    def remove(self, data):
        current = self.root
        previous = current
        is_left = False
        while current is not None and current.data != data:
            previous = current
            if data < current.data:
                current = current.left
                is_left = True
            else:
                current = current.right
                is_left = False
        if current is None:
            return -1

        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif is_left:
                previous.left = None
            else:
                previous.right = None

        elif current.left is None or current.right is None:
            if current == self.root:
                if current.right is not None:
                    self.root = current.right
                else:
                    self.root = current.left
            elif is_left:
                if current.right is not None:
                    previous.left = current.right
                else:
                    previous.left = current.left
            else:
                if current.right is not None:
                    previous.right = current.right
                else:
                    previous.right = current.left

        else:
            child = current.right
            child_parent = child
            while child.left is not None:
                child_parent = child
                child = child.left

            if child != current.right:
                child_parent.left = child.right
                child.right = current.right
            child.left = current.left

            if current == self.root:
                self.root = child
            elif is_left:
                previous.left = child
            else:
                previous.right = child
        return 0

    def direct_visit(self, *args):
        arr = []
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]
        if node is not None:
            arr += node.data
            if node.left is not None:
                arr += self.direct_visit(node.left)
            if node.right is not None:
                arr += self.direct_visit(node.right)
        return arr

    def reverse_visit(self, *args):
        arr = []
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]
        if node is not None:
            if node.left is not None:
                arr += self.reverse_visit(node.left)
            if node.right is not None:
                arr += self.reverse_visit(node.right)
            arr += node.data
        return arr

    def symmetric_visit(self, *args):
        arr = []
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]
        if node is not None:
            if node.left is not None:
                arr += self.symmetric_visit(node.left)
            arr += node.data
            if node.right is not None:
                arr += self.symmetric_visit(node.right)
        return arr


def main():
    tree = Tree()
    while True:
        com = input()
        if com == 'insert':
            print(tree.insert(input()))
        elif com == 'remove':
            print(tree.remove(input()))
        elif com == 'contains':
            print(tree.contains(input()))
        elif com == 'visit':
            com = input()
            if com == 'direct':
                print(tree.direct_visit())
            elif com == 'reverse':
                print(tree.reverse_visit())
            elif com == 'symmetric':
                print(tree.symmetric_visit())


if __name__ == '__main__':
    main()
