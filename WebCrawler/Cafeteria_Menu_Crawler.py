#!/usr/bin/env python3
import WebCrawler
import FCMManager
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def timed_job():
    print('Test Interval')

def menu_crawling() :
    WebCrawler.pnu_web_crawling()
    msg_send_result = fcm_manager.send_fcm_message()
    print('Menu Crawllllllling~~~')

def mainInit() :
    scheduler.add_job(timed_job, 'interval', seconds=30)
    #6시간마다 크롤링 진행할 수 있도록 프로그램 작성
    scheduler.add_job(menu_crawling, 'interval', hours=6)
    scheduler.start()

if __name__ == "__main__" :
    scheduler = BlockingScheduler()
    fcm_manager = FCMManager.FCM_Manager()
    
    try :
        while(True) :
            # Main Thread가 죽지않도록 주기적인 sleeping
            #delay_time = 24 * 60 * 60
            delay_time = 5
            time.sleep(delay_time)
    except (KeyboardInterrupt, SystemExit) :
        scheduler.shutdown()