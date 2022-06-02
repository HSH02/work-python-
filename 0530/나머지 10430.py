A,B,C = map(int, input().split()) # 변수 1, 변수2 = map(int,input('문자열).split('기준문자열'))

print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C, sep='\n')

#(sep = 파라미터)
#sep 파라미터는 출력 값이 여러개인 경우 각 출력값 사이에 삽입할 문자를 지정할 수 있다.
#예시 print(함수1,함수2,함수3,sep='삽입할 문자')

#출력
#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.