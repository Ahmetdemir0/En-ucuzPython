from math import prod
from flask import Flask
import json
import requests
from bs4 import BeautifulSoup
data=[]
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }

app = Flask(__name__)

@app.route("/trendyol")
def getDataTrendyol():
    urlId=1
    for i in range(1):
        url="https://www.trendyol.com/cep-telefonu-x-c103498?pi="+str(urlId)
        page=requests.get(url, headers=headers)
        htmlPage= BeautifulSoup(page.content,'html.parser')
        products=htmlPage.find_all("div", class_="p-card-chldrn-cntnr")
        for product in products:
            link="https://www.trendyol.com"+product.find("a").get("href")
            productData={"productUrl":"", "productName":"", "productPrice":"", "productImageUrl":{}, "productDetail":{}}
            page=requests.get(link, headers=headers)
            productPage= BeautifulSoup(page.content,'html.parser')
            imagesProduct=productPage.find_all("img")
            for imageProduct in imagesProduct:
                productData["productImageUrl"][imageProduct.get("alt")]=imageProduct.get("src")
            productData["productUrl"]=link
            productData["productName"]=(productPage.find("h1", class_="pr-new-br").getText())
            productData["productPrice"]=(float(productPage.find("span", class_="prc-dsc").getText().split("TL")[0].replace(".","").replace(",",".")))
            productsDetail=productPage.find_all("li", class_="detail-attr-item")
            for productDetail in productsDetail:
                productData["productDetail"][productDetail.find("span").getText()]=(productDetail.find("b").getText())
            data.append(productData)
        urlId+=1
        
if __name__ == "__main__":
    app.run(debug=True)

