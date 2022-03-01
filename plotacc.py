
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.optimize import curve_fit

dname=sys.argv[1]

df = pd.read_csv(dname + '.csv')
intt = np.diff(df.loc[:, 't'].values).mean()/1e3

if len(sys.argv)>3:
    t0, t1 = float(sys.argv[2]), float(sys.argv[3])
    fit = True
    mask = (df.loc[:, 't']/1e6 > t0) & (df.loc[:, 't']/1e6 < t1)

df = df[mask]

print('Mean tint: {} ms'.format(intt))
print('Freq:  ', 1/(intt/1000))

df.loc[:, '|a|'] = (df.loc[:, ['ax', 'ay', 'az']]**2).sum(axis=1)**(1/2)
df.loc[:, '|a|'] -= df.loc[:, '|a|'].mean()


fig, axarr = plt.subplots(3, figsize=(6,4), sharex=True)

for ax, acc in zip(axarr, ['ax', 'ay', 'az']):
    ax.plot(df.loc[:, 't']/1e6, df.loc[:, acc], "-x", lw=.5, ms=3)
    ax.set_title(acc)

ax.set_xlabel('Time [s]')
fig.text(0.04, 0.5, 'Acceleration [m/s^2]', va='center', rotation='vertical')



#def damped_harm(t, A, w, damp, phi0, B):
#    return A*np.exp(-damp*t)*np.sin(w*t + phi0) + B

def damped_harm(t, A, w, damp, phi0, B):
    return A*np.exp(-damp*t)*((damp**2 - w**2)*np.sin(w*t + phi0) - damp*w*np.cos(w*t + phi0)) + B

if fit:
    #mask = (df.loc[:, 't']/1e6 > t0) & (df.loc[:, 't']/1e6 < t1)
    t = df.loc[:, 't']/1e6
    a = df.loc[:, 'ax']

    res = curve_fit(damped_harm, t, a, (10, 100, .1, 0, 0))
    p = res[0]
    damp = p[2]
    freq = p[1]/(2*np.pi)

    axarr[0].plot(t, damped_harm(t, *p), label='fit')


print('Damping coeff: {:.4f} 1/s'.format(damp))
print('Frequency:     {:.2f} #/s'.format(freq))

plt.show()





