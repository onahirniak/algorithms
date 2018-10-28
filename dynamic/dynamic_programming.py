from os import sys

class CoinChange:

    def minCoins(self, money, coins):
        table = [sys.maxsize for c in range(money + 1)]

        table[0] = 0

        for i in range(1, money + 1):
            for coin in coins:
                if coin <= i:
                    change = table[i - coin]
                    table[i] = min(change + 1, table[i])

        return table[money]