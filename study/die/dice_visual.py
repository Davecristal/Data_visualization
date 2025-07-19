# 同时掷两个骰子
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建一个6面的骰子
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()  # 两个骰子的点数之和
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]
        
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency'}
my_layout = Layout(title='Results of rolling two D6 1000 times', 
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='two_d6.html')

#print(frequencies) # 输出每个点数出现的频率