from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

bookList_url = 'http://m.56dudu.com/list/index'
# filename='abc.txt'
# fw=open(filename, 'w', encoding='utf-8')
# fw.write(str(soup))
# fw.flush()
# fw.close()

def getPageNum(url):
    f = requests.get(url)  # Get该网页从而获取该html内容
    soup = BeautifulSoup(f.content, "lxml")
    try:
        pageNum = soup.find('div', class_="page clearfix pc_none").find('span').text
        print('getPageNum执行成功', pageNum)
        return int(pageNum[14:16])
    except:
        print('getPageNum执行失败')
    finally:
        print('___________________________')

def getBookInfo(url):
    f = requests.get(url)  # Get该网页从而获取该html内容
    soup = BeautifulSoup(f.content, "lxml")
    try:
        bookList = soup.find('div', class_="list clearfix").findAll('li')
        for i in bookList:
            imgUrl = i.find('img')
            print('书籍封面:',imgUrl['src'])
            print('书名:',(i.find('p', class_="name").text).strip())
            print('类型:',(i.find('p', class_="actor").text).strip())
            print('状态:',(i.find('span', class_="rgba1").text).strip())

            #下载文件
            # splider.YsSpider(i.find('b').text).download_files()
            print('___________________________')

    except:
        print('getBookInfo执行失败')
    finally:
        print('___________________________')

for num in range(1,2):
    pageNum = getPageNum(bookList_url+str(num)+'.html')
    print(pageNum)
    pageNum=4
    getBookInfo(bookList_url+str(num)+'.html')
    print(bookList_url+str(num)+'.html')
    for num1 in range(2,pageNum):
        getBookInfo(bookList_url+str(num)+'_'+str(num1)+'.html')
        print(bookList_url+str(num)+'_'+str(num1)+'.html')