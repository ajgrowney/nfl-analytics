import json
from argparse import ArgumentParser

def convert_odds_to_prob(odds):
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return -odds / (-odds + 100)

def convert_odds_to_probs(odds_over, odds_under):
    
    over_prob = convert_odds_to_prob(odds_over)
    under_prob = convert_odds_to_prob(odds_under)
    vig = (over_prob + under_prob) - 1
    return (over_prob - (0.5 * vig), under_prob - (0.5 * vig))

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-t", "--team", help="Team")
    parser.add_argument("-s", "--start", help="Start Points")
    parser.add_argument("-e", "--end", help="End Points")
    parser.add_argument("-f", "--file", help="File")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        data = json.load(f)
    data[args.team] = {}
    c = float(args.start)
    while c <= float(args.end):
        odds_over = int(input(f"O {c}:"))
        odds_under = int(input(f"U {c}:"))
        data[args.team][str(c)] = convert_odds_to_probs(odds_over, odds_under)
        c += 1

    with open(args.file, "w") as f:
        json.dump(data, f, indent=4)