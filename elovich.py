import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

x = pd.read_csv('data.csv')
def Ce(x,a0,b0):
    return ((np.log(a0*b0))/b0) + ((1/b0)*np.log(x))

guess = [2303394.537,0.011343129]
popt, pcov = curve_fit(Ce, x['time [sec]'], x['Ce [mg/L]'], guess)
y = np.empty(1000)

for i in range(1000):
    x_tmp = np.linspace(x['time [sec]'].min(),x['time [sec]'].max(),1000)
    y[i] = Ce(x_tmp[i],popt[0],popt[1])

print('a0 = %.12f' % popt[0], 'b0 = %.12f' % popt[1])
y_pred = []
for i in range(len(x['time [sec]'])):
    y_pred.append(Ce(x['time [sec]'][i],popt[0],popt[1]))
print('R2 = %.12f' % r2_score(x['Ce [mg/L]'],y_pred))
plt.plot(x['time [sec]'],x['Ce [mg/L]'],'r.')
plt.plot(x_tmp,y,'b-')
plt.show()

