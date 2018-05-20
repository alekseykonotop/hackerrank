# Time Conversion

def timeConversion(s):
    time_format = s[-2:]
    if time_format == 'PM' and s[0:2] != '12':
        s = str(int(s[:2]) + 12) + s[2:]
    elif time_format == 'AM' and s[0:2] == '12':
        s = '00' + s[2:]
    return s[:-2]


print('war_time: ', timeConversion('12:05:50PM'))