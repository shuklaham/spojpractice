#spoj solutions
def editDistance(str1, str2, m, n):
	dp = [[0 for i in range(n+1)]for j in range(m+1)]
	for x in xrange(m + 1):
		dp[x][0] = x

	for x in xrange(n + 1):
		dp[0][x] = x

	for i in range(1,m+1):
		for j in range(1,n+1):
				dp[i][j] = min(dp[i-1][j] + 1,
								dp[i-1][j-1] + (str1[i-1]!= str2[j-1]),
								dp[i][j-1] + 1
								)
	return dp[m][n]

tc = int(raw_input())
for i in range(tc):
	str1 = raw_input()
	str2 = raw_input()
	print editDistance(str1,str2,len(str1),len(str2))

