#!/usr/bin/env python
# coding: utf-8

# In[19]:


# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

Определить корни

Найти интервалы, на которых функция возрастает

Найти интервалы, на которых функция убывает

Построить график

Вычислить вершину

Определить промежутки, на котором f > 0

Определить промежутки, на котором f < 0


# In[21]:


from sympy import *
from sympy.abc import x

expr = -12*(x**4)*sin(cos(x))-18*x**3+5*x**2+10*x-30
precision = 100
start = -3
end = 3

xs = [x/precision for x in range(start*precision, end*precision + 1)]
ys = [expr.subs(x, value) for value in xs]
points = list(zip(xs, ys))


# In[13]:


solveset(-12*(x**4)*sin(cos(x))-18*x**3+5*x**2+10*x-30, x, domain=Reals)


# In[22]:


points = list(zip(xs, ys))
increasing, decreasing = [], []
flag_increase = True
while len(points) >= 2:
    counter = 0
    if flag_increase:
        while points[counter][0] < end and points[counter + 1][1] > points[counter][1]:
            counter += 1
        if counter != 0:
            increasing.append([points[0][0], points[counter][0]])
        flag_increase = False
    else:
        while points[counter][0] < end and points[counter + 1][1] < points[counter][1]:
            counter += 1
        if counter != 0:
            decreasing.append([points[0][0], points[counter][0]])
        flag_increase = True
    del points[:counter]

print("Интервалы возрастания:")
print(*increasing)
print("Интервалы убывания:")
print(*decreasing)


# In[25]:


import matplotlib.pyplot as plt

x = [-12*x**4*sin(cos(x))-18*x**3+5*x**2+10*x-30 for x in range(-50, 51)]
y = [y for y in range(-50, 51)]
plt.plot(y, x)
plt.show()


# In[28]:


points = list(zip(xs, ys))
extrema = []
flag_incr = True
prior = points[0]
for current in points[1:]:
    if (flag_incr and prior[1] > current[1]) or (not flag_incr and prior[1] < current[1]):
        prior = current
        continue
    else:
        extrema.append(prior)
        prior = current
        flag_incr = not flag_incr

print("Точки экстремума:")
print(*extrema)


# In[27]:


points = list(zip(xs, ys))
above, below = [], []
flag_increase = False
while len(points) >= 2:
    counter = 0
    if flag_increase:
        while points[counter][0] < end and points[counter][1] > 0:
            counter += 1
        if counter != 0:
            above.append([points[0][0], points[counter - 2][0]])
        flag_increase = False
    else:
        while points[counter][0] < end and points[counter][1] < 0:
            counter += 1
        if counter != 0:
            below.append([points[0][0], points[counter - 2][0]])
        flag_increase = True
    del points[:counter]

print("Интервалы, на котором f > 0:")
print(*above)
print("Интервалы, на котором f < 0:")
print(*below)




# In[27]:
