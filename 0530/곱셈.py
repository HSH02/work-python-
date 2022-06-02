#https://www.acmicpc.net/problem/2588

a = int(input())
b = input()

#len() 문자열 길이 반환 ex) len(123) -> 3 , len(1234) -> 4
#b는 int 선언이 안되었으므로 문자열이라는 것을 유의 b[2],b[1],b[0] 같이 출력이 가능, a는 정수라 안됌
for i in range(len(b),0,-1): # (3,0,-1)
    print(a*int(b[i-1]))


print(a*int(b))