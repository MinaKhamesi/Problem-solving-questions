def numberOfWaysToMakeChange(n, denoms):
	ways = [0 for amount in range(n+1)]
	ways[0] = 1
	
	for denom in denoms:
		for money in range(1,len(ways)):
			if money >= denom:
				ways[money] = ways[ money - denom ] + ways[ money ]
				
	return ways[-1]