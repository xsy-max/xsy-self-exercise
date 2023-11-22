if __name__ == '__main__':
    years = input('请输入年份')
    if years.isdigit():
        # years.isdigit() == 1:
        years = int(years)
        if (years / 4 == 0 and years / 100 != 0) or years / 400 == 0:
            print(f'{years}是闰年，输出闰年的日历为')
            print('''
                1月1日
                ''')
        else:
            print(f'{years}不是闰年,输出不是闰年的日历')
            print('''
            日历
            ''')
    else:
        print('输入内容非法')
