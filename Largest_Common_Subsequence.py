def lcs(string1: str, string2: str, string3: str):
    a = len(string1)
    b = len(string2)
    c = len(string3)
    dp = [[[0 for f in range(c + 1)] for e in range(b + 1)] for d in range(a + 1)]

    for d, i in enumerate(string1):
        for e, j in enumerate(string2):
            for f, k in enumerate(string3):
                if i == 0 or j == 0 or k == 0:
                    dp[d][e][f] = 0
                elif i == j and j == k:
                    dp[d + 1][e + 1][f + 1] = dp[d][e][f] + 1

                else:
                    dp[d + 1][e + 1][f + 1] = max(dp[d][e + 1][f + 1], dp[d + 1][e][f + 1], dp[d + 1][e + 1][f])

    return solve(string1, string2, string3, dp, a, b, c)


def solve(s1, s2, s3, dp, a, b, c):
    ls = ''
    i, j, k = a, b, c
    while i > 0 and j > 0 and k > 0:
        if s1[i - 1] == s2[j - 1] and s2[j - 1] == s3[k - 1]:
            ls = ls + s1[i - 1]
            i -= 1
            j -= 1
            k -= 1
        elif dp[i - 1][j][k] == dp[i][j][k]:
            i -= 1
        elif dp[i][j - 1][k] == dp[i][j][k]:
            j -= 1
        elif dp[i][j][k - 1] == dp[i][j][k]:
            k -= 1

    return ls[::-1]

