#!/usr/bin/env python3
import WebCrawler
import FCMManager
import MenuCrawlerLogger
import time
from MenuCrawlerLogger import MenuCrawlerLogger

def menuCrawling() :
    WebCrawler.pnu_web_crawling()
    fcm_manager = FCMManager.FCM_Manager()
    msg_send_result = fcm_manager.send_fcm_message()
    if msg_send_result["failure"] == 0 :
        # 실패 메시지 개수가 없으면 정상 전송된것으로 판단
        logger.info("FCM Message Sending Success")
    else :
        # 실패 메시지가 있음
        fail_log_message = "FCM Message Sending Failure, Count:{}".format(msg_send_result["failure"])
        logger.warning(fail_log_message)

if __name__ == "__main__" :
    logger = MenuCrawlerLogger.__call__().get_logger()
    while(True) :
        menuCrawling()
        """
        단순 sleep 함수로 동작하도록 설정하지 않고 
        스케줄러 구현해서 구동되도록 설정
        """
        delay_time = 24 * 60 * 60
        time.sleep(delay_time)