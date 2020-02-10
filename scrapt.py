import csv

from bs4 import BeautifulSoup
import requests



def get_html(url):
    try:
        r = requests.post(url)
        r.raise_for_status()
        #手动设置为utf-8
        r.encoding = r.apparent_encoding
        #r.encoding = 'utf-8'
        return r.text
    except:
        return "ERROR"

def get_content(url):
    lists = []
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        try:
            list = []
            tds = tr.find_all('td')
            for td in tds:
                list.append(td.text.strip())
            if list != []:
                lists.append(list)
        except:
            print("出了小问题")
    return lists



def save_file(lists):
    with open('stocke.csv', 'a', encoding='utf-8', newline='') as f:
       for i in range(len(lists)):
           csv.writer(f).writerow([lists[i][0],lists[i][1],lists[i][2],lists[i][3],lists[i][4]])


for i in range(1):
    url = 'http://tool.ccb.com/outlet/frontOprNodeQuery.gsp?_Lev1Code=340&_Lev2Code=&_KeyWork=&_NodeType=101' + '&pageNo=' + str(i + 1)
    content = get_content(url)
    save_file(content)

print("work over!")






