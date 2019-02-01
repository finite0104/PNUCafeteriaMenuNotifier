#!/usr/bin/env python3
import WebCrawler
import FCMManager
import time

if __name__ == "__main__" :
    while(True) :
        WebCrawler.pnu_web_crawling()
        fcm_manager = FCMManager.FCM_Manager()
        msg_send_result = fcm_manager.send_fcm_message()
        print (msg_send_result)

        """
        단순 sleep 함수로 동작하도록 설정하지 않고 
        스케줄러 구현해서 구동되도록 설정
        """
        delay_time = 24 * 60 * 60
        time.sleep(delay_time)
