def parse_input(input_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    k = int(lines[0])

    alphabet = {}
    for i in range(1, k + 1):
        letter, weight = lines[i].split()
        alphabet[letter] = int(weight)

    first_string = lines[k + 1]
    second_string = lines[k + 2]

    return k, alphabet, first_string, second_string


def hvlcs(a, b, values):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + values[a[i - 1]]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # backtrack to reconstruct the subsequence
    subseq = []
    i, j = m, n
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            subseq.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    subseq.reverse()
    return dp[m][n], ''.join(subseq)
