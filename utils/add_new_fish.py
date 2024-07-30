import os
import argparse
from utils import list_to_pickle, pickle_to_list, fish_in_list, check_answer
from dotenv import find_dotenv, load_dotenv
import pandas as pd
import sys

ENV_FILE = find_dotenv(".env")
if ENV_FILE:
    load_dotenv(ENV_FILE)


def add_new_fish(
    name,
    real,
):

    fish_df = pd.read_csv(os.path.join("..", os.getenv("FISH_CSV")), index_col=0)

    real_fish = fish_df[fish_df["real"] == "True"]["name"].to_list()
    made_up_fish = fish_df[fish_df["real"] == "False"]["name"].to_list()

    real_similar_fish = fish_in_list(name, real_fish)
    madeup_similar_fish = fish_in_list(name, made_up_fish)

    if not real and len(real_similar_fish) > 0:
        print(
            f"The name you suggested or a similar ones ({real_similar_fish}) acutally exists. Exiting..."
        )
        sys.exit(1)
    elif real and len(real_similar_fish) > 0:
        print(
            f"The name you suggested or a similar ones ({real_similar_fish}) is already in the list. Exiting..."
        )
        sys.exit(1)
    elif real and len(madeup_similar_fish) > 0:
        print(
            f"The name you suggested or similar ones ({madeup_similar_fish}) have already been saved as made-up fish. Exiting..."
        )
        sys.exit(1)
    elif not real and len(madeup_similar_fish) > 0:
        print(
            f"The name you suggested or similar ones ({madeup_similar_fish}) have already been saved as made-up fish. Exiting..."
        )
        sys.exit(1)
    else:
        print(f"Adding new fish {name}")
        new_row = pd.DataFrame(
            {
                "name": [name],
                "real": [real],
            }
        )
        fish_df = pd.concat(
            [
                fish_df,
                new_row,
            ],
            ignore_index=True,
        )
        fish_df.to_csv(os.path.join("..", os.getenv("FISH_CSV")))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--name",
        help="Name of the fish you would like to add. Indice whether its real or made-up setting on of the the boolean flags `--real` or `--madeup`.",
    )
    parser.add_argument(
        "--real",
        action="store_true",
        help="Boolean flag to indicate whether a fish is real. Cannot be used in conjunction with `--madup`.",
    )  # on/off flag
    parser.add_argument(
        "--madeup",
        action="store_true",
        help="Boolean flag to indicate whether a fish is made-up. Cannot be used in conjunction with `--real`.",
    )  # on/off flag

    args = parser.parse_args()

    real = args.real
    made_up = args.madeup

    assert not (
        real and made_up
    ), "Please choose either `--real` or `--madeup` as flag. ⚠️"

    if real:
        add_new_fish(args.name, "True")
    else:
        add_new_fish(args.name, "False")
