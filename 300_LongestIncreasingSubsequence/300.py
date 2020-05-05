# Dynamic programming.


class Solution:
    def LIS1(self, nums):
        """
        nums: List[int]
        return: int
        """
        if not nums:
            return 0

        arr = [1] * len(nums)  # Initial

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    arr[i] = max(arr[i], arr[j] + 1)

        return max(arr)

    def LIS2(self, nums):   # (Still confuse)
        arr = []
        for n in nums:
            if not arr or n > arr[-1]:
                arr.append(n)
            else:
                left, right = 0, len(arr) - 1
                loc = right
                while left <= right:
                    mid = (left + right) // 2
                    if arr[mid] >= n:
                        loc = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                arr[loc] = n
        return len(arr)


if __name__ == "__main__":
    s = Solution()
    x = [1, 2, 3, 2, 1]

    print(s.LIS1(x))
