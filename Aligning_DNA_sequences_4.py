# matches − 𝜇 × ( # mismatches ) − 𝜎 × ( # indels )

sigma = - 0.7      # indel penalty
mu = - 0.8         # mismatch penalty


def global_alignment_problem(v, w):
    n = len(v)
    m = len(w)
    score = [[0 for j in range(m + 1)] for i in range(n + 1)]
    dir = [[[] for j in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        score[i][0] = score[i-1][0] + sigma
        dir[i][0] = ["up"]

    for j in range(1, m + 1):
        score[0][j] = score[0][j-1] + sigma
        dir[0][j] = ["le"]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # if 只用來決定對角線要加多少
            if v[i-1] == w[j-1]:
                diag_bonus = 1        # match
            else:
                diag_bonus = mu       # mismatch

            up   = score[i-1][j] + sigma
            left = score[i][j-1] + sigma
            diag = score[i-1][j-1] + diag_bonus
            best = max(up, left, diag)

            score[i][j] = best
            if abs(diag - best) < 1e-9:
                dir[i][j].append("ul")
            if abs(up - best) < 1e-9:
                dir[i][j].append("up")
            if abs(left - best) < 1e-9:
                dir[i][j].append("le")
    return score, dir


w = "ATCGTAC"
v = "ATGTTAT"

score, direction = global_alignment_problem(v, w)
for s in score:
    print(s)
print()
for d in direction:
    print(d)
print()


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
    for d in direction[i][j]:               # 這格有幾個方向，就分幾個身
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