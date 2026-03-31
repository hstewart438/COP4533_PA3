def parse_input(input_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    # total number of letters in alphabet
    k = int(lines[0])

    # dictionary -> letter: weight
    alphabet = {}

    # load alphabet values
    for i in range(1, k+1):
        letter, weight = lines[i].split()
        alphabet[letter] = int(weight)

    # get two strings
    first_string = lines[-2]
    second_string = lines[-1]

    return k, alphabet, first_string, second_string
