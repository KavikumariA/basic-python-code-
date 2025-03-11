from bs4 import BeautifulSoup
import requests
# import csv


r = requests.get("https://www.amazon.com/s?k=toys&rh=p_36%3A-2500&_encoding=UTF8&content-id=amzn1.sym.44da4965-9668-4613-bec2-a3a75f0c2ad4&pd_rd_r=9cd600a7-d291-49c3-b2d9-dd027a426075&pd_rd_w=c8uZC&pd_rd_wg=xMrQA&pf_rd_p=44da4965-9668-4613-bec2-a3a75f0c2ad4&pf_rd_r=SNHM2165AHK9760MF2RZ&ref=pd_hp_d_atf_unk")
# w=[["name","rate"]]
print(r)
html=r
v = BeautifulSoup(html.content,'html.parser')
# for i in w:
# rr = v.find_all("a",class_="wjcEIp")
# print(rr)



# rr = v.find_all("a",class_="wjcEIp")
# for i in rr:
#     print(i.text)
#     # w.append(i.text)
   
# rs = v.find_all("div",class_="Nx9bqj")
# for j in rs:
#     print(j.text)
#     w.append(j.text)
rt = v.find_all('div',class_="puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-vo8l48qglv7yn2w1wwffhqo34k s-latency-cf-section puis-card-border")
for i in rt:
    pp=v.find_all('h2',class_="a-size-mini a-spacing-none a-color-base s-line-clamp-4").text
    pr=v.find_all('div',class_="a-section a-spacing-none a-spacing-top-micro").text
print(pp)
print(pr)
    # if pp and pr:
    #     name=pp
    #     rate=pr
    # w.append([pp],[pr])
            
# with open('w.csv',mode='w',newline='',encoding='utf-8') as file:
#     write=csv.writer(file)
#     write.writerow(w)
    # for i in w:
    #     file.writerow(i)
       
    #     file.write('\n')
        
        
    