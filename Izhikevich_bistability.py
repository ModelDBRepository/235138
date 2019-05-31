import matplotlib.pyplot as plt
import numpy as np
from brian2 import *
from brian_models import *

start_scope()

# True: Figure 5B
# False: Figure 5C
hopf = True

v_th = 30

if hopf:
    a = 0.1
    b = 0.26
    c = -60
    d = 0
else:
    a = 1
    b = 0.2
    c = -60
    d = -25


if hopf:
    ta = TimedArray([0,1,1,0], dt=1*ms)
    ta2 = TimedArray([0,1,1,1,1,0], dt=1*ms)
    Izhikevich_eqs = Izhikevich_eqs + '''
    I = 0.24 + ta(t-100*ms) - ta(t-220*ms)
    + ta(t-300*ms) - ta(t-400*ms) - ta(t-457*ms)
    + ta2(t-600*ms) - ta2(t-720*ms) - ta(t-756*ms)
    + 2*ta(t-900*ms) - 2*ta(t-1020*ms): 1'''
else:
    # Time has been scaled by 2 to make spikes visible
    ta = TimedArray([0,23,23,0], dt=.5*ms)
    ta2 = TimedArray([0,23,23,23,23,0], dt=.5*ms)
    Izhikevich_eqs = Izhikevich_eqs + '''
    I = 0.0 + ta(t-100./4.*ms) - ta(t-220./4.*ms)
    + ta(t-300./4.*ms) - ta(t-400./4.*ms)
    + ta2(t-600./4.*ms) - ta2(t-720./4.*ms)
    + 2*ta(t-900./4.*ms) - 2*ta(t-1020./4.*ms): 1'''

G = NeuronGroup(1, Izhikevich_eqs, threshold = Izhikevich_threshold, reset = Izhikevich_reset, dt=0.1*ms, method='rk4')
M = StateMonitor(G, ['v','I'], record=0)

spikemon = SpikeMonitor(G)

if hopf:
    G.v = -61.0
    G.u = -61.0*0.26
    run(1100*ms)
else:
    G.v = -70.0
    G.u = -70.0*0.2
    # Time has been scaled by 2 to make spikes visible
    run(275*ms)

t = M.t/ms
V = M[0].v
V = (V-min(V))/(max(V)-min(V))*100.
I = M[0].I
I = 105.+(I-min(I))/(max(I)-min(I))*20.

# Draw spikes
for ti in spikemon.t:
    i = int(ti / G.dt)
    V[i] = 100.

# Plot
plt.figure()
plt.plot(t, V, t, I)
plt.show()
