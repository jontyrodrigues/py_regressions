import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

x = pd.read_csv('data.csv')

print("Python Program To Fit A General Non-Linear Function To A Set Of Data \n")
# Get the no of parameters in the function
number_of_parameters = int(input('Enter number of parameters: '))
parameters = {}
# Get the parameters
for i in range(number_of_parameters):
    parameters[str(input('Enter name of parameter '+str(i+1)+': '))] = float(input('Enter the initial guess of parameter '+str(i+1)+': '))
# Get the function from the user in the python format
fun = input('Enter the fitting function: ')

guess = []
keys = {}
j = 0

# The curve fit function expects guess paramters to be a list and list doesn't support indexing hence the following
for key in parameters:
    guess.append(parameters[key])
    keys[key] = parameters[key]

# The function to fit the data is defined here replacing the parameters with the guess values and then evaluating the function
# The function is evaluated for each value of x
def funct(x_val, *param):
    exec_fun = fun
    for key in parameters:
        j = list(keys.keys()).index(key)
        exec_fun = exec_fun.replace(key,str(param[j]))
    exec_fun = exec_fun.replace('var','x_val')
    return eval(exec_fun)

# This is the same function except it evaluates one function at a time
def funct_2(x_val, *param):
    exec_fun = fun
    if isinstance(param[0], np.ndarray):
        param = param[0]
    for key in parameters:
        j = list(keys.keys()).index(key)
        exec_fun = exec_fun.replace(key,str(param[j]))
    exec_fun = exec_fun.replace('var',str(x_val))
    return eval(exec_fun)

# this function gives you the optimized parameters and coefficients of covariance matrix
popt, pcov = curve_fit(funct, x['x [unit]'], x['y [unit]'], p0 = guess)

# This produces a plot of the data and the fitted function with the optimized parameters and 1000 points
y = np.empty(1000)
for i in range(1000):
    x_tmp = np.linspace(x['x [unit]'].min(),x['x [unit]'].max(),1000)
    y[i] = funct_2(x_tmp[i],popt)

# print('a0 = %.12f' % popt[0], 'b0 = %.12f' % popt[1])
# Now we print the optimized parameters
for key in parameters:
    j = list(keys.keys()).index(key)
    print('%s = %.12f' % (key, popt[j]))

# This is the R^2 value of the fit
# First we calculate the predicted values and the perform the r2_score on predicted vs actual values
y_pred = []
for i in range(len(x['x [unit]'])):
    y_pred.append(funct_2(x['x [unit]'][i],popt))
print('R2 = %.12f' % r2_score(x['y [unit]'],y_pred))
plt.plot(x['x [unit]'],x['y [unit]'],'r.')
plt.plot(x_tmp,y,'b-')
plt.show()

