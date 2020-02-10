#encoding:UTF-8
from bs4 import BeautifulSoup
import lxml
import requests


def get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        #手动设置为utf-8
        r.encoding = 'utf-8'
        return r.text
    except:
        return "ERROR"

def get_content(url):
    #初始化一个列表
    comments = []

    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    liTags = soup.find_all('li',attrs={'class': ' j_thread_list clearfix'})
    for li in liTags:
        #初始化一个字典
        comment = {}
        try:
            comment['title'] = li.find('a',attrs={'class':'j_th_tit'}).string
            comment['link'] = "http://tieba.baidu.com/" + li.find('a', attrs={'class': 'j_th_tit '}).get('href')
            comment['name'] = li.find('span',attrs={'class':'tb_icon_author'}).get('titl')
            comment['time'] = li.find('span', attrs={'class': 'pull-right is_show_create_time'}).string
            comment['replyNum'] = li.find('span', attrs={'class': 'threadlist_rep_num center_text'}).string
            comments.append(comment)
        except:
            print("出了小问题")

    return comments

def outfile(dict):
    with open('TTBT.txt','a+') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))

    print("当前爬虫完成")

def main(base_url, deep):
    url_list = []
    # 将所有需要爬去的url存入列表
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('所有的网页已经下载到本地！ 开始筛选信息。。。。')

    #循环写入所有的数据
    for url in url_list:
        content = get_content(url)
        outfile(content)
    print('所有的信息都已经保存完毕！')


base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'
# 设置需要爬取的页码数量
deep = 3

if __name__ == '__main__':
    main(base_url, deep)










