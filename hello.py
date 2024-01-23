class Greeter:
    def __init__(self, name="World"):
        self.name = name

    def greet(self, greeting="Hello"):
        return f"{greeting}, {self.name}!"

    def farewell(self):
        return f"Goodbye, {self.name}."

    @property
    def name_length(self):
        return len(self.name)

    @name_length.setter
    def name_length(self, value):
        print("Name length cannot be set directly.")

# Example usage
greeter = Greeter("Alice")
print(greeter.greet())
print(greeter.greet("Hi"))
print(greeter.farewell())
print(f"Name length: {greeter.name_length}")
