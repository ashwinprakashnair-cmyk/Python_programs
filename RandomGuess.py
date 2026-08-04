import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("Select Difficulty:\n1. Easy (1-50, 10 guesses)\n2. Medium (1-100, 7 guesses)\n3. Hard (1-200, 5 guesses)")

     while True:
        choice = input("Enter choice (1, 2, or 3): ").strip()
        if choice == '1':
            max_num, max_attempts = 50, 10
            break
        elif choice == '2':
            max_num, max_attempts = 100, 7
            break
        elif choice == '3':
            max_num, max_attempts = 200, 5
            break
        print("❌ Invalid choice. Please enter 1, 2, or 3.")

    print(f"\nI am thinking of a number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts to guess it.")
    
    secret_number = random.randint(1, max_num)
    attempts = 0
    
    while attempts < max_attempts:
        try:
            print(f"\n[Attempt {attempts + 1}/{max_attempts}]")
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                return
                
        except ValueError:
            print("❌ Invalid input. Please enter a valid whole number.")
            
    print(f"\n💥 Game Over! You ran out of guesses. The number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()  

