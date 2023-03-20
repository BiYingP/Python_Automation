from selenium import webdriver
import time
import yagmail
import os

def get_driver():
	# set options to make browsing easier
	options = webdriver.ChromeOptions()
	options.add_argument("disable-infobars")
	options.add_argument("start-maximized")
	options.add_argument("disable-dev-shm-usage")
	options.add_argument("no-sandbox")
	options.add_experimental_option("excludeSwitches",["enable-automation"])
	options.add_argument("disable-blink-features=AutomationControlled")

	driver = webdriver.Chrome(options=options)
	driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
	
	return driver

def clear_text(text):
	res = float(text.split(" ")[0])
	return res

def send_email(text):
	sender = os.getenv("SENDER")
	receiver = os.getenv("RECEIVER")
	subject = "Re: Stock Price Change"
	contents = f"""
	Hi,

	The stock percentage has went down less than -10%.
	
	Current stock percentage is {text} %.
	
	Thank you.
	"""

	yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))
	yag.send(to=receiver, subject=subject, contents=contents)

	return yag 

def main():
	driver = get_driver()
	time.sleep(2)
	element = driver.find_element(by="xpath", value="//*[@id='app_indeks']/section[1]/div/div/div[2]/span[2]")
	
	text = clear_text(element.text)
	if (text < - 0.10):
		send_email(text)

if __name__== "__main__":
	main()
		
