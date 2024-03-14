from utils.data_handlers import generate_random_numbers


class User:
    """
    Class that tries to demonstrate various concepts
    behind the Object Oriented Programming.
    """
    name = "John"
    age  = 12
    salary = 125.67

    def __init__(self, genre, is_alive=True):
        self.genre = genre
        self.is_alive = is_alive

    def extra_init(self):
        self.country = "Norway"

    def get_information(self):
        print(f"The information of my user is: {self.name}, {self.age}, {self.salary}, {self.genre}, {self.is_alive}")

    def general_info(self):
        # Calling the `get_inforamtion` method through this method.
        self.get_information()

        # Calling the global function `generate_random_numbers` that is inside the `utils` module.
        print(f"The random number generated is: {generate_random_numbers()}")
        self.print_class_attributes()
    
    @classmethod
    def saying_hello(cls):
        print("Hello! 👋")

    @classmethod
    def print_class_attributes(cls):
        print(cls.name, cls.age, cls.salary)
        # cls.get_information()
        cls.saying_hello()


if __name__ == "__main__":
    # Statement that creates an `User` object.
    user = User(genre="Male")

    # Accessing to the attributes of the `User` instance/object.
    print(user.genre)
    print(user.age)

    # Changing the attribute age of the `User` instance/object.
    user.age = 30
    print(user.age)

    # Accessing the class attributes of the `User` class.
    print(User.salary)
    
    # Calling the methods defined inside the class.
    user.get_information()
    user.general_info()

    # Using a dictionary to define the arguments passed to the `User` class.
    user_data = {
        "genre": "No binary",
        "is_alive": False,
    }
    
    user = User(**user_data)
    user.general_info()

    # Calling a `classmethod` of the `User` class.
    User.print_class_attributes()
