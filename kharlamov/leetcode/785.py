class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Инициализируем массив для хранения цвета каждого узла
        color = [-1] * len(graph)

        # Определяем вспомогательную функцию DFS
        def dfs(node, c):
            # Присваиваем цвет текущему узлу
            color[node] = c
            # Проходим по всем соседям текущего узла
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    # Если сосед не окрашен, рекурсивно запускаем DFS с противоположным цветом
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == color[node]:
                    # Если сосед уже окрашен в тот же цвет, что и текущий узел, граф не двудольный
                    return False
            return True

        # Проверяем все узлы в графе
        for node in range(len(graph)):
            if color[node] == -1:
                # Если узел не окрашен, запускаем DFS с начальным цветом 0
                if not dfs(node, 0):
                    return False
        
        return True