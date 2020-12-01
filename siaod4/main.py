prior = {None: -1, '(': 0, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4}


def main():
    expression = input("Введите выражение:")
    print(toPostfix(expression))
    print(toPrefix(expression))


def toPostfix(expression):
    stack = Stack()
    rank = 0
    parentheses = 0
    prefix = ''
    for char in expression:
        if char in prior:
            rank -= 1
            if prior[char] > prior[stack.peek()] or prior[char] == 0:
                stack.push(char)
                if char == '(':
                    parentheses += 1
            else:
                while prior[stack.peek()] >= prior[char]:
                    prefix += stack.pop()
                if char != ')':
                    stack.push(char)
                else:
                    parentheses -= 1
                    rank += 2
                    stack.pop()
        else:
            rank += 1
            prefix += char
    while stack.size > 0:
        prefix += stack.pop()
    if rank == 1 and parentheses == 0:
        return prefix
    else:
        return 'Введено некорректное выражение'


def toPrefix(expression):
    prefix = ''
    postfix = toPostfix(expression)
    if postfix != 'Введено некорректное выражение':
        for i in range(len(postfix) - 1, -1, -1):
            prefix += postfix[i]
        return prefix
    else:
        return postfix


class Stack:
    class Node:
        def __init__(self, next, data):
            self.data = data
            self.next = next

    def __init__(self):
        self.top = self.Node(None, None)
        self.size = 0

    def push(self, data):
        node = self.Node(self.top, data)
        self.top = node
        self.size += 1

    def pop(self):
        data = self.top.data
        if self.size > 0:
            self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        return self.top.data


if __name__ == '__main__':
    main()
