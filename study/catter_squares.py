import matplotlib.pyplot as plt 
 
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]  # 计算平方值

plt.style.use('seaborn-v0_8') 
fig, ax = plt.subplots() 
#ax.scatter(x_values, y_values, c='red', s=10)  # s is the size of the point
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) # 使用颜色映射n

# 设置图表的标题和标签
ax.set_title("Square", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()