def find_minimum_number_of_coins(coins, target):
    dp = [target + 1] * (target + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[target] if dp[target] <= target else -1

print(find_minimum_number_of_coins([1, 3, 7], 9))