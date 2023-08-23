arr = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
for i in range(len(arr)):
    print(" ".join(arr[i]))
transposed = [[0 for _ in range(len(arr))]
              for _ in range(len(arr[0]))]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        transposed[j][i] = arr[i][j]
for i in range(len(transposed)):
    print(" ".join(transposed[i]))
