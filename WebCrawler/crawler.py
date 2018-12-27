from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import pymongo

def func_crawling() :
	options = Options()
	options.set_headless(True)
	driver = webdriver.Firefox(options=options, executable_path='./geckodriver')
	driver.get('http://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnWeekly.do?mCode=MN203')

	html = driver.page_source
	soup = BeautifulSoup(html)
	date_string = soup.find_all("span", {"class": "loca"}).text
	date_number = soup.find_all("span", {"class": "term"}).text
	school_meal_table = soup.find_all("table", {"class": "menu-tbl"})[0]
	table_body = school_meal_table.find_all("tbody")[0]
	table_datas = table_body.find_all("tr")

	for row in table_datas :
		counter = 0
		location = row.find_all("th")[0].text
		meal_list = row.find_all("td")
		"""
		td 내부의 li 검색, 있는 경우 h3/p Tag 데이터를 저장하고 없으면 result로 없음을 Return
		counter는 조식 중식 석식 야식 구분으로 사용
		0 조식
		1 중식
		2 석식
		3 야식
		td는 최대 4까지 나올 수 있다고 가정하고 수행함
		"""
		for data in meal_list :
			result = ""
			menu_data = data.find_all("li")


	driver.quit()

if __name__ == "__main__" :
	while(True) :
		func_crawling()
		sleep(60*60*24)
