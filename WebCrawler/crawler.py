from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import pymongo

def func_crawling() :
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
				menu_data = data.find_all("li")
				if(len(menu_data) == 0) :
					result = "식단 없음"
					non_menu_data_insert(date_string, date_number, location, counter, result)
				else :
					for data in menu_data :
						if(data.h3 != None) :
							title = data.h3.text.replace(' ', '')
						else :
							title = "메뉴"
						menu = data.p.text.replace('\n', ', ')
						print(menu.rfind(', '))
						print((len(menu)-1))
						print(menu.rfind(', ') == (len(menu)-1))
						#메뉴에 가격이 있는경우, 가격도 저장될 수 있도록 설정
						if title.find('-') != -1 :
							#가격 있는 경우 --> split 수행하고, 데이터 저장
							title_array = title.split('-')
							menu_exchange_data_insert(date_string, date_number, location, counter,
													  title_array[0], title_array[1], menu)
						else :
							menu_data_insert(date_string, date_number, location, counter, title, menu)

				counter = counter + 1
	finally :
		driver.quit()

def count_to_time(count) :
	return {
		0 : "조식",
		1 : "점심",
		2 : "저녁",
		3 : "야식"
	}.get(count, "점심")

def non_menu_data_insert(date_string, date_number, location, count, result) :
	#식단 없을 때 데이터 저장 함수
	conn = pymongo.MongoClient("localhost", 27017)
	db = conn.meal_data
	collection = db[date_number]

	time = count_to_time(count)
	if count == 0 :
		#데이터 생성
		collection.insert(
			{
				'day' : date_string,
				'date' : date_number,
				'location' : location,
				'arr_menu' : [
					{
						'time' : time,
						'name' : result
					}
				]
			}
		)
		print(time + ' : ' + result)
	else :
		#데이터 추가(array 부분에)
		collection.update(
			{
				'date' : date_number,
				'location' : location
			},
			{
				 '$push' : {
					'arr_menu' : {
						'time' : time,
						'name' : result
					}
				 }
			}
		)
		print(time + ' : ' + result)

	conn.close()

def menu_data_insert(date_string, date_number, location, count, name, menu) :
	#식단 데이터만 저장하는 함수(가격 x)
	conn = pymongo.MongoClient("localhost", 27017)
	db = conn.meal_data
	collection = db[date_number]

	time = count_to_time(count)
	if count == 0 :
		#데이터 생성
		collection.insert(
			{
				'day' : date_string,
				'date' : date_number,
				'location' : location,
				'arr_menu' : [
					{
						'time' : time,
						'name' : name,
						'menu' : menu
					}
				]
			}
		)
		print(time + ' : ' + name)
	else :
		#데이터 추가(array 부분에)
		collection.update(
			{
				'date' : date_number,
				'location' : location
			},
			{
				'$push' : {
					'arr_menu' : {
						'time' : time,
						'name' : name,
						'menu' : menu
					}
				}
			}
		)
		print(time + ' : ' + name)

	conn.close()

def menu_exchange_data_insert(date_string, date_number, location, count, name, exchange, menu) :
	#식단 및 가격 데이터 저장 함수
	conn = pymongo.MongoClient("localhost", 27017)
	db = conn.meal_data
	collection = db[date_number]

	time = count_to_time(count)
	if count == 0 :
		#데이터 생성
		collection.insert(
			{
				'day' : date_string,
				'date' : date_number,
				'location' : location,
				'arr_menu' : [
					{
						'time' : time,
						'name' : name,
						'cost' : exchange,
						'menu' : menu
					}
				]
			}
		)
		print(time + ' : ' + name)
	else :
		#데이터 추가(array 부분에)
		collection.update(
			{
				'date' : date_number,
				'location' : location
			},
			{
				'$push' : {
					'arr_menu' : {
						'time' : time,
						'name' : name,
						'cost' : exchange,
						'menu' : menu
					}
				}
			}
		)
		print(time + ' : ' + name)

	conn.close()

if __name__ == "__main__" :
	while(True) :
		func_crawling()
		sleep(60*60*24)