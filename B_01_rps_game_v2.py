import random

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and amke sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list

            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

# Display instructions
def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

To begin, choose the number of rounds (or press <enter> for
infinite mode).

Then play against the computer. You need to choose R (rock),
P (paper) or S (scissors).

The rules are as follows:
- Paper beats rock
- Rock beats scissors
- Scissors beats paper

Press <xxx> to end the game at the game at anytime.

Good luck!!!🍀
    """)


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    """Checks users enter an integer more than / equal to 1"""
    while True:
        error = "Please enter an integer more than / equal to 1"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"


        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# compare user / computer choice and returns
# result (win/ lose/ tie)
def rps_compare(user, comp):

    if user == comp:
        round_result = "tie"

    elif user == 'paper' and comp == 'rock':
        round_result = 'win'
    elif user == 'scissors' and comp == 'paper':
        round_result = 'win'
    elif user == 'rock' and comp == 'scissors':
        round_result = 'win'

    else:
        round_result = "lose"

    return round_result


# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("🪨📄✂️  Rock / Paper / Scissors Game ✂️📄🪨")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("Do you want to see the instructions? ")

#Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾♾♾ Round {rounds_played + 1} (Infinite Mode)♾♾♾"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # Adjust game lost / game tied counters and add results to game history
    if result == "tie":
        rounds_tied += 1
        feedback = "👔👔 It's a tie!! 👔👔"
    elif result == "lose":
        rounds_lost += 1
        feedback = "😢😢 Awh shucks! You lose! 😢😢"
    else:
        feedback = "🙌HUZZAH! YOU'VE WON!🙌"

    # Set up round feedback and output it user_choice
    # Add it to the game history list (include the round number)
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)


    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game History / Statistics area

if rounds_played > 0:
    # Calculate Statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output Game Statistics
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"🙌 Won: {percent_won:.2f} \t"
          f"😢 Lost: {percent_lost:.2f} \t"
          f"👔 Tied: {percent_tied:.2f}")

    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

print()
print("Thanks for playing")