logo = """

    ,.                 .                ,_           
   / |   ,-. ,-.   ,-. |  ,-. ,-. ,-. . |_ . ,-. ,-. 
  /~~|-. | | |-'   |   |  ,-| `-. `-. | |  | |-' |   
,'   `-' `-| `-'   `-' `' `-^ `-' `-' ' |  ' `-' '   
          ,|                            '            
          `'                                        

"""
print(logo)

import random

class AgeClassifier:
    def __init__(self):
        self.age_groups = {
            "child": (0, 12),
            "teenager": (13, 19),
            "adult": (20, 64),
            "senior citizen": (65, float('inf'))
        }

    def get_age_group(self, age):
        for group, (min_age, max_age) in self.age_groups.items():
            if min_age <= age <= max_age:
                return group
        return "Invalid age"

    def classify_age(self):
        while True:
            try:
                age = int(input("Enter your age: "))
                age_group = self.get_age_group(age)
                print(f"You are a {age_group}")
                break
            except ValueError:
                print("Invalid input. Please enter a valid age.")

    def generate_random_age(self):
        return random.randint(0, 100)

    def play_age_guessing_game(self):
        print("Welcome to the age guessing game!")
        age_to_guess = self.generate_random_age()
        while True:
            try:
                guess = int(input("Guess my age: "))
                if guess < age_to_guess:
                    print("Too low!")
                elif guess > age_to_guess:
                    print("Too high!")
                else:
                    print("Congratulations! You guessed my age correctly.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid age.")

def main():
    classifier = AgeClassifier()
    while True:
        print("\nAge Classifier Menu:")
        print("1. Classify your age")
        print("2. Play age guessing game")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            classifier.classify_age()
        elif choice == "2":
            classifier.play_age_guessing_game()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()