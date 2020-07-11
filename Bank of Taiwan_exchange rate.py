#Open the information page. you can write it as below.
import urllib.request as req
#url = "https://www.ptt.cc/bbs/movie/index.html"  #PTT can't not open in China.
url = "https://www.bot.com.tw/Pages/default.aspx"
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")
print(data)


#Way1:requests
import requests
req = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
print(req.text)



#Way2:pandas
import pandas
dfs = pandas.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")
print(dfs[0])

