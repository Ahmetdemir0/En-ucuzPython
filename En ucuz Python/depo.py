# import json
# import requests
# from bs4 import BeautifulSoup
# data=[]
# headers={
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
#     }

    
# def getProductDetail(productData):
#     page=requests.get(productData["url"], headers=headers)
#     productPage= BeautifulSoup(page.content,'html.parser')
#     imagesProduct=productPage.find_all("img")
#     for imageProduct in imagesProduct:
#         # if(productPage.find("h1", class_="pr-new-br").getText()==imageProduct.get("alt")):
#         productData["imageUrl"][imageProduct.get("alt")]=imageProduct.get("src")
#     # productData["productUrl"]=link
#     # productData["productName"]=(productPage.find("h1", class_="pr-new-br").getText())
#     # productData["productPrice"]=(float(productPage.find("span", class_="prc-dsc").getText().split("TL")[0].replace(".","").replace(",",".")))
#     productsDetail=productPage.find_all("li", class_="detail-attr-item")
#     for productDetail in productsDetail:
#         productData["detail"][productDetail.find("span").getText()]=(productDetail.find("b").getText())
#     return productData




# def getDataTrendyol():
    
#     urlId=1
#     for i in range(500):
#         url1="https://www.trendyol.com/cep-telefonu-x-c103498?pi="+str(urlId)
#         page=requests.get(url1, headers=headers)
#         htmlPage= BeautifulSoup(page.content,'html.parser')
#         try:
#             htmlPage.find("div", class_="dscrptn").getText()
#         except:
#             break
#         else:
#             products=htmlPage.find_all("div", class_="p-card-wrppr")
#             for product in products:
#                 productData={"id1":"", "name":"", "price":"","url":"", "imageUrl":{}, "detail":{}}
#                 productData["id1"]=product.get("data-id")
#                 productData["url"]="https://www.trendyol.com"+product.find("a").get("href")
#                 productData["price"]=product.find("div", class_="prc-box-dscntd").getText().split("TL")[0].replace(".","").replace(",",".")
#                 for title in product.find("div", class_="prdct-desc-cntnr-ttl-w two-line-text"):
#                     productData["name"]+=title.getText()
#                 deneme=getProductDetail(productData)
#                 # jsondata=json.dumps(productData)
#                 # requests.post("http://localhost:8080/product",jsondata)
#                 # data.append(productData)
#             urlId+=1
#     print("data")
# getDataTrendyol()

# # def kontrol(imageUrl1):
# #     return 'https' in imageUrl1