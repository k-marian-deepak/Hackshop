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

        # If input is empty and a default is provided, use the default
        if (not user_input) and (default is not None):
            return default

        # Check for allowed values
        if allowed_values and user_input.lower() in allowed_values:
            return user_input.lower()

        # Check if input matches the expected type (e.g., integer for range or attempts)
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

def binary_search(attempts):
    high = end
    low = start
    attempt_count = 0
    while low <= high and attempt_count < attempts:
        print("Attempt count:", attempt_count + 1)
        mid = (low + high) // 2
        guess = valid_input_or_not(f"Is {mid} the number you guessed (yes/no): ", expected_type=str, allowed_values=["yes", "no"])
        attempt_count += 1

        if guess == "yes":
            print(f"Yay, I won in {attempt_count} attempts!")
            break
        elif guess == "no":
            high_or_low = valid_input_or_not(f"Is the number higher or lower than {mid} (high/low): ", expected_type=str, allowed_values=["high", "low"])

            if high_or_low == "high":
                low = mid + 1
            elif high_or_low == "low":
                high = mid - 1
    else:
        if attempt_count >= attempts:
            print("Out of attempts!")
        elif low > high:
            print("The range was exhausted! The number could not be guessed.")

# Random guessing method
def random_guessing():
    global start, end  # Declare start and end as global to modify them here
    seen = set()
    attempts = 0
    while True:
        guess = random.randint(start, end)
        if guess in seen:
            continue  # Skip already guessed numbers
        seen.add(guess)

        print(f"Computer guesses: {guess}")
        user_response = valid_input_or_not(f"Is {guess} your number? (yes/no): ", expected_type=str, allowed_values=["yes", "no"])
        attempts += 1

        if user_response == "yes":
            print(f"Computer found the number in {attempts} tries!")
            break
        elif user_response == "no":
            high_or_low = valid_input_or_not("Is the number higher or lower than this guess? (high/low): ", expected_type=str, allowed_values=["high", "low"])

            if high_or_low == "high":
                start = guess + 1
            elif high_or_low == "low":
                end = guess - 1

# User Guessing part
def user_guess(random_num, attempts):
    for i in range(attempts):
        user_guess_num = valid_input_or_not("Enter a number that you guess (or type 'exit' to quit): ", expected_type=int)

        if user_guess_num not in range(start, end + 1):
            print(f"The number you guessed is out of range. \nGuesses left: {attempts - i - 1}")
            continue  # Skip the rest of the loop if out of range
        
        if user_guess_num == random_num:
            print("You guessed it right!")
            break
        elif user_guess_num < random_num:
            print(f"Try a higher number. \nGuesses left: {attempts - i - 1}")
        else:
            print(f"Try a lower number. \nGuesses left: {attempts - i - 1}")
    else:
        print("Out of tries! The correct number was:", random_num)

# Main function to initiate the game
def guess_game():
    game_type = valid_input_or_not("Choose game type (User/Computer) Guess (or type 'exit' to quit): ", expected_type=str, allowed_values=["user", "computer"])

    if game_type == "user":
        attempts = valid_input_or_not("Enter the number of tries (or type 'exit' to quit): ", expected_type=int)
        random_num = range_()
        user_guess(random_num, attempts)

    elif game_type == "computer":
        attempts = valid_input_or_not("Would you like the computer to use optimal attempts? (Enter number of tries or type 'no' for random guessing): ", expected_type=int, default="no")
        range_()

        if isinstance(attempts, int):
            binary_search(attempts)
        else:
            random_guessing()

# Start the game
while True:
    guess_game()