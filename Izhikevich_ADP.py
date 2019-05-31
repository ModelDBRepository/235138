import matplotlib.pyplot as plt
import numpy as np
from brian2 import *
from brian_models import *

start_scope()

# False: Figure 7B
# True: Figure 7C
adp = True

v_th = 30


if adp:
    a = 1
    b = 0.2
    c = -60
    d = -15

    ta = TimedArray([0,1,1,0], dt=5*ms)
    ta2 = TimedArray([0,1,1,1,1,0], dt=5*ms)
    Izhikevich_eqs = Izhikevich_eqs + '''
    I = 0. + 5.*(ta(t-200./4*ms)
    + ta2(t-400./4*ms)
    + 1.5*ta(t-600./4*ms)
    + 1.5*ta2(t-800./4*ms)): 1'''
else:
    a = 0.5
    b = 0.6
    c = -65
    d = 6

    ta = TimedArray([0,1,1,0], dt=5*ms)
    ta2 = TimedArray([0,1,1,1,1,0], dt=5*ms)
    Izhikevich_eqs = Izhikevich_eqs + '''
    I = -20. + 5.*(ta(t-200./4*ms)
    + ta2(t-400./4*ms)
    + 1.5*ta(t-600./4*ms)
    + 1.5*ta2(t-800./4*ms)): 1'''

G = NeuronGroup(1, Izhikevich_eqs, threshold = Izhikevich_threshold, reset = Izhikevich_reset, dt=0.1*ms, method='rk4')
M = StateMonitor(G, ['v','I'], record=0)

spikemon = SpikeMonitor(G)

G.v = -70.0
G.u = -70.0*0.2

run(250*ms)

t = M.t/ms
V = M[0].v
V = (V-min(V))/(max(V)-min(V))*100.
I = M[0].I
I = 105.+(I-min(I))/(max(I)-min(I))*10.

# Draw spikes
for ti in spikemon.t:
    i = int(ti / G.dt)
    V[i] = 100.

# Plot
plt.figure()
plt.plot(t, V, t, I)
plt.show()
