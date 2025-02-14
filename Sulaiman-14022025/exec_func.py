code = """
def greet():
    print("Hello, Boss!")

greet()
"""

exec(code)


class_code = """
class DynamicClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
"""

exec(class_code)

obj = DynamicClass("Boss")
print(obj.greet())  # Output: Hello, Boss!
