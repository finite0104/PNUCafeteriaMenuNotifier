import logging
import logging.handlers
import os

class Singleton(type) :
    _instance = {}

    def __call__(cls, *args, **kwargs) :
        if cls not in cls._instance :
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class MenuCrawlerLogger(metaclass=Singleton):
    _logger = None

    def __init__(self) :
        # 로거 클래스 생성 시 작업할 내용 - 로그 폴더 생성, 로거, 행들러 생성 등 주요작업
        # Create Save Log Folder
        current_dir = os.path.dirname(os.path.realpath(__file__))
        log_dir = '{}/logs'.format(current_dir)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create Logger (Class Variable)
        self._logger = logging.getLogger('MenuCrawler')
        self._logger.setLevel(logging.INFO)

        # Create Logging Handler
        # 자정마다 로그 파일을 생성함
        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename='menu-crawler.log', when='midnight', interval=1, encoding='utf-8'
        )
        file_handler.suffix = '%U%m%d'
        file_handler.setLevel(logging.INFO)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        # Log Formatter Create and Set Formatter
        formatter = logging.Formatter(
            '[%(asctime)s] [%(filename)s:%(lineno)d] - (%(levelname)s) : %(message)s'
        )
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # Logging Handler adding
        self._logger.addHandler(file_handler)
        self._logger.addHandler(stream_handler)

    def get_logger(self) :
        # Return Logger
        return self._logger