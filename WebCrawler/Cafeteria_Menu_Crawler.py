#!/usr/bin/env python3
import WebCrawler
import FCMManager
import time
from apscheduler.schedulers.background import BackgroundScheduler

# 문제점 1 - 스케줄러가 함수 실행 이후 -> 스케줄 대기 -> 재실행 순서가 아니고 스케줄 대기 -> 실행 순서임
# 함수에 대한 우선적인 실행 방법이 필요하다.
def menu_crawling() :
    WebCrawler.pnu_web_crawling()
    msg_send_result = fcm_manager.send_fcm_message()
    print('Menu Crawling Completed')

def scheduling_test_30interval() :
    print('Scheduling - 30 Seconds')

def scheduling_test_10interval() :
    print('Scheduling - 10 Seconds')

def schedulerInitialize() :
    scheduler = BackgroundScheduler()
    scheduler.start()
    # 6시간마다 크롤링 진행할 수 있도록 프로그램 작성함
    scheduler.add_job(menu_crawling, 'interval', hours=6)

    # 테스트용 스케줄링 작업
    scheduler.add_job(scheduling_test_10interval, 'interval', seconds=10)
    scheduler.add_job(scheduling_test_30interval, 'interval', seconds=30)

if __name__ == "__main__" :
    scheduler = None
    fcm_manager = FCMManager.FCM_Manager()
    # 문제점 1에 대한 임시 대응 - 스케줄링 작업하기 전에 크롤링 작업 한번 실행
    menu_crawling()
    schedulerInitialize()
    
    try :
        while(True) :
            # Main Thread가 죽지않도록 주기적인 sleeping
            #delay_time = 24 * 60 * 60
            delay_time = 3
            time.sleep(delay_time)
    except (KeyboardInterrupt, SystemExit) :
        # scheduler none type check해서 처리하는 경우 안꺼지는 문제 있음
        scheduler.shutdown()