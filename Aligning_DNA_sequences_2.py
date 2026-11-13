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

# 單一路徑
def direction(score, v, w):
    n = len(v)
    m = len(w)
    dir = [["" for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if v[i-1] == w[j-1]:
                dir[i][j] = "ul" 
            elif score[i-1][j] > score[i][j-1]:
                dir[i][j] = "up"     
            elif score[i-1][j] < score[i][j-1]:
                dir[i][j] = "le"
            else:
                dir[i][j] = "le"    
    return dir

w = "ATCGTAC"
v = "ATGTTAT"

# 最長子序列長度
score, length = LCS(v, w)
print("length of the longest common subsequence : ", length)
print()

# 列出單一路徑
dir = direction(score, v, w)
move = {"ul": (-1, -1), "up": (-1, 0), "le": (0, -1)}   # 每個方向要怎麼移動
paths = []
def dfs(i, j, path):
    if i == 0 or j == 0:
        paths.append(path)
        return 
    dx, dy = move[dir[i][j]]
    dfs(i + dx, j + dy, path + [dir[i][j]])
dfs(len(v), len(w), [])
print(paths)
print()