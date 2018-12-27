from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

def func_crawling() :
	options = Options()
	options.set_headless(True)
	driver = webdriver.Firefox(options=options, executable_path='./geckodriver')
	driver.get('http://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnWeekly.do?mCode=MN203')

	html = driver.page_source
	soup = BeautifulSoup(html)
	tableList = soup.find_all("table")

	print(len(tableList))
	driver.quit()

while(True) :
	func_crawling()
	sleep(30)
