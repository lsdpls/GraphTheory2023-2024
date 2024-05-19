class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # Проверяем, есть ли достаточное количество соединений
        if len(connections) < n - 1:
            return -1
        
        # Создаем список смежности для хранения связей между узлами
        adjacency = [[] for _ in range(n)]
        # Заполняем список смежности на основе переданных соединений
        for u, v in connections:
            adjacency[u].append(v)
            adjacency[v].append(u)
        
        # Инициализируем переменные
        ans = -1  # Количество операций, необходимых для связывания компонентов
        visited = set()  # Множество для отслеживания посещенных узлов
        
        # Определяем функцию DFS для обхода графа
        def dfs(node):
            visited.add(node)
            # Рекурсивно обходим смежные узлы текущего узла
            for n in adjacency[node]:
                if n not in visited:
                    dfs(n)
        
        # Итерируем по всем узлам
        for node in range(n):
            # Если узел не был посещен, запускаем DFS
            if node not in visited:
                dfs(node)
                # После завершения обхода увеличиваем количество компонентов
                ans += 1
        
        # Возвращаем количество компонентов
        return ans