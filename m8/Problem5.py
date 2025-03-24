# Haseeb
# Date: 3/23/25
# Problem 5: Check items for game character tasks

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

# Create player
player1 = character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])

def check_tasks(player):
    items = player.weapons
    debuffs = player.weaknesses

    # Task 1
    print("Checking Task 1: Climb a mountain")
    if all(x in items for x in ['rope', 'coat', 'first aid kit']) and 'slow' not in debuffs:
        print("Task 1: Ready to climb the mountain.")
    else:
        print("Task 1: Cannot climb the mountain.")

    # Task 2
    print("Checking Task 2: Cook a meal")
    if all(x in items for x in ['pan', 'groceries']) and 'small' not in debuffs:
        print("Task 2: Ready to cook a meal.")
    else:
        print("Task 2: Cannot cook a meal.")

    # Task 3
    print("Checking Task 3: Write a book")
    if all(x in items for x in ['pen', 'paper', 'idea']) and 'confusion' not in debuffs:
        print("Task 3: Ready to write a book.")
    else:
        print("Task 3: Cannot write a book.")

check_tasks(player1)
