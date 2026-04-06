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

## Written Component
 
### Q2: Recurrence Equation
 
Let `dp[i][j]` be the maximum value of any common subsequence of `A[:i]` and `B[:j]`.
 
**Base cases:**
```
dp[0][j] = 0   for all j
dp[i][0] = 0   for all i
```
An empty prefix of either string has no characters to match, so the value is 0.
 
**Recurrence:**
```
if A[i-1] == B[j-1]:
    dp[i][j] = dp[i-1][j-1] + value[A[i-1]]
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```
 
**Correctness:**
 
When `A[i-1] == B[j-1]`, the matched character can either be included or excluded. Excluding it gives at most `max(dp[i-1][j], dp[i][j-1])`. Including it gives `dp[i-1][j-1] + value[A[i-1]]`. Since all values are nonnegative, including the match is always at least as good, so we always take it.
 
When `A[i-1] != B[j-1]`, the two characters cannot both appear at the end of any common subsequence, so at least one must be skipped. We take the better of the two options: skip the current character in A (`dp[i-1][j]`) or skip it in B (`dp[i][j-1]`).
 
**Example** (`tests/example.in`, A = `aacb`, B = `caab`):
 
|       | ""  | c | a | a | b |
| ----- | --- | - | - | - | - |
| ""    | 0   | 0 | 0 | 0 | 0 |
| **a** | 0   | 0 | 2 | 2 | 2 |
| **a** | 0   | 0 | 2 | 4 | 4 |
| **c** | 0   | 5 | 5 | 5 | 5 |
| **b** | 0   | 5 | 5 | 5 | 9 |
 
Backtracking from `dp[4][4] = 9`:
- `(4,4)`: `b == b` → include `b`, move to `(3,3)`
- `(3,3)`: `c ≠ a` → `dp[3][2]=5 > dp[2][3]=4`, move to `(3,2)`
- `(3,2)`: `c ≠ a` → `dp[3][1]=5 > dp[2][2]=2`, move to `(3,1)`
- `(3,1)`: `c == c` → include `c`, move to `(2,0)`
- `(2,0)`: j=0, stop
 
Result (reversed): **cb** with value 5 + 4 = **9**