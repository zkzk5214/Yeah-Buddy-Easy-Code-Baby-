def SpiralOrder(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)  # Remove first row
        matrix = list(map(list, zip(*matrix)))[::-1]
    return res
