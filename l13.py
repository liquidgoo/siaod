import re


def main():
    my_list = List()
    while True:
        com = int(
            input('1 - Добавить номер\n2 - Найти по фамилии\n3 - Найти по номеру\n4 - Вывести список абонентов\n:'))
        if com == 1:
            name = ''
            while len(re.split(r'\s', name)) != 3:
                name = input('Введите ФИО в указанном порядке:')
            num = ''
            while len(num) != 7:
                num = input('Введите номер из 7 цифр:')
            my_list.add(name, num)
        elif com == 2:
            sn = input('Введите фамилию:')
            print(my_list.find_by_sn(sn))
        elif com == 3:
            num = input('Введите номер:')
            print(my_list.find_by_num(num))
        elif com == 4:
            print(my_list.to_string())


class Entry:
    def __init__(self, name, num, next):
        if name is not None:
            names = re.split(r'\s', name)
            self.fn = names[1]
            self.sn = names[0]
            self.p = names[2]
        else:
            self.fn = None
            self.sn = None
            self.p = None
        self.num = num
        self.next = next


class List:
    def __init__(self):
        self.head = Entry(None, None, None)
        self.size = 0

    def add(self, name, num):
        current = self.head
        while current.next is not None and current.next.sn + current.next.fn + current.next.p < name:
            current = current.next
        current.next = Entry(name, num, current.next)
        self.size += 1

    def find_by_num(self, num):
        names = ""
        current = self.head
        while current.next is not None:
            current = current.next
            if current.num == num:
                names += current.sn + ' ' + current.fn + ' ' + current.p + "\n"
        if names == "":
            return '-1'
        return names

    def find_by_sn(self, sn):
        nums = ""
        current = self.head
        while current.next is not None:
            current = current.next
            if current.sn == sn:
                nums += current.num + ' | ' + current.sn + ' ' + current.fn + ' ' + current.p + "\n"
        if nums == "":
            return '-1'
        return nums

    def to_string(self):
        out = ''
        current = self.head
        for i in range(self.size):
            current = current.next
            out += current.num + ' | ' + current.sn + ' ' + current.fn + ' ' + current.p + '\n'
        return out


if __name__ == '__main__':
    main()
