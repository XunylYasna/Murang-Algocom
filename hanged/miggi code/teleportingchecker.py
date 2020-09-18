MOD = int(1e9) + 7
r,c,p,k = list(map(int,input().strip().split(" ")))
rstart,cstart = list(map(int,input().strip().split(" ")))
portals = [list(map(int,input().strip().split(" "))) for i in range(p)]

# compute and print answer here

hasPortal = [502][502]
pair<int,int> portals[502][502]
dp = [502][502][22]

def solve(int row,int col, int k):
	if( row >= 1 && row <= r && col >= 1 && col <= c ):
		if dp[row][col][k] > -1 :
			return dp[row][col][k]
	
		if row == r :
			return 1
		
		elif hasPortal[row][col] && k > 0:
			pair<int,int> tempdest = portals[row][col];
			return dp[row][col][k] = solve(tempdest.first,tempdest.second,k-1) % MOD + solve(row + 1,col-1,k) % MOD + solve(row + 1,col+1,k) % MOD
		
        else:
			return dp[row][col][k] = solve(row+1,col-1,k) % MOD + solve(row+1,col+1,k) % MOD 
	
    else:
		return 0
		


# 	int p,k,rs,cs,rpsource,cpsource,rdest,cdest;
# 	scanf("%d%d%d%d",&r,&c,&p,&k);
#	memset(hasPortal,false,sizeof(hasPortal));
#	memset(dp,-1,sizeof(dp));
	
	for i in range(0, p-1) :
		hasPortal[rpsource][cpsource] = true
		hasPortal[rdest][cdest] = true
		
		portals[rpsource][cpsource] = make_pair(rdest,cdest)
		portals[rdest][cdest] = make_pair(rpsource,cpsource)
	
	
	print("{}",solve(rs,cs,k))