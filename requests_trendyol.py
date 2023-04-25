import requests
from bs4 import BeautifulSoup

def trendyol(product):
    productId = str(product)
    url = "https://www.trendyol.com/marka/urun-p-" + productId
    icerik = requests.get(url)
    htmlicerik = icerik.content
    soup = BeautifulSoup(htmlicerik,"html.parser")
    title = soup.find_all("h1",{"class":"pr-new-br"})
    fiyat = soup.find_all("span",{"class":"prc-dsc"})
    satici = soup.find_all("a",{"class":"merchant-text"})
    for i,j,z in zip(title,fiyat,satici):
        print(i.text,":",j.text,":",z.text)

