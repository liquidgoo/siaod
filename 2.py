def main():
    k = int(input('Введите k: '))
    print('size | список')
    for i in range(1, 65):
        ring = KidList(i)
        print('{:5}|{}'.format(i, ring.kick(k)))


class Kid:
    def __init__(self, num):
        self.next = None
        self.num = num


class KidList:
    def __init__(self, size):
        self.size = size
        self.head = Kid(-1)
        current = self.head
        for i in range(size):
            current.next = Kid(i)
            current = current.next
        current.next = self.head.next

    def kick(self, k):
        current = self.head
        while self.size > k:  # while self.size > k
            for i in range(k - 1):
                current = current.next
            if self.head.next == current.next:
                self.head.next = current.next.next
            current.next = current.next.next
            self.size -= 1
        current = self.head
        string = ''
        for i in range(self.size - 1):
            current = current.next
            string += str(current.num) + ', '
        string += str(current.next.num)
        return string


if __name__ == '__main__':
    main()
