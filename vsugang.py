from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://wis.hufs.ac.kr/src08/jsp/lecture/LECTURE2020L.jsp"
res = req.urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(res,'html.parser')

sugang = soup.select("#premier1 > div")
print(sugang)
