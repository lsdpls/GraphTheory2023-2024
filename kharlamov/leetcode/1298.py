class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # Инициализация очереди для хранения коробок, которые будем обрабатывать
        queue = deque()
        # Множество для хранения всех доступных коробок (открытых и закрытых)
        available_boxes = set(initialBoxes)
        # Множество для отслеживания коробок, из которых уже забрали конфеты
        collected_boxes = set()
        # Переменная для хранения общего количества конфет
        total_candies = 0

        # Добавляем все изначально открытые коробки в очередь
        for box in initialBoxes:
            if status[box] == 1:  # Проверяем, открыта ли коробка
                queue.append(box)  # Добавляем открытую коробку в очередь

        # Обработка коробок с помощью BFS
        while queue:
            current_box = queue.popleft()  # Извлекаем текущую коробку из очереди

            # Пропускаем коробки, из которых уже забрали конфеты
            if current_box in collected_boxes:
                continue  # Пропускаем коробку, если из нее уже забрали конфеты

            # Собираем конфеты из текущей коробки
            total_candies += candies[current_box]
            collected_boxes.add(current_box)  # Помечаем коробку как обработанную

            # Обрабатываем ключи, найденные в текущей коробке
            for key in keys[current_box]:
                status[key] = 1  # Открываем коробку с найденным ключом
                if key in available_boxes and key not in collected_boxes:
                    queue.append(key)  # Добавляем открытую коробку в очередь, если она у нас есть и не была обработана

            # Обрабатываем вложенные коробки
            for inner_box in containedBoxes[current_box]:
                available_boxes.add(inner_box)  # Добавляем вложенную коробку в доступные
                if status[inner_box] == 1 and inner_box not in collected_boxes:
                    queue.append(inner_box)  # Добавляем вложенную коробку в очередь, если она открыта и не была обработана

        return total_candies  # Возвращаем общее количество собранных конфет
