# Py Regressions

## What is py regressions ?

Py Regressions are a set of scripts to perform linear and non linear regression analysis in python. Some of them use out of the box libraries to perform regressions like scipy some do the calculations in the script itself.

## How To Use The Scripts ?

Just Call The Scripts from the commandline and the results will be printed there itself. More information about each script will be given below.

### linear_input.py

#### Introduction

This scripts uses the linear regression method to perform a linear fit of a set of points. When you run the script it will prompt you to enter the number of data points in the fit and then enter the x and y data of each point after which it calculates the slope, intercept, <a href = "https://en.wikipedia.org/wiki/Pearson_correlation_coefficient" >pearson correlation coefficient (r) </a> and <a href = "https://en.wikipedia.org/wiki/Coefficient_of_determination"> coefficient of determination (r^2) </a>. Then it plots the graph of the fitted line.

#### Theory

Linear regression is a way to model the relationship between two variables, which have a linear relationship. It is a method of estimating the parameters of a linear relationship between two variables. It is used to estimate the slope and the intercept of a line.<br>
The equation of a line is given by y = mx + c.<br>
The formula to calculate the slope is:<br>

<img src ="https://quicklatex.com/cache3/f9/ql_3871410c07f74d0794499b1ad30e1df9_l3.png"></img><br>
Where x and y are the mean of the x and y values of the data points.

#### Working

When the script is run it will prompt you to enter the number of data points in the fit. This is stored in a variable called 'n'.

```
n = int(input("Enter the number of data points: "))
```

This variable will be used later and also set the no of datapoints in the given dataset. Then we step through the loop and ask the user to enter the x and y data of each point. The data is stored in a list called for x data called x and y data called y.

```
x = []
y = []
for i in range(n):
    x.append(float(input("Enter x value: ")))
    y.append(float(input("Enter y value: ")))
```

Then we calculate the mean of both the x data and the y data.

```
x_mean = sum(x)/n
y_mean = sum(y)/n
```

Then we loop over all the data and sum of the square of the x data and the y data

```
x_sum_sq = 0
y_sum_sq = 0
for i in range(n):
    x_sum_sq += x[i]**2
    y_sum_sq += y[i]**2
```

Then we calculate the sum of the product of the x data and the y data

```
x_y_sum = 0
for i in range(n):
    x_y_sum += x[i]*y[i]
```

Now we calculate the slope of the line using the formula

```
slope = (n*x_y_sum - x_sum_sq*y_mean)/(n*x_sum_sq - x_mean**2)
```

And the intercept using the formula

```
intercept = y_mean - slope*x_mean
```

We then use the slope and intercept to calculate the y values of the fitted line

```
y_fitted = []
for i in range(n):
    y_fitted.append(slope*x[i] + intercept)
```

Using this y values we then perform the calculation of the <a href = "https://en.wikipedia.org/wiki/Pearson_correlation_coefficient" >pearson correlation coefficient (r) </a> and <a href = "https://en.wikipedia.org/wiki/Coefficient_of_determination"> coefficient of determination (r^2) </a>

First we calculate the sum of the product of the y actual data and the y fitted data, then we calculate the sum of the square of the y fitted data.

```
y_y_calc_sum = 0
y_calc_sum = 0
y_calc_sum_sq = 0
for i in range(n):
    y_calc_sum += y_line[i]
    y_calc_sum_sq += y_line[i]**2
    y_y_calc_sum += y_line[i]*y[i]
```

We then use this data to caluclate the <a href = "https://en.wikipedia.org/wiki/Pearson_correlation_coefficient" >pearson correlation coefficient (r) </a> and <a href = "https://en.wikipedia.org/wiki/Coefficient_of_determination"> coefficient of determination (r^2) </a> as follows:

```
r = (n*x_y_sum - x_sum_sq*y_mean)/(sqrt(n*x_sum_sq - x_mean**2)*sqrt(n*y_sum_sq - y_mean**2))
r_sq = (n*x_y_sum - x_sum_sq*y_mean)/(n*x_sum_sq - x_mean**2)**2
```

Finally we use the fitted line and the actual data to plot the graph

```
plt.plot(x, y, 'ro')
plt.plot(x, y_fitted)
plt.show()
```
