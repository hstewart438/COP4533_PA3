import sys
import os
from opt import parse_input, hvlcs

def main():
    if len(sys.argv) <= 1:
        print("Please name a test file to run.")
        sys.exit(1)

    file_path = sys.argv[1]
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    try:
        k, alphabet, first_string, second_string = parse_input(file_path)
    except FileNotFoundError:
        print(f"Could not find {file_name} within 'tests' folder")
        sys.exit(1)

    max_value, subsequence = hvlcs(first_string, second_string, alphabet)

    print(max_value)
    print(subsequence)

    outfile = os.path.join("data", f"{file_name}.out")
    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    with open(outfile, 'w') as f:
        f.write(f"{max_value}\n")
        f.write(f"{subsequence}\n")


if __name__ == "__main__":
    main()