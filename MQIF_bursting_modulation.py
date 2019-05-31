import matplotlib.pyplot as plt
from brian2 import *
from brian_models import *

start_scope()

time = 1000*ms

case = 1

C = 1*ms
tau_s = 10*ms
tau_u = 100*ms
v_th = -30
v_f0 = -40
I = 5.

if case == 1:
    v_s0 = -41
    v_u0 = -50
elif case == 2:
    v_s0 = -39
    v_u0 = -50
elif case == 3:
    v_s0 = -38.5
    v_u0 = -50
elif case == 4:
    v_s0 = -39
    v_u0 = -54.5
elif case == 5:
    v_s0 = -38.5
    v_u0 = -54.5

g_f = 1
g_s = 0.5
g_u = 0.015

v_sr = -35
dv_u = 3


G = NeuronGroup(1, MQIF_eqs, threshold = MQIF_threshold, reset = MQIF_reset, dt=0.05*ms, method='rk4')
G.v = -35
G.v_s = -35
G.v_u = -35
M = StateMonitor(G, ['v','v_s','v_u'], record=0)

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
