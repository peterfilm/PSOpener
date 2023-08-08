import json
from pynput import keyboard


def load_api_keys():
    '''
    Достаем файлы из настроек
    '''
    with open('config.json') as file:
        data = json.load(file)
        return data


def load_key_to_api(name, value):
    '''
    Изменяем данные в настройках config.json
    name - ключ
    value - значение
    '''
    data = load_api_keys()
    data[name] = value
    with open('config.json', "w") as file:
        json.dump(data, file, indent=2)


conf = load_api_keys()

keys = {'F1': keyboard.Key.f1, 'F2': keyboard.Key.f2,
        'F3': keyboard.Key.f3, 'F4': keyboard.Key.f4,
        'F5': keyboard.Key.f5, 'F6': keyboard.Key.f6,
        'F7': keyboard.Key.f7, 'F8': keyboard.Key.f8,
        'F9': keyboard.Key.f9, 'F10': keyboard.Key.f10,
        'F11': keyboard.Key.f11, 'F12': keyboard.Key.f12}
