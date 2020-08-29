from .dynamic_programming import CoinChange
class DpRunner():
    @staticmethod
    def run():
        coin_change = CoinChange()

        print("COIN CHANGE")

        c = coin_change.minCoins(19, [9,6,5,1])

        print(c)
