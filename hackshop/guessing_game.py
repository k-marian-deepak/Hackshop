import random

# Checks if the user wants to exit or not
def exit_or_not(prompt):
    user_input = input(prompt)
    if user_input.lower() == "exit":
        print("Exiting the game...")
        exit()  # Exit the entire program
    return user_input 

# Checks if the input is valid or not
def valid_input_or_not(prompt, expected_type=int, default=None, allowed_values=None):
    while True:
        user_input = exit_or_not(prompt)

        # If input is empty and a default is provided, use the default: "range_()" -> satisfies
        if (not user_input) and (default is not None):
            return default

        # Check for allowed values (e.g., 'user' or 'computer' for game type): (Mode of the game) "guess_game()" -> Satisfies
        if allowed_values and user_input.lower() in allowed_values:
            return user_input.lower()

        # Check if input matches the expected type (e.g., integer for range or attempts): for "range_()" & "attmpts -> user-guess()" -> Satisfies
        if expected_type == int:
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number or type 'exit' to quit.")
        else:
            print(f"Please enter one of the following options: {', '.join(allowed_values)} or type 'exit' to quit.")

# The range of the number that the game will have 
def range_():
    global start, end  # Using both start and end as global variables
    start = valid_input_or_not("Enter the starting number of the range (or type 'exit' to quit): ", expected_type=int, default=0)
    end = valid_input_or_not("Enter the ending number of the range (or type 'exit' to quit): ", expected_type=int, default=100)

    if start > end:
        print("Invalid range! The start number must be less than or equal to the end number.")
        return range_()  # Retry if the range is invalid

    random_num = random.randint(start, end)
    return random_num  # The number the user tries to guess

# Computer guessing part: Binary Search
def binary_search():
    print(open("machine_guessing_mode.md").read())
    high = end  # Use 'end' as the upper limit for binary search
    low = start  # Use 'start' as the lower limit for binary search
    while True:
        mid = (low + high) // 2

        guess = input(f"Is {mid} the number you guessed (yes/no): ").lower()

        guess = exit_or_not(guess)

        if guess == "yes":
            print("Yay, I won!")
            break
        elif guess == "no":
            high_or_low = input(f"Is the number higher or lower than {mid} (high/low): ").lower()

            guess = exit_or_not(guess)

            if high_or_low == "high":
                low = mid + 1
            elif high_or_low == "low":
                high = mid - 1
            else:
                print("Invalid input, please type 'high' or 'low'.")
        else:
            print("Invalid input, please type 'high' or 'low'.")

# User Guessing part
def user_guess(random_num, attempts):
    print(open("user_guessing_mode.md").read())
    for i in range(attempts):
        user_guess_num = valid_input_or_not("Enter a number that you guess (or type 'exit' to quit): ")

        if user_guess_num == random_num:
            print("You guessed it right!!")
            break
        else:
            print("Better try next time!")
    else:
        print("Out of tries! The correct number was:", random_num)

# Main function to initiate the game
def guess_game():
    game_type = valid_input_or_not("Choose game type (User/Computer) Guess (or type 'exit' to quit): ", expected_type=str, allowed_values=["user", "computer"])

    if game_type == "user":
        attempts = valid_input_or_not("Enter the number of tries (or type 'exit' to quit): ", expected_type=int)
        random_num = range_()  # Get random number from range_()
        user_guess(random_num, attempts)

    elif game_type == "computer":
        range_()  # Sets start and end for binary search
        binary_search()  # Computer performs binary search until it finds the correct number

# Start the game
guess_game()