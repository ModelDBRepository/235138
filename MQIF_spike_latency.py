import matplotlib.pyplot as plt
from brian2 import *
from brian_models import *

start_scope()

C = 1*ms
tau_s = 10*ms
tau_u = 100*ms
v_th = 30
v_f0 = -40
v_s0 = -35
v_u0 = -40
g_f = 1
g_s = 0.5
g_u = 0

v_sr = 0
dv_u = 0

t_step = 100
MQIF_eqs = MQIF_eqs + '''I = 30.0 + 20.0*sign(t/ms-t_step) : 1'''

G = NeuronGroup(1, MQIF_eqs, threshold = MQIF_threshold, reset = MQIF_reset, dt=0.05*ms, method='rk4')
G.v = -50
G.v_s = -50
G.v_u = -50
M = StateMonitor(G, ['v','I'], record=0)

spikemon = SpikeMonitor(G)

run(200*ms)

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
