#https://www.acmicpc.net/problem/2163

n,m = map(int,input().split())
#초콜릿을 1*1로 나뉙 위해 자르는 횟수는 다음과 같다
#가로 = 가로 -1 번 
#세로 = 세로 -1 번
#(세로-1)+세로*(가로-1)
# -> 세로-1+세로*가로-세로 ->세로*가로-1


#(n*m) -1 

print((n*m)-1)