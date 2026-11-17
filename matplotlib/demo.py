from turtle import lt

import matplotlib.pyplot as plt

#create a simple line plot
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# plt.plot(x, y)
# plt.show()


#customizing the plot
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# plt.plot(x, y, color='red', linestyle='--', marker='o', label='Line 1',linewidth=2, markersize=8)
# plt.title('Simple Line Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
# plt.figure(figsize=(4, 2))  #---->>specify the size of the figure


#multiple lines and legends 
# x = [1, 2, 3, 4, 5]
# y1 = [2, 4, 6, 8, 10]
# y2 = [1, 3, 5, 7, 9]
# plt.plot(x,y1, label='Line 1', color='blue', linewidth=2)
# plt.plot(x,y2, label='Line 2', color='green', linewidth=2)
# plt.title('Multiple Lines Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()
# plt.show()


#bar chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.bar(x, y)
plt.title('Simple Bar Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
