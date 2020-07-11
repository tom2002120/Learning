#抓取PTT電影版的網頁原始碼
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"  #練習用，用urlopen是抓不到的資訊的，要給他user特徵

#建立一個Request物件，附加Request Headers的資訊
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
'''print(data)'''

#解析原始碼，取得文章標題
import bs4
root = bs4.BeautifulSoup(data,"html.parser")
'''print(root.title.string)'''
titles = root.find_all("div",class_="title")    #尋找所有class="title"的div標籤
                                                #只抓文字print(titles.a.string)
'''print(titles)'''
for title in titles:
    if title.a != None:                         #如果有a就是完整的就印出來
        print(title.a.string)
