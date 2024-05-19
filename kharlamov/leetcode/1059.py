class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Построение графа в виде списка смежности
        graph = defaultdict(list)  # Инициализация списка смежности для n узлов
        for u, v in edges:  # Заполнение списка смежности
            graph[u].append(v)
        
        # Мемоизация состояний узлов: 0 - не посещен, 1 - посещен в текущем пути, 2 - полностью обработан
        states = [0] * n  # Инициализация списка состояний для каждого узла

        def dfs(node: int) -> bool:
            if states[node] != 0:  # Узел уже посещен ранее
                return states[node] == 2  # Если узел полностью обработан, возвращаем True
            
            if not graph[node]:  # Узел не имеет исходящих ребер
                return node == destination  # Проверяем, является ли узел назначением
            
            states[node] = 1  # Помечаем узел как посещенный в текущем пути
            
            for neighbor in graph[node]:  # Рекурсивно посещаем соседние узлы
                if not dfs(neighbor):  # Если обнаружен путь, который не ведет к назначению, возвращаем False
                    return False
            
            states[node] = 2  # Узел полностью обработан
            return True  # Все пути от узла проверены и ведут к назначению
        
        return dfs(source)  # Запускаем DFS с узла-источника