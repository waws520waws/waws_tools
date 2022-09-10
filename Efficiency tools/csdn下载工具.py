import requests
from bs4 import BeautifulSoup
from werkzeug.utils import secure_filename

def csdn_download_tool(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    req = requests.get(url, headers=headers)
    # 标准解析格式
    html = req.text

    soup = BeautifulSoup(html, "lxml")
    title = soup.select("#articleContentId")[0].get_text()
    content = str(soup.select("#article_content")[0])
    filename = secure_filename(title + ".html")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print("已经下载完成")

if __name__ == '__main__':
    url = "https://blog.csdn.net/qq_41185868/article/details/96484201"
    csdn_download_tool(url)