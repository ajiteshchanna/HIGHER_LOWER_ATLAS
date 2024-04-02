from art import logo_atlas, vs
from atlas import data
import random
import os


clear = lambda: os.system('cls')


def print_header(A, B, score):
    print(logo_atlas)
    if score > 0:
        print(f"You are Right!: Your Score is {score}")
    print(f"Compare A: {A['name']}")
    print(vs)
    print(f"Against B: {B['name']}")


def game():
    curr_score = 0
    A = random.choice(data)
    B = random.choice(data)
    game_is_on = True
    while game_is_on:
        print_header(A, B, curr_score)
        user = input("Which country has more population? Type 'A' or 'B': ")
        ans = "A" if A['population'] >= B['population'] else "B"
        if user == ans:
            curr_score += 1
            if user == "A":  # means our A had more followers
                A = B
                B = random.choice(data)
            else:  # means our B had more followers
                B = random.choice(data)
                clear()
        else:
            game_is_on = False
            print("Sorry, You are Wrong, GAME OVER💀")
            # updating the high score
            with open("highscore.txt", mode="r") as file:
                high_score = file.read()
                if high_score == '':
                    high_score=0
                if int(high_score) < curr_score:
                    high_score = curr_score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{high_score}")
            print(f"YOUR SCORE: {curr_score} \nHIGH SCORE: {high_score}")

    again = input("Do you want to play again? Type 'y' for yes, 'n' for no: ")
    if again.lower() == 'y':
        clear()
        game()
    else:
        clear()
        return


game()
