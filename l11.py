import re


def main():
    while True:
        com = input(
            "Команда: 1 - Сравнить многочлены \n"
            "         2 - Вычислить значение многочлена в точке x\n"
            "         3 - Вычислить сумму многочленов\n"
            ":")
        a = polynomial_input()
        if com == '1':
            b = polynomial_input()
            print(equality(a, b))
        elif com == '2':
            x = input("Введите x:")
            print(meaning(a, int(x)))
        elif com == '3':
            b = polynomial_input()
            c = Polynomial()
            add(c, a, b)
            print(c.output())


class Entry:
    def __init__(self, n, a, next):
        self.next = next
        self.n = n
        self.a = a


class Polynomial:
    def __init__(self):
        self.head = Entry(None, None, None)
        self.size = 0

    def add(self, n, a):
        if a != 0:
            current = self.head
            while current.next is not None:
                if current.next.n > n:
                    current = current.next
                else:
                    break
            if current.next is not None and current.next.n == n:
                current.next.a += a
                if current.next.a == 0:
                    current.next = current.next.next
                    self.size -= 1
            else:
                new_entry = Entry(n, a, current.next)
                current.next = new_entry
                self.size += 1

    def output(self):
        current = self.head
        string = ""
        for i in range(self.size):
            current = current.next
            if current.a > 0 and i != 0:
                string += "+"
            if current.a != 1 or current.n == 0:
                string += str(current.a)
            if current.n != 0:
                string += "x"
            if current.n > 1:
                string += "^" + str(current.n)
        return string


def equality(p, q):
    equal = True
    if p.size != q.size:
        equal = False
    current_p = p.head
    current_q = q.head
    for i in range(p.size):
        current_p = current_p.next
        current_q = current_q.next
        if current_p.n != current_q.n or current_p.a != current_q.a:
            equal = False
            break
    return equal


def meaning(p, x):
    meaning = 0
    current = p.head
    for i in range(p.size):
        current = current.next
        meaning += current.a * (x ** current.n)
    return meaning


def add(p, q, r):
    p.head = Entry(None, None, None)
    current = q.head
    for i in range(q.size):
        current = current.next
        p.add(current.n, current.a)
    current = r.head
    for i in range(r.size):
        current = current.next
        p.add(current.n, current.a)
    return p


def polynomial_input():
    string = input("Введите многочлен a0x^n+...+an:")
    string = re.sub(r'[+]', ' +', string)
    string = re.sub(r'[-]', ' -', string)
    strings = re.split(r'\s', string)
    a = Polynomial()
    for part in strings:
        nums = re.split(r'[x^]+', part)
        if nums[0] == '' or nums[0] == '-' or nums[0] == '+':
            nums[0] += '1'
        if len(nums) == 1:
            nums.append('0')
        elif nums[1] == '':
            nums[1] += '1'
        a.add(int(nums[1]), int(nums[0]))
    return a


if __name__ == '__main__':
    main()
