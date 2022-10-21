
# 抓取 PTT 電影版的網頁原始碼（HTML)
import bs4
import urllib.request as req


def getData(url):
    # 建立一個 Request 物件，例如 Request Headers 的資訊
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        with open("movie.txt", "a", encoding="utf-8") as file:
            data = response.read().decode("utf-8")
            root = bs4.BeautifulSoup(data, "html.parser")
            titles = root.find_all("div", class_="title")
            for title in titles:
                if title.a != None:
                    if (title.a.string[0:4]) == "[好雷]":
                        print(title.a.string)
                        file.write(title.a.string+"\n")
    # 抓取上一頁的連結
    nextLink = root.find("a", string="‹ 上頁")  # 找到內文是‹ 上頁 的 a 標籤
    return nextLink["href"]


# 主程序，抓取多個頁面的標題
pageURL = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count < 10:
    pageURL = "https://www.ptt.cc"+getData(pageURL)
    count += 1


def getData(url):
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        with open("movie.txt", "a", encoding="utf-8") as file:
            data = response.read().decode("utf-8")
            root = bs4.BeautifulSoup(data, "html.parser")
            titles = root.find_all("div", class_="title")
            for title in titles:
                if title.a != None:
                    if (title.a.string[0:4]) == "[普雷]":
                        print(title.a.string)
                        file.write(title.a.string+"\n")

    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]


# 抓取多個頁面的標題
pageURL = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count < 10:
    pageURL = "https://www.ptt.cc"+getData(pageURL)
    count += 1


def getData(url):
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        with open("movie.txt", "a", encoding="utf-8") as file:
            data = response.read().decode("utf-8")
            root = bs4.BeautifulSoup(data, "html.parser")
            titles = root.find_all("div", class_="title")
            for title in titles:
                if title.a != None:
                    if (title.a.string[0:4]) == "[負雷]":
                        print(title.a.string)
                        file.write(title.a.string+"\n")

    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]


# 抓取多個頁面的標題
pageURL = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count < 10:
    pageURL = "https://www.ptt.cc"+getData(pageURL)
    count += 1
