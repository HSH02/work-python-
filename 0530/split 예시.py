# split의 예시 
a = "Hello World"
# split 함수는 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.
print(a.split()) #  출력 값 ['Hello', 'World']

b = "aubucud"
print(b.split('u')) # 출력 값 ['a', 'b', 'c', 'd']