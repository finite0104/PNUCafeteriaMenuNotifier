import pymongo
import logging

"""
	MongoDB 데이터 저장 함수
"""
def non_menu_data_insert(_id, date_string, date_number, location, time, result) :
    #식단 없을 때 데이터 저장 함수
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.meal_data
    collection = db[date_number]

    if _id == 0 :
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

    conn.close()

def menu_data_insert(_id, date_string, date_number, location, time, name, menu) :
    #식단 데이터만 저장하는 함수(가격 x)
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.meal_data
    collection = db[date_number]

    if _id == 0 :
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

    conn.close()

def menu_exchange_data_insert(_id, date_string, date_number, location, time, name, exchange, menu) :
    #식단 및 가격 데이터 저장 함수
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.meal_data
    collection = db[date_number]

    if _id == 0 :
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

    conn.close()

def get_push_device_tokens() :
    #알림 보낼 디바이스 토큰들 가져오는 함수
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.user_ids
    collection = db['user_token']

    device_token = []
    for data in collection.find() :
        device_token.append(data['token_value'])
    
    info_log_msg = "Get Device Tokens - Token Counts : {}".format(len(device_token))
    logging.info(info_log_msg)

    conn.close()
    return device_token