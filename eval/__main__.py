"""
Runs simple baseline models, or evaluates sentence-aligned files
"""
import argparse

import evaluate
import model

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str, choices=["evaluate", "run"])
    args, _ = parser.parse_known_args()
    if args.command == "evaluate":
        parser = argparse.ArgumentParser()
        parser.add_argument("--file_original", type=str)
        parser.add_argument("--file_translated", type=str)
        args, _ = parser.parse_known_args()
        with open(args.file_original) as f1, open(args.file_translated) as f2:
            evaluate.print_summary(f1, f2)
    elif args.command == "run":
        parser = argparse.ArgumentParser()
        parser.add_argument("--model", default="word_replace", type=str, choices=["word_replace"])

if __name__ == "__main__":
    main()