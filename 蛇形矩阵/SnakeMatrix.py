while True:
    try:
        n, curNum = int(input()), 1
        res = [[0 for i in range(n)] for j in range(n)]  # Matrix = zeros(n)
        for i in range(n):  # i = 0 : n-1
            for j in range(i + 1):  # j = 0 : i
                res[i - j][j] = curNum
                curNum += 1
        for i in res:
            print(" ".join(map(str, (filter(lambda i: i != 0, i)))))  # Remove value >0 in Matrix
    except:
        break

# input 4
# 1 3 6 10
# 2 5 9
# 4 8
# 7
