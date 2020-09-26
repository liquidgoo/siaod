def main():
    d_list = DList()
    while True:
        com = int(input(
            '1 - Добавить абонента\n2 - Добавить службу\n3 - Вывести двунапр. список\n4 - Вывести однонапр. список\n:'))
        if com == 1 or com == 2:
            num_len = 7
            is_service = False
            prompt = 'Фио:'
            if com == 2:
                num_len = 3
                is_service = True
                prompt = 'Назв. службы:'

            name = input(prompt)

            num = ''
            while len(num) != num_len:
                num = input('Номер:')
            d_list.add(num, name, is_service)
        elif com == 3:
            print(d_list.to_string())
        elif com == 4:
            s_list = SList(d_list)
            print(s_list.to_string())


class DList:
    class DEntry:
        def __init__(self, prev, num, name, is_service):
            self.head = None
            self.prev = prev

            self.num = num
            self.name = name
            self.is_service = is_service

    def __init__(self):
        self.head = self.DEntry(None, None, None, None)
        self.size = 0

    def add(self, num, name, is_service):
        current = self.head
        for i in range(self.size):
            current = current.next

        current.next = self.DEntry(current, num, name, is_service)
        self.head.prev = current.next
        current.next.next = self.head

        self.size += 1

    def to_string(self):
        out = ''
        current = self.head
        for i in range(self.size):
            current = current.next
            out += '{:7}  | {}\n'.format(current.num, current.name)
        return out


class SList:
    class SEntry:
        def __init__(self, next, num, name):
            self.next = next
            self.num = num
            self.name = name

    def __init__(self, d_list):
        self.head = self.SEntry(None, None, None)
        self.size = 0

        current = d_list.head

        for i in range(d_list.size):
            current = current.prev
            if not current.is_service:
                self.insert(current.num, current.name)
                self.size += 1

    def insert(self, num, name):
        current = self.head

        while current.next is not None and name > current.next.name:
            current = current.next

        current.next = self.SEntry(current.next, num, name)

    def to_string(self):
        out = ''
        current = self.head
        for i in range(self.size):
            current = current.next
            out += current.num + ' | ' + current.name + '\n'
        return out


if __name__ == '__main__':
    main()
