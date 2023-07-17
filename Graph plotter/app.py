import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [10, 12, 8, 6, 7]

plt.plot(x1, y1, label = "Line 1")

x2 = [1,2,3,4,5]
y2 = [1,3,5,6,7]

plt.plot(x2,y2, label ='Line 2')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Plot')
plt.grid(True)
plt.legend()
plt.show()
