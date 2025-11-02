import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
        

class DiceGame:
    def __init__(self):
       self.die1 = Die()
       self.die2 = Die()
    
    def play_round(self):
       roll1 = self.die1.roll()
       roll2 = self.die2.roll()
       total = roll1 + roll2
       result = self.evaluate_roll(total)
       return {"die1": roll1, "die2": roll2, "total": total, "result": result}
    
    def evaluate_roll(self, total):
        if total in (7, 11):
            return "You win"
        elif total in (2, 3, 12):
            return "You lose"
        else:
            return "Please roll again"


def main():
    print("Welcome to the Dice Game Simulator!")
    game = DiceGame()

    while True:
        print("\nMenu:")
        print("1. Play a round!")
        print("2. Exit game")
        choice = input("Enter your choice here: ")   


        if choice == "1":
           outcome = game.play_round()
           print(f"\nYou have just rolled {outcome['die1']} and {outcome['die2']}.")
           print(f"Total: {outcome['total']}")
           print(f"Result: {outcome['result']}")
        elif choice == "2":
           print("Goodbye!")
           break
    
        else:
           print("Wrong choice! Please try again!")



if __name__ == "__main__":
    main()