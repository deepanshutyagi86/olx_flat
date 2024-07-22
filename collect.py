from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [], 'price': [], 'link': [], 'location': []}

for file in os.listdir("data"):
    try:    # to escape from those products, which don't give the value
        with open(f"data/{file}") as f:
          html_doc = f.read()
        
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        #print(soup.prettify())
        t = soup.find("span", attrs={"data-aut-id": 'itemTitle'})
        title = t.get_text() 
        
        l = soup.find("a")
        link ="https://www.olx.in" + l['href']
        
        p = soup.find("span", attrs={"data-aut-id": 'itemPrice'})
        price = p.get_text()

        lo = soup.find("span", attrs={"data-aut-id": 'item-location'})
        location = lo.get_text()


        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
        d['location'].append(location)

        # print(title , price)
    except Exception as e:
       print(e)

  #break if i want to print only 1 
df = pd.DataFrame(data=d)
df.to_csv("data..csv")