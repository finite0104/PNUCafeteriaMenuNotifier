import logging
import logging.handlers
import os

def loggingInit() :
    # 로그 저장할 폴더 생성
    current_dir = os.path.dirname(os.path.realpath(__file__))
    log_dir = '{}/logs'.format(current_dir)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 로거 생성
    crawlerLogger = logging.getLogger('MenuCrawler') # 로거 이름: MenuCrawler
    crawlerLogger.setLevel(logging.INFO) # 로깅 수준: INFO

    # 핸들러 생성
    file_handler = logging.handlers.TimedRotatingFileHandler(
    filename='menu-crawler.log', when='midnight', interval=1,  encoding='utf-8'
    ) # 자정마다 한 번씩 로테이션
    file_handler.suffix = '%Y%m%d' # 로그 파일명 날짜 기록 부분 포맷 지정 

    crawlerLogger.addHandler(file_handler) # 로거에 핸들러 추가
    formatter = logging.Formatter(
    '[%(asctime)s] [%(filename)s:%(lineno)d] - (%(levelname)s) : %(message)s '
    )
    file_handler.setFormatter(formatter) # 핸들러에 로깅 포맷 할당