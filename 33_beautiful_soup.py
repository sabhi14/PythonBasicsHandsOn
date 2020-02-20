from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as req
import time
import xlsxwriter as xlsx


workbook = xlsx.Workbook("Flipkart_Mobile.xlsx")
worksheet = workbook.add_worksheet("Flipkart_Mobiles")
cellRow = 0
cellCol = 0
worksheet.write(cellRow,cellCol,"Mobile Name")
worksheet.write(cellRow,cellCol+1,"Price")
cellRow+=1

for i in range(1,48) :
    url = "https://www.flipkart.com/search?q=mobiles&page="+str(i)
    uclient = req(url)
    page = uclient.read()
    uclient.close()

    pagesoup = soup(page,'html.parser')
    allMobileHtml = pagesoup.findAll("div",{"class":"_3wU53n"})
    allMobilePriceHtml = pagesoup.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
    #print(allMobilePriceHtml)

    print("{:-^80}.Page ",i)

    counter=0
    while counter< len(allMobileHtml):
        eachtitlediv=allMobileHtml[counter]
        eachtitleprice=allMobilePriceHtml[counter]
        print(eachtitlediv.text+"      "+eachtitleprice.text)
        worksheet.write(cellRow,cellCol,eachtitlediv.text)
        worksheet.write(cellRow,cellCol+1,eachtitleprice.text)
        cellRow+=1
        counter+=1
    time.sleep(3)

workbook.close()
