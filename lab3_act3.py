class Character:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __init__(self):
        self.input_string = input("Input a string: ")
        self.convert_vowels()

    def convert_vowels(self):
        result = ''.join([char.upper() if char in self.vowels else char for char in self.input_string])
        print(result)

# Create an instance of the class to run the program
Character()
