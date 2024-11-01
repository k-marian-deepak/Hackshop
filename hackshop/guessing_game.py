import random

def get_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == "exit":
        print("Exiting the game.")
        exit()  # Exit the entire program
    return user_input

def get_validated_input(prompt, expected_type=int, default=None, allowed_values=None):
    while True:
        user_input = get_input(prompt)
        
        # If the input is empty and a default is provided, use the default
        if not user_input and default is not None:
            return default
        
        # Check for allowed values (like 'user' or 'computer' for game type)
        if allowed_values and user_input.lower() in allowed_values:
            return user_input.lower()
        
        # Check if input matches expected type (like an integer for range or tries)
        if expected_type == int:
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number or type 'exit' to quit.")
        else:
            print(f"Please enter one of the following options: {', '.join(allowed_values)} or type 'exit' to quit.")

def try_except():
    Length = get_validated_input(
        "Enter the Range of the number (To run default just press enter or type 'exit' to quit): ", 
        default=100
    )
    Range = list(range(0, Length + 1))
    random_num = random.choice(Range)
    return random_num

def guess_user(random_num, tries):
    for i in range(tries):
        user_guess_num = get_validated_input("Enter a number that you guess (or type 'exit' to quit): ")
        
        if user_guess_num == random_num:
            print("You guessed it right!!")
            break
        else:
            print("Better try next time!!")
    else:
        print("Out of tries! The correct number was:", random_num)

def guess_comp(random_num, tries):
    for i in range(tries):
        user_num = get_validated_input("Enter your number (or type 'exit' to quit): ")
        
        if random_num == user_num:
            print("The computer guessed it right, you lost!")
            break
        else:
            print("You won: Computer failed to guess your number!!")
    else:
        print("Out of tries! The correct number was:", random_num)

def guess_game():
    game_type = get_validated_input(
        "Choose game type (User/Computer) Guess (or type 'exit' to quit): ", 
        expected_type=str, 
        allowed_values=["user", "computer"]
    )
    tries = get_validated_input("Enter the number of tries (or type 'exit' to quit): ")

    random_num = try_except()  # Get random number from try_except()

    if game_type == "user":
        guess_user(random_num, tries)
    elif game_type == "computer":
        guess_comp(random_num, tries)

# Start the game
guess_game()