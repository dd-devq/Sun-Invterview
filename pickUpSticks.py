def pickUpSticks(n):
    ways = [0] * (n + 1)
    ways[0] = 1

    for i in range(1, n + 1):
        ways[i] += ways[i - 1]
        if i >= 2:
            ways[i] += ways[i - 2]
        if i >= 3:
            ways[i] += ways[i - 3]
    return ways[n]


print('Test 1: ' + str(pickUpSticks(2)))
print('Test 2: ' + str(pickUpSticks(3)))
