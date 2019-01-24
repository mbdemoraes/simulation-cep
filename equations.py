import matplotlib.pyplot as plt
import numpy as np
import math


#plt.plot([1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000], [199, 399, 599, 799, 1000, 1200, 1400, 1600, 1800, 2000], marker="^", color='#000000')


ts = 800
delta = 1
M = 600
R = 60

Tapp = ts

# --------- Equation 2 -----------

tau = math.sqrt(2*delta*M) * 1+((1/3) * math.sqrt(delta/2*M) + 1/9 * (delta/2*M))
tau = round(tau)

print("Equation for Optimal Checkpoint Interval, Tau = " + str(tau))

# --------- Equation 1 -----------
tw = ts + (ts/tau) * delta

print("Equation for Failure Free, tw = " + str(tw))

# --------- Equation 3 -----------

k = int(Tapp/tau)


Tfail = Tapp + (k-1)*delta + k* ((tau + delta)/2 + R) * ((tau + delta)/M)

print("Equation For Failure, T = " + str(Tfail) + " k=" + str(k))


# --------- Equation Discarded Failure-Prone -----------


arrival = 5000
teste = (Tfail/M) + 1
omega = arrival * (k*delta) + arrival * ((teste) * R)

print("Discards failure = " + str(omega) + "tapp=" + str(teste))

# --------- Equation Discarded Failure-Free -----------

omega = arrival * (k*delta)

print("Discards FREE = " + str(omega))

# --------- Equation Unprocessed -----------

theta = arrival * (teste) * (tau/2)

print("Unprocessed = " + str(tau/2))





