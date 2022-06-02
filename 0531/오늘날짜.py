#https://www.acmicpc.net/problem/10699
from datetime import datetime, timedelta


print(datetime.today().strftime("%Y-%m-%d"))

# print(datetime.today().strftime("%Y/%m/%d %H:%M:%S")) # YYYY/mm/dd HH:MM:SS 형태의 시간 출력
# print(datetime.today()) # 현재 날짜 
# print(datetime.today().year) # 현재 년도
# print(datetime.today().month) # 현재 월
# print(datetime.today().day) # 현재 일
# print(datetime.today().hour) # 현재 시간 
# yes = datetime.today() -timedelta(1)
# print(yes.strftime("%Y-%m-%d")) 어제 날짜 출력