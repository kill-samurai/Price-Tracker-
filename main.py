from bs4 import BeautifulSoup
import requests
import smtplib
import os

MOUSE = "https://www.amazon.com/Razer-Viper-Ultralight-Ambidextrous-Gaming/dp/B08QVM2JMQ/?_encoding=UTF8&pd_rd_w=GfG1d&content-id=amzn1.sym.10f16e90-d621-4a53-9c61-544e5c741acc&pf_rd_p=10f16e90-d621-4a53-9c61-544e5c741acc&pf_rd_r=HYQZZXV333YK3D4MT8PM&pd_rd_wg=k1Nep&pd_rd_r=dfb812ed-9ce7-41f2-bb90-d98440635e94&ref_=pd_gw_exports_top_sellers_unrec"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "accept-language": "en-US,en;q=0.9"
}

EMAIL = os.environ["EMAIL"]
PASS = os.environ["PASS"]
my_email = ""

MINIMUM_PRICE = 30.00

response = requests.get(url=MOUSE, headers=HEADERS)
html = response.text
soup = BeautifulSoup(html, "html.parser")

whole_price = soup.find(name="span", class_="a-offscreen")
whole_price_text = whole_price.getText().split("$", 1)
whole_price_to_compare = float(whole_price_text[1])

if whole_price_to_compare < MINIMUM_PRICE:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        message = f"The mouse price is below ${MINIMUM_PRICE}, Purchase now!\n{MOUSE}"
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=my_email, msg=f"Subject:Mouse Price Alert!\n\n{message}")
else:
    pass


