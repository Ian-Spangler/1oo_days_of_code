def greet():
    print("Hello Ian")
    print("How are you doing?")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you doing {name}?")

greet_with_name("Ian")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Ian", "Seoul")
greet_with(location = "Seoul", name = "Ian")