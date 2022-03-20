# take inputs from the user in the form of x and y data store the x and y data in list
# and then perform a linear regression on the data
# and then print the slope and intercept of the line
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