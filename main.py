import smtplib

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url="https://www.amazon.com/Apple-16-MacBook-Pro-Z0XZ0007A/dp/B08374BBQG/ref=sr_1_9?dchild=1&keywords=macbook+pro&qid=1610573034&sr=8-9"
TARGET_PRICE = 3000
from_mail = "abcde@gmail.com"
to_mail = "burhansaydin@gmail.com"
password = "asdfsadfadsf"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

price = soup.find("span", id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
title = soup.find("span", id="productTitle", class_="a-size-large product-title-word-break").getText()

price_str = price.split("$")[1]
last_price = price_str.split(",")
gathered_str = last_price[0]+last_price[1]
price_float = float(gathered_str)

if price_float < TARGET_PRICE:

    message = f"{title} is now {price_float}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(from_mail, password)
        connection.sendmail(
            from_addr=from_mail,
            to_addrs=to_mail,
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}"
        )