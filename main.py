import argparse
import random

with open("adjectives.txt", "r") as f:
    adjectives = [line.removesuffix("\n") for line in f.readlines()]

with open("nouns.txt", "r") as f:
    nouns = [line.removesuffix("\n") for line in f.readlines()]

with open("names.txt", "r") as f:
    names = [line.removesuffix("\n") for line in f.readlines()]

argparser = argparse.ArgumentParser(description="Generate a random safe username")
argparser.add_argument(
    "--num", type=int, default=1, action="store", help="number of usernames to generate"
)
args = argparser.parse_args()

for x in range(0, args.num):
    if random.randint(1, 5) != 1:
        print(
            adjectives[random.randint(0, len(adjectives) - 1)]
            + nouns[random.randint(0, len(nouns) - 1)]
            + str(random.randint(100, 999))
        )
    else:
        print(
            names[random.randint(0, len(names) - 1)]
            + nouns[random.randint(0, len(nouns) - 1)]
            + str(random.randint(100, 999))
        )
