import streamlit as st
import random

# Global variables to store range, attempts, and state
start, end = 0, 100
random_num = None
attempt_count = 0
seen_guesses = set()

# Initialize Streamlit session state variables
if 'random_num' not in st.session_state:
    st.session_state.random_num = None
if 'start' not in st.session_state:
    st.session_state.start = 0
if 'end' not in st.session_state:
    st.session_state.end = 100
if 'attempt_count' not in st.session_state:
    st.session_state.attempt_count = 0
if 'seen_guesses' not in st.session_state:
    st.session_state.seen_guesses = set()

# Function to handle the range input
def set_range():
    st.session_state.start = st.number_input("Enter the starting number of the range:", min_value=0, value=0)
    st.session_state.end = st.number_input("Enter the ending number of the range:", min_value=st.session_state.start+1, value=100)

    if st.session_state.start < st.session_state.end:
        st.session_state.random_num = random.randint(st.session_state.start, st.session_state.end)
        st.write("Range set successfully!")
    else:
        st.write("Invalid range! The start number must be less than the end number.")

# User guessing function
def user_guess_game():
    attempts = st.number_input("Enter the number of attempts:", min_value=1, value=5)
    if st.session_state.random_num is None:
        set_range()

    user_guess_num = st.number_input("Enter your guess:", min_value=st.session_state.start, max_value=st.session_state.end)

    if st.button("Submit Guess"):
        if user_guess_num == st.session_state.random_num:
            st.write("You guessed it right!")
        elif user_guess_num < st.session_state.random_num:
            st.write("Try a higher number.")
        else:
            st.write("Try a lower number.")
        st.session_state.attempt_count += 1

        if st.session_state.attempt_count >= attempts:
            st.write(f"Out of attempts! The correct number was: {st.session_state.random_num}")
            st.session_state.attempt_count = 0  # Reset for a new game

# Computer guessing function (Binary search or random)
def computer_guess_game():
    if st.session_state.random_num is None:
        set_range()

    attempts = st.number_input("Enter attempts for binary search (or 0 for random guessing):", min_value=0, value=5)

    if attempts > 0:
        # Binary search
        high, low = st.session_state.end, st.session_state.start
        for attempt in range(attempts):
            mid = (low + high) // 2
            guess_response = st.selectbox(f"Is {mid} the number?", ["", "yes", "no"])
            if guess_response == "yes":
                st.write(f"Computer guessed it in {attempt + 1} attempts!")
                break
            elif guess_response == "no":
                high_or_low = st.selectbox("Is the number higher or lower?", ["", "higher", "lower"])
                if high_or_low == "higher":
                    low = mid + 1
                elif high_or_low == "lower":
                    high = mid - 1
        else:
            st.write("Out of attempts or range exhausted.")
    else:
        # Random guessing
        while True:
            guess = random.randint(st.session_state.start, st.session_state.end)
            if guess in st.session_state.seen_guesses:
                continue
            st.session_state.seen_guesses.add(guess)
            user_feedback = st.selectbox(f"Is {guess} your number?", ["", "yes", "no"])
            if user_feedback == "yes":
                st.write(f"Computer guessed the number in {len(st.session_state.seen_guesses)} attempts!")
                break
            elif user_feedback == "no":
                high_or_low = st.selectbox("Is the number higher or lower?", ["", "higher", "lower"])
                if high_or_low == "higher":
                    st.session_state.start = guess + 1
                elif high_or_low == "lower":
                    st.session_state.end = guess - 1

# Main function for the game
def guess_game():
    st.title("Number Guessing Game")

    game_type = st.radio("Choose game type", ["User Guess", "Computer Guess"])

    if game_type == "User Guess":
        user_guess_game()
    elif game_type == "Computer Guess":
        computer_guess_game()

# Run the game
guess_game()