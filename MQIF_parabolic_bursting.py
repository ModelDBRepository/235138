import matplotlib.pyplot as plt
from brian2 import *
from brian_models import *

start_scope()

time = 2000*ms

C = 1*ms
tau_s = 10*ms
tau_u = 100*ms
tau_uu = 1000*ms
v_th = -0
v_f0 = -40
v_s0 = -40
v_u0 = -20
v_uu0 = -50
g_f = 1
g_s = 0.5
g_u = 0.1
g_uu = 0.01

v_sr = -25
dv_u = 3
dv_uu = 3

I = 110.

G = NeuronGroup(1, MQIF2_eqs, threshold = MQIF2_threshold, reset = MQIF2_reset, dt=0.05*ms, method='rk4')
G.v = -35
G.v_s = -35
G.v_u = -35
G.v_uu = -35
M = StateMonitor(G, ['v','v_s','v_u','v_uu'], record=0)

spikemon = SpikeMonitor(G)

run(time)

t = M.t/ms
V = M[0].v
V = (V-min(V))/(max(V)-min(V))*100.

# Draw spikes
for ti in spikemon.t:
    i = int(ti / G.dt)
    V[i] = 100.

# Plot
plt.figure()
plt.plot(t, V)
plt.show()
