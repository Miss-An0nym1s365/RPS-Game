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

# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

print("🪨📄✂️  Rock / Paper / Scissors Game ✂️📄🪨")
print()

# Instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    print("You chose infinite!♾️")
    num_rounds = 5
# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("rounds played", rounds_played)

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    print("num rounds: ", num_rounds)

# Game loop ends here

# Game History / Statistics area