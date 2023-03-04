import json
import requests
from bs4 import BeautifulSoup
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }

def getDataN11():
    urlId=1
    for i in range(1000):
        page=requests.get("https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?pg="+str(urlId), headers=headers)
        htmlPage= BeautifulSoup(page.content,'html.parser')
        products=htmlPage.find_all("li", class_="column")
        try:
            htmlPage.find("div", class_="resultText").getText()
        except:
            break
        else:
            for product in products:
                productData={"platformId":"","platformName":"N11", "name":"", "price":"","url":"", "imageUrl":"", "detail":{},"category":{"id":"5cd02b6d-e592-6cb6-7ca9-43f3cb23274a"}}
                productData["id1"]=product.find("a").get("data-id")
                productData["url"]=product.find("a").get("href")
                productData["price"]=product.find("ins").getText().split("TL")[0].replace(".","").replace(",",".")
                productData["name"]+=product.find("a").get("title")
                productData["imageUrl"]=product.find("img").get("data-original")
                jsondata=json.dumps(getProductDetail(productData))
                jsondata=json.dumps(productData)
                requests.post("http://localhost:8080/product",jsondata)
            urlId+=1
    print("data")
    
def getProductDetail(productData):
    page=requests.get(productData["url"], headers=headers)
    productPage= BeautifulSoup(page.content,'html.parser')
    productsDetail=productPage.find_all("li", class_="unf-prop-list-item")
    for productDetail in productsDetail:
        if productDetail.find_all("p")[1].get("a"):
            break
        else:
            productData["detail"][productDetail.find_all("p")[0].getText()]=productDetail.find_all("p")[1].getText()
    return productData
getDataN11()