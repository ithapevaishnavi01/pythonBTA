import random

def game():
    print("You are playing the game...")

    score = random.randint(1, 62)

    # Fetch the high score
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    if highscore != "":
        highscore = int(highscore)
    else:
        highscore = 0

    print(f"Your score is {score}")

    # Check if new score is higher
    if score > highscore:
        print("New high score!")

        # Write new high score to file
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score


game()