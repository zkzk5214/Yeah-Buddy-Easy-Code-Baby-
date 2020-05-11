from collections import Counter


def majorityElement1(arr):
    freqDict = Counter(arr)
    size = len(arr)
    for (key, val) in freqDict.items():
        if val > (size / 2):
            return key
    return None


def majorityElement2(arr):
    return sorted(arr)[len(arr) // 2]


if __name__ == '__main__':
    nums = [2, 3, 2]
    s = majorityElement1(nums)
    print(s)
