from modules import conf
import os

from datetime import datetime


def write_log(filename_path, text, flag):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y.%m.%d - %H:%M")
    if conf['COMMENT_PATH']:
        path = os.path.join(conf['COMMENT_PATH'], 'log.txt')
    else:
        path = os.path.join(conf['LAST_PATH'], 'log.txt')
    try:
        with open(path, 'a') as file:
            filename = os.path.normpath(filename_path)
            if not flag:
                file.write(
                    f"{formatted_datetime}\n{os.path.basename(filename)} - {text} \n\n")
            else:
                file.write(
                    f"{formatted_datetime}\n{os.path.basename(filename)} - {text} ({os.path.normpath(filename_path)})\n\n")
    except Exception as e:
        print(f"Ошибка: {e}")
