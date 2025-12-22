#Create a class with PRIVATE fields, private method and a main method. Print the fields 
in main method. Call the private method in main method.
class PrivateExample:
    def __init__(self):
        self.__private_field = "I am Private Field"

    def __private_method(self):
        print("Private Method Called")

    @staticmethod
    def main():
        obj = PrivateExample()

        # Accessing private field (inside same class)
        print(obj.__private_field)

        # Calling private method (inside same class)
        obj.__private_method()


# Running main method
PrivateExample.main()


# Subclass trying to access PRIVATE members
class ChildPrivate(PrivateExample):
    def access_private(self):
        # These will raise AttributeError
        # print(self.__private_field)
        # self.__private_method()
        print("Cannot access private members in subclass")

