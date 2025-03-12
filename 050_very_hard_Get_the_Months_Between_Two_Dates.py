"""
Get the Months Between Two Dates
Create a function that, given 2 dates, returns the names of the months that are present between them (inclusive).

Examples
Input

 january = datetime.date(2017, 1, 1)
 march = datetime.date(2017, 3, 1)

monthsInterval(january, march)
Output

['January', 'February', 'March']
Input

 december = datetime.date(2017, 12, 1)
 january = datetime.date(2018, 1, 1)

monthsInterval(december, january)
Output

['January', 'December']
Input

 january2017 = datetime.date(2017, 0, 1)
 january2018 = datetime.date(2018, 0, 1)

monthsInterval(january2017, january2018)
Output

['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
(Notice that January is not duplicated!)

Notes
The returned list should include the months of dateStart and dateEnd (inclusive)
The returned list must not include duplicate values
The month names returned by the function should be sorted (not alphabetically, but ordered by which comes first (January = 1st month, February = 2nd month, … , December = 12th month))
The function should produce the same output even if dateStart is greater than dateEnd
"""

import datetime

def months_interval(date1, date2):
    # 1. 受け取った2つの日付のうち、早い方をstart,　遅い方をendにする
    if date1 > date2:
        date1, date2 = date2, date1
    
    # 2. 1月から12月までの月の名前の一覧を作成する
    month_names =  ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    
    result = []
    
    # 3. startの日付からendの日付まで、月ごとにループするための準備
    current_year = date1.year
    current_month = date1.month
    
    # (年, 月)の組み合わせで比較することで、endの日付（月単位）に達するまでループを続ける
    while (current_year, current_month) <= (date2.year, date2.month):
        month = month_names[current_month - 1]
        if month not in result:
            result.append(month)
            
        # 5. 次の月に進む（12月の場合は翌年の1月へ）
        if current_month == 12:
            current_month = 1
            current_year += 1
        else:
            current_month += 1
    
    
    # 6. 結果のリストをカレンダー順（1月～12月）に並び替える
    result.sort(key=lambda m: month_names.index(m))
    return result
    
    
print(months_interval(datetime.date(2017, 1, 1), datetime.date(2017, 1, 1))) # ['January'])
print(months_interval(datetime.date(2016, 1, 1), datetime.date(2017, 1, 1))) # ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
print(months_interval(datetime.date(2017, 1, 1), datetime.date(2016, 1, 1))) # ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
print(months_interval(datetime.date(2017, 4, 1), datetime.date(2017, 8, 1))) # ['April', 'May', 'June', 'July', 'August'])
print(months_interval(datetime.date(2017, 8, 1), datetime.date(2017, 4, 1))) # ['April', 'May', 'June', 'July', 'August'])
print(months_interval(datetime.date(2017, 12, 1), datetime.date(2018, 1, 1))) # ['January', 'December'])
print(months_interval(datetime.date(2018, 1, 1), datetime.date(2017, 12, 1))) #['January', 'December'])
print(months_interval(datetime.date(2017, 4, 1), datetime.date(2019, 4, 1))) # ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
print(months_interval(datetime.date(2019, 4, 1), datetime.date(2017, 4, 1))) # ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
print(months_interval(datetime.date(2017, 4, 1), datetime.date(2043, 10, 1))) # ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
print(months_interval(datetime.date(2043, 10, 1), datetime.date(2017, 4, 1))) # ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])