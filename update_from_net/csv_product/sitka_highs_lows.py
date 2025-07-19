import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'study/update_from_net/data/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件头中提取日期和最高温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')  # 日期在第一列
        high = int(row[1])  # 最高温度在第二列
        low = int(row[3])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # 打印文件头及其位置
    for index, column_header in enumerate(header_row):
        print(index, column_header)

#print(highs)

# 绘制最高和最低温度的图形
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形格式
ax.set_title("Daily high and low temperatures, 2014", fontsize=24)
ax.set_xlabel('', fontsize=16) 
fig.autofmt_xdate()  # 自动格式化日期标签
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('study/update_from_net/figures/Figure_5.png')
plt.show()