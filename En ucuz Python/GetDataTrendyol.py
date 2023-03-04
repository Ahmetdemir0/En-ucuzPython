import json
import requests
from bs4 import BeautifulSoup
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
    
def getProductDetail(productData):
    page=requests.get(productData["url"], headers=headers)
    productPage= BeautifulSoup(page.content,'html.parser')
    imagesProduct=productPage.find_all("img")
    for imageProduct in imagesProduct:
        try:
            imageProduct.get("alt")
        except:
            continue
        else:
            if imageProduct.get("alt").replace(" ","") == productData["name"].replace(" ",""):
                productData["imageUrl"]=imageProduct.get("src")
                break
    productsDetail=productPage.find_all("li", class_="detail-attr-item")
    for productDetail in productsDetail:
        productData["detail"][productDetail.find("span").getText()]=(productDetail.find("b").getText())
        print(productData)
    return productData




def getDataTrendyol():
    print("data")
    
    urlId=1
    for i in range(500):
        url1="https://www.trendyol.com/cep-telefonu-x-c103498?pi="+str(urlId)
        page=requests.get(url1, headers=headers)
        htmlPage= BeautifulSoup(page.content,'html.parser')
        try:
            htmlPage.find("div", class_="dscrptn").getText()
        except:
            break
        else:
            products=htmlPage.find_all("div", class_="p-card-wrppr")
            for product in products:
                productData={"platformId":"", "name":"", "platformName":"Trendyol", "price":"","url":"", "imageUrl":"", "detail":{},"category":{"id":"5cd02b6d-e592-6cb6-7ca9-43f3cb23274a"}}
                productData["id1"]=product.get("data-id")
                productData["url"]="https://www.trendyol.com"+product.find("a").get("href")
                productData["price"]=product.find("div", class_="prc-box-dscntd").getText().split("TL")[0].replace(".","").replace(",",".")
                for title in product.find("div", class_="prdct-desc-cntnr-ttl-w two-line-text"):
                    productData["name"]+=title.getText()+" "
                jsondata=json.dumps(getProductDetail(productData))
                requests.post("http://localhost:8080/product",jsondata)
            urlId+=1
    print("data")
getDataTrendyol()
