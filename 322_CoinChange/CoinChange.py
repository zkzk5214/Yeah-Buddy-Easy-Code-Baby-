class Solution(object):
    def coinChange1(self, coins, amount):
        """
        BFS
        """
        if amount == 0:  # Don't need any coin
            return 0
        value1, value2, coin_num = [0], [], 0
        visited = [True] + [False] * amount
        while value1:
            coin_num += 1  # Coin Num (depth)
            for val in value1:
                for coin in coins:
                    new = val + coin
                    if new <= amount:  # Find a combination
                        if not visited[new]:  # Current value not checked
                            if new == amount:
                                return coin_num
                            visited[new] = True  # Prevent checking again
                            value2.append(new)  # Value2 always exist new val
            value1, value2 = value2, []
        return False

    def coinChange2(self, coins, amount):
        """
        DP
        """
        rs = [0 if col == 0 else float("inf") for col in range(amount + 1)]
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    rs[i] = min(rs[i], rs[i - coin] + 1)

        if rs[amount] == amount + 1:
            return -1
        return rs[amount]

    def coinChange3(self, coins, amount):
        """
        DP
        """
        cols = amount + 1
        rows = len(coins)
        # First col is 0, rest is inf
        rs = [[0 if col == 0 else float("inf") for col in range(cols)] for _ in range(rows)]

        for i in range(0, rows):
            for j in range(1, cols):
                if j >= coins[i]:
                    rs[i][j] = min(rs[i - 1][j], rs[i][j - coins[i]] + 1)
                else:
                    rs[i][j] = rs[i - 1][j]
        return rs[rows-1][cols-1]


if __name__ == '__main__':
    nums = [5, 2]
    n = 12
    s = Solution()
    x = s.coinChange2(nums, n)
    print(x)
