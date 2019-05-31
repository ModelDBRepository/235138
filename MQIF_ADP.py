import matplotlib.pyplot as plt
from brian2 import *
from brian_models import *

start_scope()

C = 1*ms
tau_s = 10*ms
tau_u = 100*ms
v_th = -30
v_f0 = -40
v_s0 = -39
v_u0 = -40
g_f = 1
g_s = 0.5
g_u = 0

v_sr = -35
dv_u = 0

ta = TimedArray([0,1,1,0], dt=10*ms)
ta2 = TimedArray([0,1,1,1,1,0], dt=10*ms)
MQIF_eqs = MQIF_eqs + '''
    I = -1. + 4.5*(ta(t-200./2*ms)
    + ta2(t-400./2*ms)
    + 1.5*ta(t-600./2*ms)
    + 1.5*ta2(t-800./2*ms)): 1'''

G = NeuronGroup(1, MQIF_eqs, threshold = MQIF_threshold, reset = MQIF_reset, dt=0.05*ms, method='rk4')
G.v = -41.5
G.v_s = -41.5
G.v_u = -41.5
M = StateMonitor(G, ['v','I'], record=0)

spikemon = SpikeMonitor(G)

run(500*ms)

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
