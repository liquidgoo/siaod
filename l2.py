def main():
    table = Table()
    while True:
        try:
            com = int(input("1 - Добавить\n"
                            "2 - Найти по строке и столбцу\n"
                            "3 - Найти по значению\n"
                            "4 - Удалить\n"
                            ": "))
            if com == 1:
                value = input("Слово: ")
                table.append(value)
            elif com == 2:
                row, column = 0, 0
                success = False
                while not success or row > 64:
                    try:
                        row = int(input("Строка: "))
                        success = True
                    except ValueError:
                        print("Введите целое число")
                success = False
                while not success:
                    try:
                        column = int(input("Столбец: "))
                        success = True
                    except ValueError:
                        print("Введите целое число")
                print(table.find_by_index(row, column))
            elif com == 3:
                value = input("Слово: ")
                print(table.find_by_value(value))
            elif com == 4:
                value = input("Слово: ")
                table.remove(value)
        except ValueError:
            print("Введите число от 1 до 4")


def my_hash(value):
    sum = 0
    for i in range(len(value)):
        sum += ord(value[i])
    return sum % 64


class Table:
    class List:
        class Node:
            def __init__(self, next, value):
                self.next = next
                self.value = value

        def __init__(self):
            self.head = self.Node(None, None)

        def append(self, value):
            current = self.head
            while current.next is not None and value < current.next.value:
                current = current.next
            if current.next is not None and current.next.value == value:
                return -1
            else:
                current.next = self.Node(current.next, value)
                return 1

        def find_by_value(self, value):
            current = self.head
            i = -1
            while current.next is not None:
                current = current.next
                i += 1
                if current.value == value:
                    return i
            return -1

        def find_by_index(self, index):
            current = self.head
            for i in range(index + 1):
                if current.next is None:
                    return -1
                else:
                    current = current.next
            return current.value

        def remove(self, value):
            current = self.head
            while current.next is not None and current.next.value != value:
                current = current.next
            if current.next is None:
                return -1
            else:
                current.next = current.next.next
                return 1

    def __init__(self):
        self.list = []
        for i in range(64):
            self.list.append(self.List())

    def append(self, value):
        return self.list[my_hash(value)].append(value)

    def find_by_value(self, value):
        index = self.list[my_hash(value)].find_by_value(value)
        if index != -1:
            return -1
        else:
            return my_hash(value), self.list[my_hash(value)].find_by_value(value)

    def find_by_index(self, row, column):
        return self.list[row].find_by_index(column)

    def remove(self, value):
        return self.list[my_hash(value)].remove(value)


if __name__ == "__main__":
    main()
