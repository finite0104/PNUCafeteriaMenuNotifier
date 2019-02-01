import WebCrawler
import FCMManager
import time

if __name__ == "__main__" :
    while(True) :
        WebCrawler.pnu_web_crawling()
        fcm_manager = FCMManager.FCM_Manager()
        msg_send_result = fcm_manager.send_fcm_message()
        print msg_send_result

        delay_time = 24 * 60 * 60
        time.sleep(delay_time)
