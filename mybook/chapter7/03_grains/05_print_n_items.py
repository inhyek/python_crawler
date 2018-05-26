from urllib.request import urlopen
import json

from_date = "2010-01-01"
to_date = "2018-04-28"
url = "http://grains.krei.re.kr/chart/main_chart/index/kind/W/sdate/" + from_date + "/edate/" + to_date
html = urlopen(url)

json_objs = json.load(html)
print(json_objs[0:10])