def main():
    tree = ThreadedTree()
    print('"insert" - добавить узел'
          '"remove" - удалить узел'
          '"visit" - обход')
    while True:
        com = input()
        if com == 'insert':
            print(tree.insert(input()))
        elif com == 'visit':
            print(tree.visit())
        elif com == 'remove':
            print(tree.remove(input()))


class ThreadedTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.right_is_thread = False

    def __init__(self):
        self.previous = None
        self.root = None

    def insert(self, data):
        self.delete_threads()
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
        self.thread()
        return 0

    def remove(self, data):
        self.delete_threads()
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
        self.thread()
        return 0

    def delete_threads(self):
        if self.root is not None:
            self.delete_threads_rec(self.root)

    def delete_threads_rec(self, node):
        if node is not None:
            self.delete_threads_rec(node.left)
            if not node.right_is_thread:
                self.delete_threads_rec(node.right)
            else:
                node.right = None
                node.right_is_thread = False

    def thread(self):
        self.previous = None
        self.thread_rec(self.root)

    def thread_rec(self, node):
        if self.previous is not None:
            self.previous.right = node
            self.previous.right_is_thread = True
            self.previous = None
        if node.left is not None:
            self.thread_rec(node.left)
        if node.right is not None:
            self.thread_rec(node.right)
        else:
            self.previous = node

    def visit(self):
        arr = []
        current = self.root
        while current is not None:
            arr += current.data
            if current.left is not None:
                current = current.left
            else:
                current = current.right
        return arr


if __name__ == '__main__':
    main()
