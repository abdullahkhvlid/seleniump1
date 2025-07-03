from bs4 import BeautifulSoup
import os
import pandas as pd

d = {"title": [], "price": [], "link": []}



for file in os.listdir("data"):
    try:

        with open(f"data/{file}", "r") as f:
            htmldoc = f.read()
        soup = BeautifulSoup(htmldoc, "html.parser")
        t = soup.find("h2")
        title = t.get_text()
        l = soup.find("a")
        link = "https://amazon.com/"+ l.get("href")
        p = soup.find("span", class_ ="a-price-whole")
        price = p.get_text()

        d["title"].append(title)
        d["price"].append(price)
        d["link"].append(link)

      
       

    except Exception as e:
        print(e)

df = pd.DataFrame(d)
df.to_csv("data.cvs")