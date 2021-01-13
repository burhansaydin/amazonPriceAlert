import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url="https://www.amazon.com/Apple-16-MacBook-Pro-Z0XZ0007A/dp/B08374BBQG/ref=sr_1_9?dchild=1&keywords=macbook+pro&qid=1610573034&sr=8-9"
TARGET_PRICE = 3000
from_mail = "abcde@gmail.com"
to_mail = "burhansaydin@gmail.com"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

price = soup.find("span", id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString")

print(price.getText())
