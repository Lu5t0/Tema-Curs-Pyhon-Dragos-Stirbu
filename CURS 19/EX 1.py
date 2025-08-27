class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Vector2D ({self.x}, {self.y})"


if __name__ == "__main__":
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)
    v3 = Vector2D(5, 6)

    print ("v1 + v2 =",v1 + v2)
    print("v1 - v2 =", v1 - v2)
    print("v1 + v3 =", v1 + v3)
    print("v1 - v3 =", v1 - v3)