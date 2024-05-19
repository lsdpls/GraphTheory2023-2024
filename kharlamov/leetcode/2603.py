class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        # Создаем граф в виде списка смежности
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Находим все начальные листья без монет
        initial_leaves = deque()
        for i in range(len(coins)):
            if len(graph[i]) == 1 and coins[i] == 0:  # Условие для листа без монеты
                initial_leaves.append(i)

        # Удаляем начальные листья без монет
        while initial_leaves:
            leaf = initial_leaves.popleft()  # Извлекаем лист из очереди
            if graph[leaf] and coins[leaf] == 0:  # Проверяем, что лист существует и без монеты
                neighbor = graph[leaf][0]  # Получаем соседа листа
                graph[neighbor].remove(leaf)  # Удаляем лист из смежности соседа
                graph[leaf] = []  # Очищаем смежности листа
                if len(graph[neighbor]) == 1 and coins[neighbor] == 0:  # Проверяем, что сосед стал листом без монеты
                    initial_leaves.append(neighbor)  # Добавляем соседа в очередь

        # Удаление двух последних слоев листьев
        for _ in range(2):
            leaves = [i for i in range(len(coins)) if len(graph[i]) == 1]  # Находим текущие листья
            for leaf in leaves:
                if graph[leaf]:
                    neighbor = graph[leaf][0]  # Получаем соседа листа
                    graph[neighbor].remove(leaf)  # Удаляем лист из смежности соседа
                    graph[leaf] = []  # Очищаем смежности листа

        # Подсчитываем количество оставшихся рёбер
        remaining_edges = sum(len(neighbors) for neighbors in graph.values()) // 2  # Каждое ребро учитывается дважды

        # Возвращаем минимальное количество проходов через рёбра
        return remaining_edges * 2  # Учитываем поход туда и обратно
