def maxProfit(prices):
    buy, ans = float('inf'), 0
    for p in prices:
        buy, ans = min(buy, p), max(ans, p - buy)
    return ans


nums = [7, 6, 4, 3, 1]
maxProfit(nums)
print(maxProfit(nums))
