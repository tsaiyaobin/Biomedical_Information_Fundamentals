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

def all_direction(score, v, w): 
    n = len(v)
    m = len(w)
    dir = [[[] for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if v[i-1] == w[j-1]:
                dir[i][j].append("ul")
                # 字元相同的情況下，上或左有分數相同的就加入路徑
                if score[i-1][j] == score[i][j]:
                    dir[i][j].append("up")
                if score[i][j-1] == score[i][j]:
                    dir[i][j].append("le")
            elif score[i-1][j] > score[i][j-1]:
                dir[i][j].append("up")      
            elif score[i-1][j] < score[i][j-1]:
                dir[i][j].append("le") 
            else:
                # 在位置（i,j）上跟左的分數平手
                dir[i][j].append("le")
                dir[i][j].append("up")   
    return dir

w = "ATCGTAC"
v = "ATGTTAT"

# 最長子序列長度
score, length = LCS(v, w)
print("length of the longest common subsequence : ", length)
print()

# 輸出所有路徑
dir = all_direction(score, v, w)
move = {"ul": (-1, -1), "up": (-1, 0), "le": (0, -1)}   # 每個方向要怎麼移動 
paths = []
Dna1 = []
Dna2 = []
matchs = []
def walk(i, j, path, dna1, dna2, match):
    if i == 0 or j == 0:              # 走到邊界，這條路完成了
        paths.append(path)
        Dna1.append(dna1)
        Dna2.append(dna2)
        matchs.append(match)
        return
    for d in dir[i][j]:               # 這格有幾個方向，就分幾個身
        di, dj = move[d]
        if d == 'ul': 
            walk(i + di, j + dj, path + [d], dna1 + v[i-1], dna2 + w[j-1], match + '|')    # 每個分身往自己的方向繼續走
        elif d == 'le':
            walk(i + di, j + dj, path + [d], dna1 + '-', dna2 + w[j-1], match + ' ')
        else:
            walk(i + di, j + dj, path + [d], dna1 + v[i-1], dna2 + '-', match + ' ')

walk(len(v), len(w), [], "", "", "")
i = 1
for d1, d2, m in zip(Dna1, Dna2, matchs):
    print(f'path{i}:')
    print(d1[::-1])
    print(m[::-1])
    print(d2[::-1])
    print()
    i += 1