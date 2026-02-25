# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans):
    while True:

        # Get user response and amke sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:

            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif question == item[0]:
                return item


# Main routine

yes_no = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]
want_instructions
