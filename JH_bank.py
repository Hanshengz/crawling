import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        #手动设置为utf-8
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




def save_csv(lists):
    with open('bank0.csv', 'a', encoding='utf-8', newline='') as f:
       for i in range(len(lists)):
           csv.writer(f).writerow([lists[i][0],lists[i][1],lists[i][2],lists[i][3],lists[i][4]])

def main(deep):
    lev1code=[340,110,500,350,620,440,450,520,460,130,410,230,420,430,220,320,360,210,150,640,630,370,140,610,310,510,120,540,650,530,330]

    for i in range(deep):
        url = 'http://tool.ccb.com/outlet/frontOprNodeQuery.gsp?_Lev1Code=340&_Lev2Code=&_KeyWork=&_NodeType=101'+'&pageNo='+str(i+1)
        content = get_content(url)
        save_csv(content)

    print("work over!")

if __name__ == "__main__":
    deep = 19
    main(deep)