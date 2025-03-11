from bs4 import BeautifulSoup
import requests
import csv
s = requests.get('https://www.flipkart.com/offers-list/itaccessories?screen=dynamic&pk=themeViews%3DITAcce%3Aapp%2CITAcce%3Adesk~widgetType%3DdealCard~contentType%3Dneo&wid=2.dealCard.OMU&fm=neo%2Fmerchandising&iid=M_98feca88-06f9-4b1b-adf1-9a5936d9b1ae_1_372UD5BXDFYS_MC.B0RGQT4LXCY4&otracker=hp_rich_navigation_7_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2BAccessories_B0RGQT4LXCY4&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_7_L1_view-all&cid=B0RGQT4LXCY4')
print (s)
cc=[['a1']]
html =s
s = BeautifulSoup(html.content,'html.parser')
v =s.find('title')
'''print(s.prettify())'''
print(v.text)
a = s.find_all(class_="ZHvV68")
print(a)
for i in a:
    a1 = i.text
    print(a1)
    cc.append([a1])
with open('cc.csv', mode='w',newline='',encoding='utf-8') as fil:
    wri=csv.writer(fil)
    wri.writerow(cc)



'''b =s.find('h1').text'''
'''print(a)'''
'''for i in b:
    print(i.text)'''