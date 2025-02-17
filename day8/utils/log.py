import datetime
import os
import sys
# 使用指南：https://betterstack.com/community/guides/logging/loguru/#getting-started-with-loguru
from loguru import logger

from dotenv import load_dotenv

load_dotenv(verbose=True)

# logs/xx.log
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
LOG_PATH = os.path.join(ROOT_PATH, 'logs')

logger.remove(0)
if os.getenv("CONSOLE_PRINT") == "true":
    logger.add(sink=sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}", level="INFO")
# 设置日志文件
log_filename = datetime.datetime.now().strftime("%Y%m%d")
logger.add(sink=os.path.join(LOG_PATH, f"{log_filename}.log"),
           format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}", level="INFO")
