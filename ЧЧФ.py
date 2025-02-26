def human_read_format(bites):
    sizes = {
        'bites': 'Б',
        'kilobites': 'КБ',
        'megabites': 'МБ',
        'gigabites': 'ГБ'
    }
    result = ''
    size = ''
    if bites < 1024:
        result = bites
        size = 'bites'
    elif bites < 1024 ** 2:
        result = bites / 1024
        size = 'kilobites'
    elif bites < 1024 ** 3:
        result = bites / (1024 ** 2)
        size = 'megabites'
    else:
        result = bites / (1024 ** 3)
        size = 'gigabites'
    
    result = int(round(result))
    answer = '{}{}'.format(result, sizes[size])
    return answer


print(human_read_format(15000))
print(human_read_format(1023))
