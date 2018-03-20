'''小说网站爬取
武炼巅峰 元尊
'''
import requests
import re
import time
url = 'http://www.biquge5200.com/modules/article/search.php?'

def huoqu():
    name = input('请输入书名：')
    params = {'searchkey':name}
    response = requests.get(url,params = params)
    response.encoding = 'gbk'
    data = response.text
    #print(data)
    shuming = re.findall(r'<td class="odd"><a href="(.*?)">(.*?)</a></td>',data,re.S)
    #print(shuming)
    if shuming ==[]:
        print("该书名不存在。")
        return huoqu()
    else:
        for aa in shuming:
            if aa[1] == name:
                return aa
                print(aa[0])
            else:
                pass

def get_zhangjie(url1):
    response = requests.get(url1)
    response.encoding = 'gbk'
    data = response.text
    zhangjie = re.findall(r'<dd><a href="(.*?)">(.*?)</a></dd>', data, re.S)
    return zhangjie
def get_chapter(url2):
    response = requests.get(url2)
    response.encoding = 'gbk'
    data = response.text
    chapter = re.findall(r'<div id="content">(.*?)</div>',data,re.S)[0]
    #chapter = chapter.strip()         #去掉首尾的空格
    chapter = chapter.replace('<br/>',' ')
    return chapter

url = huoqu()
zhangjie = get_zhangjie(url[0])
f = open('%s.txt'%url[1],'w',encoding="utf-8")
for aa in zhangjie:
    chapter = get_chapter(aa[0])
    f.write(aa[1])
    f.write('\n')
    f.write(chapter)
    print(aa[1])
    time.sleep(0.5)
f.close()
