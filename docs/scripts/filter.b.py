''' 
This script demonstrates using rbf.filter.filter to denoise and 
differentiate a time series
'''
import numpy as np
import matplotlib.pyplot as plt
from rbf.filter import filter
np.random.seed(1)

t = np.linspace(0.0,5.0,200)
u_true,udiff_true = np.sin(t),np.cos(t) # true signal
sigma_obs = 0.5*np.ones(t.shape)
u_obs = u_true + np.random.normal(0.0,sigma_obs) # observed
# find the filtered solution
u_pred,sigma_pred = filter(t[:,None],u_obs,sigma_obs,
                           samples=1000,n=3,
                           cutoff=0.5)
# find the derivative of the filtered solution
udiff_pred,sigmadiff_pred = filter(t[:,None],u_obs,sigma_obs,
                                   samples=1000,n=3,
                                   cutoff=0.5,diffs=(1,))

# plot the results
fig,ax = plt.subplots(2,1)
ax[0].plot(t,u_obs,'k.',label='observed',zorder=0)
ax[0].plot(t,u_true,'r-',label='true signal',zorder=2)
ax[0].plot(t,u_pred,'b-',label='filtered',zorder=1)
ax[0].fill_between(t,u_pred-sigma_pred,u_pred+sigma_pred,
                   color='b',alpha=0.4,edgecolor='none',zorder=1)
ax[0].legend(frameon=False)                   
ax[1].plot(t,udiff_true,'r-',label='true signal derivative',zorder=2)
ax[1].plot(t,udiff_pred,'b-',label='filtered derivative',zorder=1)
ax[1].fill_between(t,udiff_pred-sigmadiff_pred,
                   udiff_pred+sigmadiff_pred,
                   color='b',alpha=0.4,edgecolor='none',zorder=1)
ax[1].legend(frameon=False)                   
plt.tight_layout()
plt.savefig('../figures/filter.b.png')
plt.show()

