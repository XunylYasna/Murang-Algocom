def solve(s1, s2, n, m):
    # compute and return answer here
    # taken from enchant utils
    if n < m:
        return solve(s2, s1, m, n)

    previous_row = range(m + 1)

    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


s1 = input().rstrip()
s2 = input().rstrip()
n = len(s1)
m = len(s2)
print("{}".format(solve(s1, s2, n, m)))
