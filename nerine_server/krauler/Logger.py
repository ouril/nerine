#!/usr/bin/env python
# coding: utf-8


import logging


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('log.txt')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(funcName)s in %(filename)s wrote: %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)






# import threading
# from _datetime import datetime
# from collections import Iterable
#
#
# def write_log(res):
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     lock = threading.Lock()
#     with lock:
#         f = open('log.txt', 'a+', encoding='utf-8')
#
#         if len(res) == 2:
#             f.write(now + ' Краулер выполнил запрос к базе:\n')
#             f.write(res[1] + '\n')
#             f.write('База вернула результат:\n')
#             if isinstance(res[0], Iterable):
#                 for t in res[0]:
#                     f.write(str(t) + '\n')
#             else:
#                 f.write(res[0])
#             f.write('\n')
#         elif len(res) == 3:
#             f.write(now + ' Краулер выполнил запрос к базе:\n')
#             argums = ' '.join(map(lambda x: str(x), res[2]))
#             f.write(res[1] + ' аргументы: ' + argums + '\n')
#             f.write('База вернула результат: ' +
#                     str(res[0]) + '\n')
#             f.write('\n')
