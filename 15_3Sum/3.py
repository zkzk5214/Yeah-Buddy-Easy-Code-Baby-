def ThreeSum1(nums):
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # prevent checking duplicate again
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res = (i, l, r)
                while l < r and nums[l] == nums[l + 1]:  # skip over same valued elements
                    l += 1
                while l < r and nums[r] == nums[r - 1]:  # skip over same valued elements
                    r -= 1
                l += 1
                r -= 1

    if not res:
        return -1

    return res


if __name__ == "__main__":
    with open('rosalind_3sum.txt', 'r') as f:
        for i in f.readlines():
            input_list = list(map(int, i.split()))
            s = ThreeSum1(input_list)
