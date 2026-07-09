matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

pos_i, pos_j = 0, 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            pos_i, pos_j = i, j
            break

center_i, center_j = 2, 2
min_distance = abs(pos_i - center_i) + abs(pos_j - center_j)

print(min_distance)
