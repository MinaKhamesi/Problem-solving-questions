def maxProfitWithKTransaction( prices , k):
    if not len(prices): return 0
    maxProfits =[[0 for day in prices] for transaction in range( k + 1)]

    for transaction in range(1 , k+1):
        maxThusFar = float('-inf')
        for day in range(1 , len(prices)):
            maxThusFar = max(maxThusFar , -prices[day - 1]+maxProfits[transaction - 1][ day - 1 ])
            maxProfits[transaction][day] = max(maxProfits[transaction][day - 1] , maxThusFar + prices[day])
            

    return maxProfits[k][-1]

