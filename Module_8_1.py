def add_everything_up(a, b):
    try:
        # Пытаемся сложить a и b
        return a + b
    except TypeError:
        # Если возникает TypeError, возвращаем строковое представление a и b
        return f"{a}{b}"

# Примеры использования:
print(add_everything_up(5, 10))        # 15
print(add_everything_up(3.5, 2.5))     # 6.0
print(add_everything_up("Hello, ", "World!"))  # Hello, World!
print(add_everything_up(5, "abc"))     # 5abc
print(add_everything_up("abc", 5))     # abc5