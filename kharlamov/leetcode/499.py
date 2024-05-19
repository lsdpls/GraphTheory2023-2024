from collections import deque
import heapq
from typing import List

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # Размеры лабиринта
        m, n = len(maze), len(maze[0])
        
        # Начальная позиция мяча
        r, c = ball
        
        # Позиция отверстия
        rh, ch = hole
        
        # Очередь для BFS
        pq = [(0, '', r, c)]  # Содержит кортежи (расстояние, путь, текущая строка, текущий столбец)
        
        # Массивы для отслеживания минимальных расстояний и путей
        dist = [[float('inf')] * n for _ in range(m)]
        path = [[''] * n for _ in range(m)]
        
        # Начальное расстояние до стартовой позиции - 0
        dist[r][c] = 0
        
        # Возможные направления движения: вниз, влево, вправо, вверх
        directions = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0)}
        
        def roll(x, y, dx, dy):
            """
            Функция для симуляции движения мяча в заданном направлении
            до столкновения со стеной или достижения отверстия.
            Возвращает конечную позицию и количество пройденных шагов.
            """
            steps = 0
            while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy
                steps += 1
                if (x, y) == (rh, ch):
                    break
            return x, y, steps
        
        # Основной цикл BFS
        while pq:
            dist_so_far, path_so_far, x, y = heapq.heappop(pq)
            # Если текущая позиция - отверстие, возвращаем путь
            if (x, y) == (rh, ch):
                return path_so_far
            # Рассматриваем все возможные направления движения
            for d, (dx, dy) in directions.items():
                nx, ny, steps = roll(x, y, dx, dy)
                new_dist = dist_so_far + steps
                new_path = path_so_far + d
                # Обновляем расстояние и путь, если найден новый лучший путь
                if new_dist < dist[nx][ny] or (new_dist == dist[nx][ny] and new_path < path[nx][ny]):
                    dist[nx][ny] = new_dist
                    path[nx][ny] = new_path
                    heapq.heappush(pq, (new_dist, new_path, nx, ny))
        
        # Если до отверстия не удалось добраться, возвращаем "impossible"
        return "impossible"
