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
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:  # skip over same valued elements
                    l += 1
                while l < r and nums[r] == nums[r - 1]:  # skip over same valued elements
                    r -= 1
                l += 1
                r -= 1
    return res


def ThreeSum2(A, sum):
    A.sort()
    # Now fix the first element one by one and find the other two elements
    for i in range(0, len(A) - 2):
        # Start two index variables from two corners of the array and move them toward each other
        # index of the first and last element in the remaining elements
        l, r = i + 1, len(A) - 1
        while l < r:
            if A[i] + A[l] + A[r] == sum:
                return print("Triplet is", A[i], ', ', A[l], ', ', A[r])
            elif A[i] + A[l] + A[r] < sum:
                l += 1
            else:  # A[i] + A[l] + A[r] > sum
                r -= 1
    return False
