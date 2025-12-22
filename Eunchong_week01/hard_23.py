class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print("v1 길이:", v1.length())
print("v2 길이:", v2.length())

v3 = v1.add(v2)
print("v1 + v2 =", v3.x, v3.y)
