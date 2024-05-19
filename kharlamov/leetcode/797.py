class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)  # Получаем количество узлов в графе
        target = n - 1  # Определяем индекс целевого узла
        
        # Инициализация стека с начальными путями
        stack = [(0, [0])]  # Каждый элемент стека - кортеж (узел, путь до этого узла)
        paths = []  # Список для хранения всех путей
        
        # Пока стек не пуст
        while stack:
            node, path = stack.pop()  # Извлекаем узел и его путь из стека
            
            # Если текущий узел является целевым
            if node == target:
                paths.append(path)  # Добавляем путь в список путей
            
            # Иначе продолжаем исследование
            else:
                # Для каждого соседа текущего узла
                for neighbor in graph[node]:
                    # Добавляем в стек кортеж с соседним узлом и новым путем, содержащим соседа
                    stack.append((neighbor, path + [neighbor]))
        
        return paths  # Возвращаем список всех путей