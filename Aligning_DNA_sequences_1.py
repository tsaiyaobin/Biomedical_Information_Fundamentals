def LCS(v, w):
    n = len(v)
    m = len(w)
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if v[i-1] == w[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp, dp[-1][-1]        


w = "ATCGTAC"
v = "ATGTTAT"

# 最長子序列長度
score, length = LCS(v, w)
print("length of the longest common subsequence : ", length)
print()



