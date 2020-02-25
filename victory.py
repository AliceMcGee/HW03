months = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

days = {
    '01': 'первое',
    '02': 'втрое',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое',
    '12': 'двенадцатое'
}



data = '04.05.1955'
day, month, year = data.split('.')
d = 'все_равно_какого_дня'
if day in days.keys():
    d = day

print(d, months[month], year, 'года')