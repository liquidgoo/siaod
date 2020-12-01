class Graph:
    def __init__(self, graph):
        self.graph = graph

    def shortest(self, i, j):
        visited = []
        shortest = self.graph[i]
        while len(visited) < len(self.graph):
            current = shortest.index(min(shortest[node] for node in range(len(shortest)) if node not in visited))
            for next_node in range(len(self.graph)):
                new_shortest = shortest[current] + self.graph[current][next_node]
                if new_shortest < shortest[next_node]:
                    shortest[next_node] = new_shortest
            visited.append(current)
        return shortest[j]

    def shortest_pairwise(self):
        shortest = self.graph
        for k in range(len(shortest)):
            for i in range(len(shortest)):
                for j in range(len(shortest)):
                    new_shortest = shortest[i][k] + shortest[k][j]
                    if new_shortest < shortest[i][j]:
                        shortest[i][j] = new_shortest
        return shortest

    def centre(self):
        shortest = self.shortest_pairwise()
        ecc = list(max(paths) for paths in shortest)
        min_ecc = min(ecc)
        return list(node for node in range(len(shortest)) if ecc[node] == min_ecc)


def main():
    n = int(input('Количество вершин:'))
    infinity = 999999999
    graph = []
    for i in range(n):
        graph.append([infinity] * n)
        graph[i][i] = 0
    for i in range(n):
        next = list(int(num) for num in input('Вершины, смыжные с ' + str(i) + ':').split())
        for j in next:
            weight = int(input('Вес вершины ' + str(i) + '->' + str(j) + ':'))
            graph[i][j] = weight
    print()
    graph = Graph(graph)
    while True:
        com = input('s - кротчаший путь между 2 вершинами\n'
                    'sp - кротчайший путь между всеми парами вершин\n'
                    'c - центральная вершина графа\n')
        if com == 's':
            i, j = int(input('Начальная вершина:')), int(input('Конечная вершина:'))
            print(graph.shortest(i, j))
        elif com == 'sp':
            shortest = graph.shortest_pairwise()
            for node in shortest:
                print(list(str(path) + ' ' for path in node))
            print()
        elif com == 'c':
            print(graph.centre())


if __name__ == '__main__':
    main()
