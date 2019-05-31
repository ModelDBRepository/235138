import matplotlib.pyplot as plt
import numpy as np
from brian2 import *
from brian_models import *

start_scope()

# False: Figure 6B
# True: Figure 6C
latency = True

v_th = 30
a = 0.02
b = 0.
if latency:
    c = -62
    d = 0.
else:
    c = -65
    d = 6

t_step = 1000
Izhikevich_eqs = Izhikevich_eqs + '''I = 16. + .255*sign(t/ms-t_step) : 1'''

G = NeuronGroup(1, Izhikevich_eqs, threshold = Izhikevich_threshold, reset = Izhikevich_reset, dt=0.5*ms, method='rk4')
M = StateMonitor(G, ['v','I'], record=0)

spikemon = SpikeMonitor(G)

run(2000*ms)

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
