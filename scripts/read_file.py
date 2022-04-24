import argparse
import csv


def handle_args():
    """Handle arguments for script."""
    parser = argparse.ArgumentParser(description="Sum values in CSV.")
    parser.add_argument("path", help="Path to CSV file.")
    parser.add_argument("col", help="Name of column to sum values of.")

    return parser.parse_args()


def main():
    "Entry point to script."
    args = handle_args()
    total = 0
    with open(args.path) as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            print(row[args.col])
            total += int(row[args.col])

    print(f"Total: {total}")


if __name__ == "__main__":
    main()
