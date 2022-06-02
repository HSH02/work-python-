# https://www.acmicpc.net/problem/2530

hour, min , second= map(int,input().split())
time = int(input())


min += time//60 
time = time % 60
second += time
# second가 600으로 나눈 나머지를 계산이 다르게 되도록 하지 않게 time을 60으로 나눈 나머지로 계산하게 함
# 2515를 그냥 600으로 하면 115, 60의 나머지로 계산하면 55가 됨으로 55가 나머지로 해짐
# second는 59 time을 2515라 가장할때 time = time % 60을 하지 않으면 second는 174 
# time = time % 60 계산을 한 후에는 second는 114

if second>=60:
    min += second//60
    second = second%60

if  min>=60:
    hour += min//60
    min = min%60

if hour>=24:
    hour = hour % 24

print(hour,min,second)
# print(time%600)
# print(time//60)