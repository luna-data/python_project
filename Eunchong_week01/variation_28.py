class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


def path_length(moves):
    total = 0
    for v in moves:
        total += v.length()
    return total


# 사용 예시
moves = [
    Vector2D(3, 4),   # 길이 5
    Vector2D(1, 1),   # 길이 sqrt(2)
    Vector2D(-2, 2)   # 길이 sqrt(8)
]

total_dist = path_length(moves)
print("총 이동 거리:", round(total_dist, 2))
