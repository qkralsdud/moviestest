import requests
from bs4 import BeautifulSoup

def temp():
    #list = []
    uri="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hRs5Tlp0Jy0ssTgTlHossssstYZ-261792"
    response = requests.get(uri)

    soup = BeautifulSoup(response.text, 'html.parser')
    target = soup.select_one(".todaytemp")
    today_temp = target.text
    today_temp1 = dict([["temp", today_temp]])
    #list.append(today_temp1)
    #print(today_temp1)
    return today_temp1

def temp2():
    uri="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hRs5Tlp0Jy0ssTgTlHossssstYZ-261792"
    response = requests.get(uri)

    soup = BeautifulSoup(response.text, 'html.parser')
    target = soup.select_one(".todaytemp")
    today_temp = target.text
    #list.append(today_temp)
    return today_temp

