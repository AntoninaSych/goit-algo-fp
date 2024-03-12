import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, start, end, weight):
        self.vertices[start].append((end, weight))

    def dijkstra(self, start):
        # Ініціалізуємо відстані до всіх вершин як нескінченні
        distances = {vertex: float('infinity') for vertex in self.vertices}
        # Відстань до початкової вершини дорівнює 0
        distances[start] = 0
        # Ініціалізуємо бінарну купу та додаємо початкову вершину з відстанню 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Якщо знайдено коротший шлях до поточної вершини, оновлюємо відстань
            if current_distance > distances[current_vertex]:
                continue

            # Опрацьовуємо сусідів поточної вершини
            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight

                # Якщо відстань до сусіда менша за поточну відстань, оновлюємо відстань
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Приклад використання:
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

graph.add_edge("A", "B", 6)
graph.add_edge("A", "D", 1)
graph.add_edge("B", "C", 5)
graph.add_edge("B", "D", 2)
graph.add_edge("B", "E", 2)
graph.add_edge("C", "E", 5)
graph.add_edge("D", "E", 1)

distances = graph.dijkstra("A")
print(distances)


# У цьому коді ми спочатку створюємо клас Graph, який представляє граф. Ми використовуємо словник для збереження вершин та їхніх сусідів разом з вагами ребер. Метод dijkstra реалізує алгоритм Дейкстри, використовуючи бінарну купу для оптимізації вибору вершин. Він повертає словник з відстанями до кожної вершини від заданої початкової вершини.

# Приклад використання додає вершини та ребра до графа, а потім викликає метод dijkstra для знаходження найкоротших шляхів від початкової вершини "A" до всіх інших вершин.