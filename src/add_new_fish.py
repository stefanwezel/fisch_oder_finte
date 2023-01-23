import os
import argparse
from commons import list_to_pickle, pickle_to_list, fish_in_list



def add_new_fish(name, made_up, real_fish_path="../data/real_fish.pickle",made_up_fish_path="../data/made_up_fish.pickle"):
    real_fish = pickle_to_list(real_fish_path)
    made_up_fish = pickle_to_list(made_up_fish_path)

    saved_fish = fish_in_list(name, real_fish)
    already_saved = True if len(saved_fish) > 0 else False
    print(already_saved)
    print(made_up)
    if already_saved and made_up:
        print(f"The name you suggested or a similar ones ({saved_fish}) acutally exists. Exiting...")
        return None
    elif already_saved and (not made_up):
        print(f"The name you suggested or a similar ones ({saved_fish}) is/are already saved in {real_fish_path}. Exiting...")
        return None

    elif (not already_saved) and made_up:
        made_up_fish.append(name.capitalize())
        print(f"Saving you suggested fish {name} to {made_up_fish_path}")
        list_to_pickle(made_up_fish, made_up_fish_path)
        return None

    elif (not already_saved) and (not made_up):
        real_fish.append(name.capitalize())
        print(f"Saving you suggested fish {name} to {real_fish_path}")
        # list_to_pickle(real_fish, real_fish_path)
        return None



parser = argparse.ArgumentParser()
parser.add_argument('--name')
parser.add_argument('--madeup', action='store_true')  # on/off flag
parser.add_argument('--real', action='store_true')  # on/off flag

args = parser.parse_args()

made_up = args.madeup
suggested_name = args.name

add_new_fish(args.name, made_up)


# all_made_up_fish = pickle_to_list("../data/made_up_fish.pickle")
print(all_made_up_fish)