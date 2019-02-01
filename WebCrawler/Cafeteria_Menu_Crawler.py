import WebCrawler
import FCMManager
import time

if __name__ == "__main__" :
    while(True) :
        WebCrawler.pnu_web_crawling()
        fcm_manager = FCMManager.FCM_Manager()

        delay_time = 24 * 60 * 60
        time.sleep(delay_time)
