# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:42:33 2017

@author: theau
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## paramètres

N = 2 ## nombre périodes
omega = 1 # fréquence
tau_1 = 20 # amplitude
tau_yield = 10 # en pascal
G = 10E4 # en pascal 
k = 0.5

n = 0.5 # exposant
Bi = 0.1 # adimension

Gam_1 = 5 ## np.arange(0.0, 10, 1)
gam_yield = tau_yield/G
gam_1 = Gam_1*gam_yield

gam = []
gam_dot = []

## data

time = np.arange(0.0, 2*N*3.14, 0.01)
l = len(time)
tau = tau_1*np.sin(omega*time)
tau_dot = tau_1*omega*np.cos(omega*time)


for t in range(l) :
    T = tau[t]
    T_a = np.abs(T)
    T_dot = tau_dot[t] 
    time_loop = time[t]
    
    if T_a < tau_yield :
        gam_loop = (1/G)*tau_1*np.sin(omega*time_loop)
        
        gam.append(gam_loop)
        gam_dot.append((1/G)*T_dot)
    else :
        K= ((T_a-tau_yield)/(k*T_a**n))**(1/n)
        
#        gam_loop = (1/G)*tau_1*np.sin(omega*time_loop)
#        - K*(tau_1/omega)*np.cos(omega*time_loop)
        
        gam.append((1/G)*T - K*(1/omega)*T_dot)
        gam_dot.append((1/G)*T_dot + K*T)
        

## plot

plt.figure(1)
plt.plot(time,tau,time,tau_dot)
#
plt.figure(2)
##plt.ylim(-10E-5,10E-5)
plt.plot(time, gam, time, gam_dot)

plt.figure(3)
plt.plot(tau,gam,tau,gam_dot)