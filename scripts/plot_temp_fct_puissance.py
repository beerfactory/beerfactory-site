# -*- coding: utf8 -*-
import numpy as np
import matplotlib.pyplot as plt


r = np.arange(1000.0, 8100.0, 100.0)

def f(m,t):
	'''Temps nécessaire pour élever la température d''une masse d''eau m de 1°C en fonction de la puissance de chauffe'''
	return ((m*1000.0*4.185)/t)/60.

plt.plot(r, f(20,r), 'b', label='20 l')
plt.plot(r, f(50,r), 'g', label='50 l')
plt.plot(r, f(70,r), 'r', label='70 l')
plt.plot(r, f(100,r), 'c', label='100 l')
plt.axhline(y=1,linestyle=':')
#Intersection 20l
plt.axvline(x=1395., ymax=0.15, linestyle=':')
plt.plot(1395.,1., 'o')
plt.annotate('1395W', xy=(1395., 1.0), xytext=(1595., 1.5),
	arrowprops=dict(facecolor='black', shrink=0.1))
#Intersection 50l
plt.axvline(x=3487.5, ymax=0.15, linestyle=':')
plt.plot(3487.5,1., 'o')
plt.annotate('3487W', xy=(3487.5, 1.0), xytext=(3687., 1.5),
	arrowprops=dict(facecolor='black', shrink=0.1))
#Intersection 70l
plt.axvline(x=4882.5, ymax=0.15, linestyle=':')
plt.plot(4882.5,1., 'o')
plt.annotate('4882W', xy=(4882.5, 1.0), xytext=(5082., 1.5),
	arrowprops=dict(facecolor='black', shrink=0.1))
#Intersection 100l
plt.axvline(x=6975., ymax=0.15, linestyle=':')
plt.plot(6975.,1., 'o')
plt.annotate('6975W', xy=(6975., 1.0), xytext=(7175., 1.5),
	arrowprops=dict(facecolor='black', shrink=0.1))

plt.xlabel('Puissance (W)')
plt.ylabel('Temps (min)')
plt.legend()
#plt.show()
plt.savefig("../content/images/temp_fct_puissance.png")