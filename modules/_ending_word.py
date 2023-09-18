def ending_count(cnt):
    if cnt % 100 in [11, 12, 13, 14]:
        return f'{cnt} фотографий'
    elif cnt % 10 == 1:
        return f'{cnt} фотография'
    elif cnt % 10 in [2, 3, 4]:
        return f'{cnt} фотографии'
    else:
        return f'{cnt} фотографий' 