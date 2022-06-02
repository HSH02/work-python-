#https://www.acmicpc.net/problem/2525

hour, min = map(int,input().split())
time = int(input())
min += time

if(min>=60):
    hour += min//60
    min = min%60

if(hour>=24):
    hour = hour%24
    
  
print(hour,min)

# print(hour,min)