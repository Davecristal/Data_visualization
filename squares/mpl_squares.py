import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5] 
squares = [1, 4, 9, 16, 25]

# 变量fig表示整张图片，变量ax表示图片中的各个图表，大多数情况下要使用它。
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)


# 设置图表的标题和标签
ax.set_title("Square", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()

#print(plt.style.available)