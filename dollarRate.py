# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:24:26 2019

@author: Hp
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("./37.year.dollar.rate.for.Turkey.csv",sep=';')

x = data.Day
y = data.Rate_Price

x = x.values.reshape(-1,1)
y= y.values.reshape(-1,1)
"""
#(Use for single table)
plt.scatter(x,y,c="gold",s=3) 
plt.xlabel("Rate_Price")
plt.ylabel("Day")
plt.show()
"""
#Lineer Regresyon
estimateLinear = LinearRegression()
estimateLinear.fit(x,y)
y_head_linear=estimateLinear.predict(x)

"""
#Linear Regression Table (single table)
plt.plot(x,y_head_lineer,c="red")
plt.title("Linear Regression")
plt.show()
"""

#MSE values find in Linear Regression 
MSE_Linear = 0
for i in range(len(y)):
    MSE_Linear = MSE_Linear + (float(y[i])-float(y_head_linear[i]))**2
mse_linear_value=MSE_Linear/len(y)
print("MSE value of Linear Regression : ",mse_linear_value)

#Polynomial Regression
estimatePolynomial = PolynomialFeatures(degree=3)
X_new = estimatePolynomial.fit_transform(x)
polynomial_model = LinearRegression()
polynomial_model.fit(X_new,y)
y_head_polynomial=polynomial_model.predict(X_new)

"""
#3.degrees polynomial table (single table)
plt.plot(x,y_head_polynomial,c="green")
plt.title("Polynomial Regression")
plt.show()
"""
#MSE values find in Polynomial Regression
MSE_polynomial = 0
for i in range(len(X_new)):
    MSE_polynomial = MSE_polynomial + (float(y[i])-float(y_head_polynomial[i]))**2
mse_polynomial_value=MSE_polynomial/len(X_new)
print("3th degrees MSE value of Polynomial Regression ",mse_polynomial_value)

#Finding MSE values ​​by degree
mse_array=[]
MSE_polynomial = 0
#I try the first 75 degrees. 
for a in range(75):
    estimate_polynomial = PolynomialFeatures(degree=a+1)
    X_new = estimate_polynomial.fit_transform(x)
    polynomial_model = LinearRegression()
    polynomial_model.fit(X_new,y)
    y_head_polynomial2=polynomial_model.predict(X_new)
    for i in range(len(X_new)):
        MSE_polynomial = MSE_polynomial + (float(y[i])-float(y_head_polynomial2[i]))**2
    mse_polynomial_value=MSE_polynomial/len(X_new)
    mse_array.append(mse_polynomial_value)
    print(a+1,".degrees error in function:", mse_polynomial_value)
    MSE_polynomial = 0

#Finding the degree of the smallest error value
min_value=0
for value in range(75):
    if(mse_array[value]==min(mse_array)):
        print("Minimum value:",mse_array[value]," Degree:",(value+1))
        min_value=value+1

#Modeling the polynomial that gives the best degree (4th degree)
estimate_polynomial_min = PolynomialFeatures(degree=min_value)
X_new = estimate_polynomial_min.fit_transform(x)
polynomial_model_min = LinearRegression()
polynomial_model_min.fit(X_new,y)
y_head_polynomial_min=polynomial_model_min.predict(X_new)

"""
#Modeling the polynomial that gives the best degree table (single table)
plt.plot(x,y_head_polynomial_min,c="blue")
plt.title("Polynomial Regression (the best degree)")
plt.show()
"""

"""
#Let's show all the visualizations we have done in a single table.
plt.plot(x,y_head_linear,c="red")
plt.plot(x,y_head_polynomial,c="green")
plt.plot(x,y_head_polynomial_min,c="blue")
plt.show()
"""

#I apply this process to show all the tables one by one in a single figure.
fig, axs = plt.subplots(2, 2)
axs[0, 0].scatter(x,y,c="gold",s=3)
axs[0, 1].scatter(x,y,c="gold",s=3)
axs[1, 0].scatter(x,y,c="gold",s=3)
axs[1, 1].scatter(x,y,c="gold",s=3)
plt.show()

#I entered the axis labels of the tables.
for ax in axs.flat:
    ax.set(xlabel='Day', ylabel='Rate Price')

#I hid the X tags and were able to see the tags for the top graphics
for ax in axs.flat:
    ax.label_outer()

#Table-1    
axs[0, 0].plot(x,y_head_linear,c="red")
axs[0, 0].set_title('Linear Regression')
#Table-2
axs[0, 1].plot(x,y_head_polynomial,c="green")
axs[0, 1].set_title('3th degree Polynomial Regression')
#Table-3
axs[1, 0].plot(x,y_head_polynomial_min,c="blue")
axs[1, 0].set_title('Polynomial Regression of the best degree(4)')
#Table-4 (In the last table, we do it to draw all of them.)
axs[1, 1].plot(x,y_head_linear,c="red")
axs[1, 1].plot(x,y_head_polynomial,c="green")
axs[1, 1].plot(x,y_head_polynomial_min,c="blue")
axs[1, 1].set_title('Combination of 3 Tables')
plt.show()

#Difference between real value and estimated value (for 520th row)
print("Real Value:",y[520]," Estimated Value:",y_head_polynomial_min[520])
print("Difference between real value and estimated value:",(float(y[520])-float(y_head_polynomial_min[520])))
