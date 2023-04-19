import random


class Character:
    char_list = []
    char_classes = ["Warrior", "Wizard", "Potato"]

    def __init__(self, char_name):
        self.char_name = char_name
        self.char_class = Character.char_classes[random.randint(0, 2)]
        self.strength = random.randint(5, 10)
        self.magic = random.randint(5, 10)
        self.health = random.randint(5, 10)

        if self.char_class == Character.char_classes[0]:
            self.strength *= 3
        elif self.char_class == Character.char_classes[1]:
            self.magic *= 3
        elif self.char_class == Character.char_classes[2]:
            self.health *= 3

        Character.char_list.append(self)


# -----------------------------------------------------------


print("Welcome to the character generator, you name 'em we make 'em!")
print("Let's start by naming em!")
char1 = Character(input("Char1 name: "))
char2 = Character(input("Char2 name: "))
char3 = Character(input("Char3 name: "))
char4 = Character(input("Char4 name: "))
char5 = Character(input("Char5 name: "))

print("YOUR CHARACTERS ARE COMPLETE")

# I want to print the created characters all at the same time
for char in Character.char_list:
    print(
        f'"{char.char_name}" is a {char.char_class}!\n    Strength: {char.strength}\n    Magic: {char.magic}\n    Health: {char.health}\n'
    )
    #  how do I make double quotes work inside a string? need to use / somehow

print("Try to not get your characters killed. No pressure :D")

# TODO all there's left is to complete the optional bonus challenge
