from brian2 import *

# Izhikevich
Izhikevich_eqs = '''
dv/dt = (0.04*v**2 + 5*v + 140 - u + I)/ms : 1
du/dt = a*(b*v - u)/ms : 1
'''

Izhikevich_threshold = 'v > v_th'
Izhikevich_reset = '''
v = c
u = u + d
'''

# MQIF
MQIF_eqs = '''
dv/dt = (g_f*(v-v_f0)**2 - g_s*(v_s-v_s0)**2 - g_u*(v_u-v_u0)**2 + I)/C : 1
dv_s/dt = (v - v_s)/tau_s : 1
dv_u/dt = (v - v_u)/tau_u : 1
'''

MQIF_threshold = 'v > v_th'
MQIF_reset = '''
v = v_f0
v_s = v_sr
v_u = v_u + dv_u
'''

# MQIF with ultra-ultraslow timescale
MQIF2_eqs = '''
dv/dt = (g_f*(v-v_f0)**2 - g_s*(v_s-v_s0)**2 - g_u*(v_u-v_u0)**2 - g_uu*(v_uu-v_uu0)**2 + I)/C : 1
dv_s/dt = (v - v_s)/tau_s : 1
dv_u/dt = (v - v_u)/tau_u : 1
dv_uu/dt = (v - v_uu)/tau_uu : 1
'''

MQIF2_threshold = 'v > v_th'
MQIF2_reset = '''
v = v_f0
v_s = v_sr
v_u = v_u + dv_u
v_uu = v_uu + dv_uu
'''
