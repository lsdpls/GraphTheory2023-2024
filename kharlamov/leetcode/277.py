class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0  # Изначально предполагаем, что знаменитость - человек 0

        # Шаг 1: Определение кандидата на роль знаменитости
        for i in range(1, n):
            if knows(candidate, i):  # Если кандидат знает i, то кандидат не может быть знаменитостью
                candidate = i  # Теперь кандидат - человек i
        
        # Шаг 2: Проверка кандидата на соответствие условиям знаменитости
        for i in range(n):
            if i != candidate:  # Проверяем всех, кроме самого кандидата
                if knows(candidate, i) or not knows(i, candidate):  # Если кандидат знает кого-то или кто-то не знает кандидата
                    return -1  # Возвращаем -1, если кандидат не соответствует условиям знаменитости
        
        return candidate  # Возвращаем кандидата, если он прошел все проверки