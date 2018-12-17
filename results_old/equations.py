import matplotlib.pyplot as plt
import numpy as np
import math


#plt.plot([100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000], [19,39, 59, 79, 99, 119, 139, 159, 179, 199], marker="^", color='#000000')

# --------- Equation 1 -----------
ts =2000
tau = 10
N =  4
cavg = 3
beta = 12
delta = (N * (cavg)) / beta
tw = ts + (ts/tau) * delta

print("Equation for Failure Free, tw = " + str(tw))

Tapp = ts

M = 600
R = 60

# --------- Equation 2 -----------

tau = math.sqrt(2*delta*M) * 1+((1/3) * math.sqrt(delta/2*M) + 1/9 * (delta/2*M))
tau = round(tau)

print("Equation for Optimal Checkpoint Interval, Tau = " + str(tau))

# --------- Equation 3 -----------

k = int(Tapp/tau)
Tapp = k*tau;

Tfail = Tapp + (k-1)*delta + k* ((tau + delta)/2 + R) * ((tau + delta)/M)

print("Equation For Failure, T = " + str(Tfail) + " k=" + str(k))

#TfailNEW = Tapp + (k-1)*delta + k* ((tau + delta)/(k*k) + R) * ((tau + delta)/M)

#print("[NEW] Equation for Failure, T = "  + str(TfailNEW) + " k=" + str(k))




