from datetime import date, timedelta
youbi = '月火水木金土日'
start = date(2022, 8, 15)
for d in range(14):
    cur = start + timedelta(days=d)
    wd = cur.weekday()
    print(cur, youbi[wd])
