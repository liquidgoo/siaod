def main():
    while True:
        string = input('Введите список весов для очередей в одну строку: ')
        weights = list(float(weight) for weight in string.split())
        if sum(weights) == 1:
            in_range = True
            for weight in weights:
                if weight > 1 or weight <=0:
                    print('Веса должны быть в промежутке (0;1]')
                    in_range = False
                    break
            if in_range:
                break
        else:
            print('Сумма весов дожна ровняться 1')
    queue = CombinedQueue(weights)
    while True:
        com = int(input('1 - Добавить элемент в приоритетную очередь\n'
                        '2 - Добавить элемент в взвешенную очередь\n'
                        '3 - Извлечь 3 элементов из комбинированной очереди\n'))
        if com == 1:
            data = input('Введите данные: ')
            priority = int(input('Введите приоритет: '))
            queue.enqueue(data, priority, True)
        elif com == 2:
            data = input('Введите данные: ')
            while True:
                weight = float(input('Введите вес: '))
                if weight in queue.queues:
                    break
                else:
                    print('Нет очереди с таким весом')
            queue.enqueue(data, weight)
        elif com == 3:
            print(queue.dequeue())


class CombinedQueue:
    class Queue:
        class Node:
            def __init__(self, next, data):
                self.next = next
                self.data = data

        def __init__(self):
            self.head = self.Node(None, None)
            self.tail = self.head
            self.size = 0

        def enqueue(self, data):
            self.tail.next = self.Node(None, data)
            self.tail = self.tail.next
            self.size += 1

        def dequeue(self):
            temp = self.head.next.data
            self.head.next = self.head.next.next
            if self.size > 0:
                self.size -= 1
            return temp

    class PriorityQueue:
        class Node:
            def __init__(self, next, data, priority):
                self.next = next
                self.data = data
                self.priority = priority

        def __init__(self):
            self.head = self.Node(None, None, None)
            self.tail = self.head
            self.size = 0

        def enqueue(self, data, priority):
            current = self.head
            while current.next is not None and current.next.priority > priority:
                current = current.next
            current.next = self.Node(current.next, data, priority)
            self.size += 1

        def dequeue(self):
            temp = self.head.next.data
            self.head.next = self.head.next.next
            self.size -= 1
            return temp

    def __init__(self, weights: list):
        self.p_queue = self.PriorityQueue()
        self.queues = {}
        for weight in weights:
            self.queues[weight] = self.Queue()

    def enqueue(self, data, priority, prioritized=False):
        if prioritized:
            self.p_queue.enqueue(data, priority)
        else:
            if priority in self.queues:
                self.queues[priority].enqueue(data)
                return 1
            else:
                return -1

    def dequeue(self):
        pack = []
        left = 3
        while self.p_queue.size > 0 and left > 0:
            pack.append(self.p_queue.dequeue())
            left -= 1
        if left > 0:
            temp = left
            quantities = {}
            weight_sum = 1
            enough = False
            while not enough:
                enough = True
                for weight in self.queues:
                    if weight in quantities:
                        continue
                    if self.queues[weight].size <= (weight / weight_sum) * temp:
                        quantities[weight] = self.queues[weight].size
                        temp -= self.queues[weight].size
                        weight_sum -= weight
                        enough = False
            for weight in self.queues:
                if weight in quantities:
                    continue
                else:
                    quantities[weight] = round((weight / weight_sum) * temp)
            for weight in quantities:
                for i in range(quantities[weight]):
                    if left == 0:
                        break
                    else:
                        pack.append(self.queues[weight].dequeue())
                        left -= 1
        return pack


if __name__ == '__main__':
    main()
