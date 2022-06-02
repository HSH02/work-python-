#https://www.acmicpc.net/problem/2914
#( 멜로디의 개수) / (앨범에 수록된 곡의 개수)
#첫째 줄에 앨범에 수록된 곡의 개수 A와 평균값 I가 주어진다. (1 ≤ A, I ≤ 100)

a,b = map(int,input().split())

print(a*(b-1)+1)
