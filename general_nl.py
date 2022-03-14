import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

x = pd.read_csv('data.csv')

number_of_parameters = int(input('Enter number of parameters: '))
parameters = {}
for i in range(number_of_parameters):
    parameters[str(input('Enter name of parameter '+str(i)+': '))] = float(input('Enter value of parameter '+str(i)+': '))
fun = input('Enter a function: ')

guess = []
keys = {}
j = 0
for key in parameters:
    guess.append(parameters[key])
    keys[key] = parameters[key]

def funct(x_val, *param):
    exec_fun = fun
    for key in parameters:
        j = list(keys.keys()).index(key)
        exec_fun = exec_fun.replace(key,str(param[j]))
    exec_fun = exec_fun.replace('var','x_val')
    return eval(exec_fun)

def funct_2(x_val, *param):
    exec_fun = fun
    if isinstance(param[0], np.ndarray):
        param = param[0]
    for key in parameters:
        j = list(keys.keys()).index(key)
        exec_fun = exec_fun.replace(key,str(param[j]))
    exec_fun = exec_fun.replace('var',str(x_val))
    return eval(exec_fun)


popt, pcov = curve_fit(funct, x['x [unit]'], x['y [unit]'], p0 = guess)
# print(popt)
y = np.empty(1000)
for i in range(1000):
    x_tmp = np.linspace(x['x [unit]'].min(),x['x [unit]'].max(),1000)
    y[i] = funct_2(x_tmp[i],popt)

# print('a0 = %.12f' % popt[0], 'b0 = %.12f' % popt[1])
for key in parameters:
    j = list(keys.keys()).index(key)
    print('%s = %.12f' % (key, popt[j]))
    
y_pred = []
for i in range(len(x['x [unit]'])):
    y_pred.append(funct_2(x['x [unit]'][i],popt))
print('R2 = %.12f' % r2_score(x['y [unit]'],y_pred))
plt.plot(x['x [unit]'],x['y [unit]'],'r.')
plt.plot(x_tmp,y,'b-')
plt.show()

