sigma = - 1      # indel penalty
mu = - 1        # mismatch penalty

def local_alignment_problem(v, w):
    n = len(v)
    m = len(w)
    score = [[0 for j in range(m + 1)] for i in range(n + 1)]
    dir = [[[] for j in range(m + 1)] for i in range(n + 1)]
    max_score = 0
    max_loc = (0, 0)
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
            best = max(0, up, left, diag)

            score[i][j] = best

            if score[i][j] > max_score:
                max_score = score[i][j]
                max_loc = (i, j)
            if abs(diag - best) < 1e-9:
                dir[i][j].append("ul")
            if abs(up - best) < 1e-9:
                dir[i][j].append("up")
            if abs(left - best) < 1e-9:
                dir[i][j].append("le")
    return score, dir, max_loc

v = 'TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC'
w = 'AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC'

score, direction, max_loc = local_alignment_problem(v, w)
print(max_loc)

move = {"ul": (-1, -1), "up": (-1, 0), "le": (0, -1)}   # 每個方向要怎麼移動 
paths = []
results = []   # (起點 i, 起點 j, dna1, dna2, match)
def walk(i, j, path, dna1, dna2, match):
    if score[i][j] == 0:             
        paths.append(path)
        results.append((i, j, dna1[::-1], dna2[::-1], match[::-1]))
        return
    for d in direction[i][j]:               # 這格有幾個方向，就分幾個身
        di, dj = move[d]
        if d == 'ul':
            m = '|' if v[i-1] == w[j-1] else '.'   # mismatch 不要畫 |
            walk(i + di, j + dj, path + [d], dna1 + v[i-1], dna2 + w[j-1], match + m)
        elif d == 'le':
            walk(i + di, j + dj, path + [d], dna1 + '-', dna2 + w[j-1], match + ' ')
        else:
            walk(i + di, j + dj, path + [d], dna1 + v[i-1], dna2 + '-', match + ' ')

end_i, end_j = max_loc
walk(end_i, end_j, [], "", "", "")

for k, (si, sj, d1, d2, m) in enumerate(results, 1):
    # 比對區塊前面的字數不同 (v 有 si 個、w 有 sj 個)，
    # 用空白把較短的那條往右推，讓比對區塊的起點對齊在同一欄
    width = max(si, sj)
    top = ' ' * (width - si) + v[:si] + d1 + v[end_i:]
    mid = ' ' * width + m
    bot = ' ' * (width - sj) + w[:sj] + d2 + w[end_j:]
    print(f'path{k}:  score = {score[end_i][end_j]:.1f}')
    print(top)
    print(mid)
    print(bot)
    print()
