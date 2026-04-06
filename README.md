# Highest Value Longest Common Subsequence (HVLCS)

Implementation of the HVLCS algorithm using dynamic programming.

**Authors:** Hari-Krishna Patel (UFID: 89949738), Hunter Stewart (UFID: 43812980)

## Input Format

**Input file type:** Input files must use the **`.in`** extension (e.g., `example.in`, `1.in`, etc). Input file must contain K (number of characters in the alphabet), K lines of character-value pairs, and two strings A and B.

**Structure:**

```
K
x1 v1
x2 v2
...
xK vK
A
B
```

| Field    | Description                                                              |
| -------- | ------------------------------------------------------------------------ |
| `K`      | Number of distinct characters in the alphabet                            |
| `xi vi`  | Character and its positive integer value (space-separated, one per line) |
| `A`      | First string                                                             |
| `B`      | Second string                                                            |

See `tests/example.in` for reference.

## Output Format

Prints the maximum subsequence value on the first line and the reconstructed subsequence on the second line. Output is also written to `data/<filename>.out`.

```
<max_value>
<subsequence>
```

## How to Run

On macOS, the Python 3 interpreter is usually available as `python3`.
On many Linux/Windows setups, or if you've configured your system so `python` points to Python 3, you can use `python` instead.
Equivalent commands with both options are shown below.

### From the project root:

```bash
# macOS (typical)
python3 src/main.py tests/example.in

# Linux/Windows or if `python` is Python 3
python src/main.py tests/example.in
```

### To add and run your own test files, follow this format:

```bash
# macOS (typical)
python3 src/main.py tests/<filename>.in

# Linux/Windows or if `python` is Python 3
python src/main.py tests/<filename>.in
```

### Clearing output files

To remove all `.out` files from `/data`:

```bash
rm data/*.out
```

---

# Written Response

## Problem Description

Given two strings **A** and **B** and a value map that assigns a positive integer value to each character in the alphabet, find the common subsequence that maximizes the sum of character values.

This is a generalization of the classic Longest Common Subsequence (LCS) problem. In standard LCS, every character has an implicit value of 1, so maximizing value is equivalent to maximizing length. In HVLCS, characters have varying weights, so a shorter subsequence can outperform a longer one if it uses higher-value characters.

## Algorithm

### DP Table Construction

A 2D table `dp` of size `(m+1) x (n+1)` is built where `m = len(A)` and `n = len(B)`. Each cell `dp[i][j]` stores the maximum value achievable by a common subsequence of `A[:i]` and `B[:j]`.

**Base case:**

```
dp[0][j] = 0   for all j
dp[i][0] = 0   for all i
```

**Recurrence:**

```
if A[i-1] == B[j-1]:
    dp[i][j] = dp[i-1][j-1] + value[A[i-1]]
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

When characters match, we extend the best subsequence ending before both positions by including the matched character's value. When they don't match, we take the better result from either skipping the current character in A or in B.

### Backtracking

The optimal subsequence is reconstructed by tracing back from `dp[m][n]`:

1. If `A[i-1] == B[j-1]`, the character is part of the solution — record it and move diagonally to `(i-1, j-1)`.
2. If `dp[i-1][j] >= dp[i][j-1]`, move up to `(i-1, j)`.
3. Otherwise, move left to `(i, j-1)`.

The collected characters are reversed to produce the final subsequence.

### Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(m × n)   |
| Space  | O(m × n)   |

Where `m` and `n` are the lengths of strings A and B, respectively.

---

## Example Walkthrough

**Input** (`tests/example.in`):

```
3
a 2
b 4
c 5
aacb
caab
```

**DP Table:**

|       | ""  | c   | a   | a   | b   |
| ----- | --- | --- | --- | --- | --- |
| ""    | 0   | 0   | 0   | 0   | 0   |
| **a** | 0   | 0   | 2   | 2   | 2   |
| **a** | 0   | 0   | 2   | 4   | 4   |
| **c** | 0   | 5   | 5   | 5   | 5   |
| **b** | 0   | 5   | 5   | 5   | 9   |

**Backtracking from dp[4][4] = 9:**

- `(4,4)`: A[3]='b' == B[3]='b' → include 'b', move to `(3,3)`
- `(3,3)`: A[2]='c' ≠ B[2]='a' → dp[2][3]=4 < dp[3][2]=5, move to `(3,2)`
- `(3,2)`: A[2]='c' ≠ B[1]='a' → dp[2][2]=2 < dp[3][1]=5, move to `(3,1)`
- `(3,1)`: A[2]='c' == B[0]='c' → include 'c', move to `(2,0)`
- `(2,0)`: j=0, stop

Collected (reversed): **"cb"**

**Output:**

```
9
cb
```

The subsequence `"cb"` (value 5 + 4 = 9) outperforms the longer subsequence `"aab"` (value 2 + 2 + 4 = 8) because `c` has a higher weight than two `a`s combined.
