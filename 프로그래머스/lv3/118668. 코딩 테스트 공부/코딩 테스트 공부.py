import sys
INF=sys.maxsize
def solution(alp, cop, problems):
    target_alp=alp
    target_cop=cop
    for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
        target_alp=max(alp_req,target_alp)
        target_cop=max(cop_req,target_cop)
    dp=[[INF]*(301) for _ in range(301)]
    dp[alp][cop]=0
    for i in range(alp,target_alp+1):
        for j in range(cop,target_cop+1):
            dp[i+1][j]=min(dp[i+1][j],dp[i][j]+1)
            dp[i][j+1]=min(dp[i][j+1],dp[i][j]+1)
            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i>=alp_req and j>=cop_req:
                    #print(dp[i][j],i,j)
                    dp[i+alp_rwd][j+cop_rwd]=min(dp[i+alp_rwd][j+cop_rwd],dp[i][j]+cost)
         
    return dp[target_alp][target_cop]
        