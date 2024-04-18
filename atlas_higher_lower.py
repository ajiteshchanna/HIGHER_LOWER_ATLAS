from art import logo_atlas, vs
from atlas import data
import os
import random
import time
import pandas

clear = lambda: os.system('cls')
appeard_countries = []


# create a print header function to print header for each of the turn
def print_header(A, B, score):
    print(logo_atlas)
    if score > 0:
        print(f"You are right✅: Current Score = {score}")
    print(f"Compare A: {A['name']}")
    print(vs)
    print(f"Against B: {B['name']}")


# create a function play again
def play_again():
    again = input("Type 'y' to play again and 'n' to exit the game: ")
    if again.lower() == 'y':
        return True
    elif again.lower() == 'n':
        return False
    else:
        print("INVALID INPUT, TRY AGAIN.")
        play_again()


# game function which allows the user to play the game
def game():
    # create a current_score variable
    current_score = 0

    # take name as input and store it in a variable called name
    user_name = input("Enter your name: ")
    clear()

    # random choice of countries A and B
    A = random.choice(data)
    B = random.choice(data)

    # if A == B the computer should choose again
    while A == B:  # so now no two same countries will be shown
        B = random.choice(data)
    game_is_on = True

    # then it should print the welcome message
    print(f"Hi {user_name}, welcome to the: ")
    while game_is_on:
        # printing the header
        print_header(A, B, score=current_score)

        # taking choice from the user 
        user_choice = input("Which country has higher population? 'A' or 'B': ")
        answer = "A" if A['population'] > B['population'] else "B"

        # if the user is correct
        if user_choice.upper() == answer:
            appeard_countries.append(A['name'])
            appeard_countries.append(B['name'])
            current_score += 1

            if user_choice == "A":  # means our A had more followers
                A = B
                B = random.choice(data)
                while B['name'] in appeard_countries:
                    B = random.choice(data)

            else:  # means our B had more followers
                B = random.choice(data)
                while B['name'] in appeard_countries:
                    B = random.choice(data)
            clear()

        # the user is wrong, but not invalid
        elif user_choice != answer and (user_choice == "A" or user_choice == "B"):
            game_is_on = False
            print("Sorry, You are wrong. GAME OVER💀")

            # reading the high score
            high_score = pandas.read_csv('highscore.csv')
            names = []
            score = []
            for index, row in high_score.iterrows():
                names.append(row['name'])
                score.append(row['score'])

            # checking whether the user is now or has played earlier
            if user_name in names:
                prev_score = score[names.index(user_name)]
                if current_score > prev_score:
                    prev_score = current_score
                    score[names.index(user_name)] = prev_score
                your_high_score = prev_score

                # saving the user's score
                high_score.loc[high_score['name'] == user_name, 'score'] = your_high_score
                high_score.to_csv('highscore.csv', index=False)
            else:
                names.append(user_name)
                score.append(current_score)
                your_high_score = current_score

                new_score_data = {'name': user_name,
                                  'score': your_high_score}

                # creating a data frame
                new_player = pandas.DataFrame({'name': [user_name], 'score': [your_high_score]}, index=[0])
                high_score = high_score._append(new_player, ignore_index=True)
                high_score.to_csv('highscore.csv', index=False)

            # now finding the highscore
            highscore_score = max(score)
            high_score_player = names[score.index(highscore_score)]

            print(f"Your Score: {current_score}")
            print(f"Your HighScore: {your_high_score}")
            print(f"Overall HighScore-> {high_score_player} : {highscore_score}")

            # asking if the user wants to play the game again or not
            again = play_again()
            if again:
                clear()
                game()
            else:
                print("Thank you for playing the Higher Lower Atlas Game🌏.")
                return
        else:
            print("Invalid Input! Try again")
            time.sleep(1.5)  # letting the INVALID INPUT MESSAGE TO DISPLAY FOR SOME TIME


game()
