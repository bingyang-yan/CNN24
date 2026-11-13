from yby import *

key = ['frac_length', 'frac_height', 'frac_width', 'poro_m', 'perm_m', 'poro_f', 'perm_f']
mn = [280*meter, 10*meter, 5*milli*meter, 3*percent, 0.2*milli*darcy, 15*percent, 20*milli*darcy]
mx = [310*meter, 50*meter, 6*milli*meter, 12*percent, 2.4*milli*darcy, 30*percent, 50*milli*darcy]
samples = 130

cla = Y_lhs(key, mn, mx, samples, info='master')
res = cla.lhs()
