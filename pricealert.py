import smtplib, time, requests as rq
from bs4 import BeautifulSoup

site = '''https://www.bookoff.pl/product-pol-118868-Bruno-Bisang-30-Years-of-Polaroids.html'''

header = {'User-Agent' : '''
	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101
	Firefox/88.0 '''}

def get_price():
	html = rq.get(site, headers=header).text
	soup = BeautifulSoup(html, 'html.parser')
	price = float(soup.find(id="projector_price_value").get_text().strip())
		
		final_price = ''.join(price)[2:8]
		final_price = int(final_price.replace(',', ''))
		
		if int(final_price) < 0,8 * int(price):
			send_email()

def send_email():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
    server.ehlo()
    
    server.login('my email adress', 'password')
    
    subject = 'The price of your product has changed'
    body = '''https://www.bookoff.pl/product-pol-118868-Bruno-Bisang-
		30-Years-of-Polaroids.html'''
    msg = f"Subject:{subject}\n\n{body}"
    
    server.sendmail("Sender's email", "Recipient's email", msg)
    print("The email has been sent!")
    server.quit()
    
while True:
    get_price()
    time.sleep(60)
