import random
import argparse
import warnings
import os
import time
from getkey import getkey, key
from cli_game.commons import pickle_to_list


def get_answer():
    choice = input()
    if (not choice.isdigit()) or int(choice) > 4:
        print("Please make sure to answer with a number between 1 and 4...\n")
        get_answer()
    return int(choice)


def play_round(real_fishes, made_up_fishes):
    actual_fishes = random.sample(real_fishes, k=3)

    finte = random.sample(made_up_fishes, k=1)[0]

    options = actual_fishes + [finte]
    random.shuffle(options)

    correct_answer = options.index(finte) + 1

    print(
        "\nTippe die Zahl neben dem Fisch an, von dem du denkst, dass die Art erfunden ist:\n"
    )
    for i, option in enumerate(options):
        print(f"{i+1}: {option}")

    answer = get_answer()
    if answer == correct_answer:
        time.sleep(0.25)
        print(f"Du hast mit {options[answer-1]} geantwortet. Das war richtig! Juhu!")

        return 1
    else:
        time.sleep(0.25)
        print(f"Du hast mit {options[answer-1]} geantwortet. Das war leider falsch :(")

        return 0


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--real_fish_data", default="data/real_fish.pickle")
    args = parser.parse_args()

    if not os.path.exists(args.real_fish_data):
        warnings.warn(
            f"The specified file {args.real_fish_data} does not exists... Please make sure to enter a valid filename..."
        )

    real_fishes = pickle_to_list(args.real_fish_data)
    made_up_fishes = pickle_to_list("data/made_up_fish.pickle")
    points = 0

    rounds_counter = 0
    try:
        while True:
            rounds_counter += 1
            points += play_round(real_fishes, made_up_fishes)
            print(f"Du hast insgesamt {points} Punkte\n")
            print(
                "Druecke 'Enter' um weiterzuspielen oder eine beliebige andere Taste um das Spiel zu beenden."
            )
            key_pressed = getkey()
            if key_pressed != key.ENTER:
                print("-" * 50)
                print(
                    f"Das Spiel wurde beendet. Du hast in {rounds_counter} Runde insgesamt {points} erreicht."
                )
                print(f"Dein Score ist {(points / rounds_counter)*100:.2f} %")
                break
            print("-" * 50)
    except KeyboardInterrupt:
        pass
