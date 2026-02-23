import random
import os

if not os.path.exists("completions.txt"):
    open("completions.txt", "w").close()

class ListTracker:

    def __init__(self):
        self.isaac_characters = [
            # Base Characters
            "Isaac",
            "Magdalene",
            "Cain",
            "Judas",
            "??? (Blue Baby)",
            "Eve",
            "Samson",
            "Azazel",
            "Lazarus",
            "Eden",
            "The Lost",
            "Lilith",
            "Keeper",
            "Apollyon",
            "The Forgotten",
            "Bethany",
            "Jacob and Esau",

            # Tainted Characters
            "Tainted Isaac",
            "Tainted Magdalene",
            "Tainted Cain",
            "Tainted Judas",
            "Tainted ??? (Blue Baby)",
            "Tainted Eve",
            "Tainted Samson",
            "Tainted Azazel",
            "Tainted Lazarus",
            "Tainted Eden",
            "Tainted Lost",
            "Tainted Lilith",
            "Tainted Keeper",
            "Tainted Apollyon",
            "Tainted Forgotten",
            "Tainted Bethany",
            "Tainted Jacob"
        ]
        self.completion_mark_bosses = [
            "Blue Baby",
            "The Lamb",
            "Mega Satan",
            "Boss Rush",
            "Hush",
            "Delirium",
            "Mother",
            "The Beast",
            "Greedier"
        ]

    def gen_rand_run(self):
        valid_run = False

        with open("completions.txt", "r") as file:
            completed_runs = set(line.strip() for line in file)

        while not valid_run:
            valid_run = True
            rand_char = random.randint(0, len(self.isaac_characters) - 1)
            rand_mark = random.randint(0, len(self.completion_mark_bosses) - 1)
            run_plan = f"{self.isaac_characters[rand_char]}, {self.completion_mark_bosses[rand_mark]}"

            if run_plan in completed_runs:
                if len(completed_runs) == len(self.isaac_characters) * len(self.completion_mark_bosses):
                    print("All Runs Completed!")
                    return None

                print("Discarded Run Plan.")
                valid_run = False

        return run_plan

    def record_run(self, run_plan):
        run_plan_split = run_plan.split(", ")
        print(f"Next run, try to beat {run_plan_split[1]} as {run_plan_split[0]}.")

        if input("Did you succeed? Type y/n: ").lower() == "y":
            with open("completions.txt", "a") as file:
                file.write(run_plan + "\n")

        if input("Result Saved! Would you like to start another run? Type y/n: ").lower() == "n":
            return False

        return True

    def main(self):
        run = True
        while run:
            run_plan = self.gen_rand_run()
            if not run_plan:
                break
            run = self.record_run(run_plan)

isaac_list = ListTracker()
isaac_list.main()