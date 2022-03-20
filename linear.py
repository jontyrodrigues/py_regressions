import matplotlib.pyplot as plt
print("This program will perform a linear regression on the data you enter")
x = []
y = []
n = int(input("Enter the number of data points: "))
for i in range(n):
    x.append(float(input("Enter x value: ")))
    y.append(float(input("Enter y value: ")))
# calculate the mean of the x and y data
x_mean = sum(x)/n
y_mean = sum(y)/n
# calculate the sum of the x and y data
x_sum = 0
y_sum = 0
for i in range(n):
    x_sum += x[i]
    y_sum += y[i]
# calculate the sum of the x and y data squared
x_sum_sq = 0
y_sum_sq = 0
for i in range(n):
    x_sum_sq += x[i]**2
    y_sum_sq += y[i]**2
# calculate the sum of the product of x and y data
x_y_sum = 0
for i in range(n):
    x_y_sum += x[i]*y[i]
# calculate the slope and intercept
slope = (n*x_y_sum - x_sum*y_sum)/(n*x_sum_sq - x_sum**2)
intercept = y_mean - slope*x_mean
# print the slope and intercept
print("The slope of the line is: ", slope)
print("The intercept of the line is: ", intercept)
# using the slope and intercept calculate the y values of the line for the x values
y_line = []
for i in range(n):
    y_line.append(slope*x[i]+intercept)
# calculate the pearson correlation coefficient
y_y_calc_sum = 0
y_calc_sum = 0
y_calc_sum_sq = 0
# calculate the sum of the y_line data
for i in range(n):
    y_calc_sum += y_line[i]
    y_calc_sum_sq += y_line[i]**2
    y_y_calc_sum += y_line[i]*y[i]
r = (n*y_y_calc_sum - y_calc_sum*y_sum)/((n*y_sum_sq - y_sum**2)*(n*y_calc_sum_sq - y_calc_sum**2))**0.5
# print the pearson correlation coefficient
print("The pearson correlation coefficient is: ", r)
# calculate the r squared
r_sq = r**2
# print the r squared
print("The r squared is: ", r_sq)
# plot the data and the line
plt.plot(x,y,'ro')
plt.plot(x,y_line)
plt.show()
