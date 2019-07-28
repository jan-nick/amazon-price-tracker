import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/Samsung-C49HG90DMU-Monitor-Display-mattschwarz/dp/B073RJQXB1/ref=sr_1_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=ultra+wide+screen&qid=1563960170&s=gateway&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])

    if(converted_price < 700):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('evilmanky@gmail.com', 'ihhhdwfpduootflo')

    subject = 'Price fell down!'
    body = 'Price fell! Check: https://www.amazon.de/Samsung-C49HG90DMU-Monitor-Display-mattschwarz/dp/B073RJQXB1/ref=sr_1_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=ultra+wide+screen&qid=1563960170&s=gateway&sr=8-2'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'evilmanky@gmail.com',
        'janicklas@keemail.me',
        msg
    )
    print('Email has been sent!')

    server.quit()

while(True):
    check_price()
    time.sleep(3600)