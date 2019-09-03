from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
res = req.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(res,'html.parser')
cmd = input("안녕하세요. 현재 지역을 입력해 주세요.\n 종료하려면 q를 누르세요.\n")
while cmd != 'q':
    loc = soup.select("location")
    for e in loc :
        if(e.find("city").string == cmd):
            print(e.find("wf").string)
        else :
            print("자료가 없습니다.")
    cmd = input("안녕하세요. 현재 지역을 입력해 주세요.\n 종료하려면 q를 누르세요.\n")
