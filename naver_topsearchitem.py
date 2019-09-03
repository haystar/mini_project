from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = r"https://naver.com"
res = req.urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(res, 'html.parser')


toplist = soup.select(".ah_l > .ah_item")
for e in toplist:
    if e.find("class" == "ah_k") is not None:
        print(e.select_one(".ah_k").string)
