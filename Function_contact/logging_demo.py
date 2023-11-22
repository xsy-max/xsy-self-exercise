'''
logging,给开发人员看的，html是给老大看的
日志是追加在最后的

'''
from Function_contact.getLogger import getLogger
import logging
import traceback

logger = getLogger()

try:
    1 / 0
    logger.debug('没错')  # 报错的后面代码的没有走
except Exception as e:
    logger.error(traceback.format_exc())
    logger.error('错了点啥')
