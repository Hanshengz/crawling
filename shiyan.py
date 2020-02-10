from bs4 import BeautifulSoup
import requests

html = '''
<tr>
    <td>莆田市仓后分理处</td>    
    <td>
    莆田市荔城区镇海街道北大北街146号&nbsp;&nbsp;<span style="color:#0066b3;cursor:pointer" onclick="javascript:showmap('350838675305E02','莆田市荔城区镇海街道北大北街146号');"><a title='地图服务由Google友情提供，仅供参考，具体请以实际公布地址为准。'>[地图]</a></span>   
    </td>
    <td>原市政府后门对面</td>
    <td>周一至周日<br>对私：9：00-12：00 13：00-17：30</td>
    <td>0594-2295572</td>
  </tr>
  

'''

soup = BeautifulSoup(html,'lxml')
tds = soup.find_all('td')
for td in tds:
    print(td.text.strip())

print('http://tool.ccb.com/outlet/frontOprNodeQuery.gsp?_Lev1Code=520&_Lev2Code=5208D3596335E02&_KeyWork=&_NodeType=101'+'&pageNo='+str(5))