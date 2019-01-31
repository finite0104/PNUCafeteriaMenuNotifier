from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import MongoDBManager

"""
	문자열 처리 함수
"""
def modify_menu_text(text) :
	#텍스트 끝 두 자리가 ', '이면 그 문자열을 없애도록 함
	if text.rfind(', ') == (len(text) - 2) :
		result = text[:-2]
	else :
		result = text
	return result

def count_to_time(count) :
	return {
		0 : "조식",
		1 : "점심",
		2 : "저녁",
		3 : "야식"
	}.get(count, "점심")

"""
	크롤링 수행 함수
"""
def pnu_web_crawling() :
	try :
		options = Options()
		options.set_headless(True)
		driver = webdriver.Firefox(options=options, executable_path='./geckodriver')
		driver.get('http://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnWeekly.do?mCode=MN203')

		html = driver.page_source
		soup = BeautifulSoup(html)
		date_string = soup.find_all("span", {"class": "loca"})[0].text
		date_number = soup.find_all("span", {"class": "term"})[0].text
		school_meal_table = soup.find_all("table", {"class": "menu-tbl"})[0]
		table_body = school_meal_table.find_all("tbody")[0]
		table_datas = table_body.find_all("tr")

		for row in table_datas :
			counter = 0
			location = row.find_all("th")[0].text.replace('\t', '').replace('\n', '')
			meal_list = row.find_all("td")
			for data in meal_list :
				time = count_to_time(counter)
				menu_data = data.find_all("li")
				if(len(menu_data) == 0) :
					result = "식단 없음"
					MongoDBManager.non_menu_data_insert(counter, date_string, date_number, location, time, result)
				else :
					for data in menu_data :
						#메뉴 제목 존재여부 판별 후, 없으면 임의로 입력함
						if(data.h3 != None) :
							title = data.h3.text.replace(' ', '')
						else :
							title = "메뉴"
						#식단 데이터의 잘못된 comma 삭제하는 함수 실행, 결과값을 가져옴
						menu = modify_menu_text(data.p.text.replace('\n', ', '))

						#메뉴에 가격이 있는경우, 가격도 저장될 수 있도록 설정
						if title.find('-') != -1 :
							#가격 있는 경우 --> split 수행하고, 데이터 저장
							title_array = title.split('-')
							MongoDBManager.menu_exchange_data_insert(counter, date_string,
																	 date_number, location, time,
																	 title_array[0], title_array[1], menu)
						else :
							MongoDBManager.menu_data_insert(counter, date_string, date_number,
															location, time, title, menu)

				print('데이터 입력 : ' + location + ' - ' + time)
				counter = counter + 1
	finally :
		driver.quit()