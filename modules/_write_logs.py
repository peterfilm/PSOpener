from modules import conf

from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y.%m.%d - %H:%M")


def write_log(filename_path, text):
    if conf['COMMENT_PATH']:
        path = conf['COMMENT_PATH'] + '/log.txt'
    else:
        path = conf['LAST_PATH'] + '/log.txt'
    try:
        with open(path, 'a') as file:
            filename = filename_path.split('/')[-1]
            file.write(
                f"{formatted_datetime}\n{filename} - {text} ({filename_path})\n\n")
    except Exception as e:
        print(f"Ошибка: {e}")
