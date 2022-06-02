# https://www.acmicpc.net/problem/5355

number = int(input())

for _ in range(number):
    num = list(map(str, input().split()))
    answer = 0
    for i in range(len(num)):
        if i == 0:
            answer += float(num[i])
        else:
            if num[i] == "#":
                answer -= 7
            elif num[i] == "%":
                answer += 5
            elif num[i] == "@":
                answer *= 3
                
    print("%0.2f" % answer)



