import logging
import os
from datetime import datetime

def setup_logger(log_dir="logs", log_level=logging.DEBUG, log_to_console=True):
    """
    配置日志记录器

    :param log_dir: 日志文件保存的目录，默认为 "logs"
    :param log_level: 日志等级，默认为 logging.DEBUG
    :param log_to_console: 是否将日志输出到控制台，默认为 True
    :return: 配置好的日志记录器
    """
    # 创建日志目录（如果不存在）
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 按照当前时间生成日志文件名
    log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
    log_filepath = os.path.join(log_dir, log_filename)

    # 配置日志格式
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)

    # 创建日志记录器
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # 添加文件处理器
    file_handler = logging.FileHandler(log_filepath)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 如果需要输出到控制台，添加控制台处理器
    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# # 示例用法
# if __name__ == "__main__":
#     # 配置日志记录器
#     logger = setup_logger(log_dir="my_project_logs", log_level=logging.INFO)

#     # 记录日志
#     logger.debug("这是一条调试信息")  # 不会被记录，因为日志等级是 INFO
#     logger.info("这是一条普通信息")
#     logger.warning("这是一条警告信息")
#     logger.error("这是一条错误信息")
#     logger.critical("这是一条严重错误信息")