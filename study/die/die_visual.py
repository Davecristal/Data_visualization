from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建一个6面的骰子
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]
        
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency'}
my_layout = Layout(title='Results of rolling a D6 1000 times', 
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

print(frequencies) # 输出每个点数出现的频率