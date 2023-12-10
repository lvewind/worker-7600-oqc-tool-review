import logging
import sys

file_log = True
log_path = r'../log.txt'

logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)

# 调用模块时,如果错误引用，比如多次调用，每次会添加Handler，造成重复日志，这边每次都移除掉所有的handler，后面在重新添加，可以解决这类问题
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)

# file log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
if file_log:
    fh = logging.FileHandler(log_path, encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

# console log
formatter = logging.Formatter('%(levelname)s - %(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

####################
#   to_file_log
####################
to_file_filelog = True
to_file_log_path = r'../to_file_log.txt'

to_file_logger = logging.getLogger('to_file_log')
to_file_logger.setLevel(logging.DEBUG)

# 调用模块时,如果错误引用，比如多次调用，每次会添加Handler，造成重复日志，这边每次都移除掉所有的handler，后面在重新添加，可以解决这类问题
while to_file_logger.hasHandlers():
    for i in to_file_logger.handlers:
        to_file_logger.removeHandler(i)

# file log
to_file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
if to_file_filelog:
    to_file_fh = logging.FileHandler(to_file_log_path, encoding='utf-8')
    to_file_fh.setLevel(logging.DEBUG)
    to_file_fh.setFormatter(to_file_formatter)
    to_file_logger.addHandler(to_file_fh)
