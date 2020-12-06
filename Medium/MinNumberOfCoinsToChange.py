def minNumberOfCoinsForChange(n, denoms):
    minCoins = [float('inf') for amount in range(n+1)]
    minCoins[0] = 0

    for denom in denoms:
        for money in range(1, n+1):
            if money >= denom:
                minCoins[money] = min((minCoins[ money - denom] + 1), minCoins[money])
                
    return minCoins[n] if minCoins[n] != float('inf')  else -1