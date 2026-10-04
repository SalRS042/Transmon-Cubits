import math as m
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from numpy import *
import numpy as np
from matplotlib import *
import seaborn as sns

Ec = 6
n_min = -3
sep = 7
Ej = 36
ng = 1/2

def Psi_dec(Ej,Ec,n,ng):
    eta = m.sqrt( Ec/(8*Ej) )
    import numpy as np
    from scipy.integrate import quad
    from scipy.special import erf
    import cmath
    N = ( ((8*eta)/(m.pi))**(1/4) )*np.exp(-4*eta*((n-ng)**2))
    return N


Autovalor = []

Estados = arange(n_min,n_min + sep,1)

for i in Estados:
    Autovalor.append(abs(Psi_dec(Ej,Ec,i,ng))**2)
    
print(Autovalor)

total = 0
for i in Autovalor:
    total = total + i
print(total)

x = np.arange(n_min,n_min + sep,1)
y = abs(Psi_dec(Ej,Ec,x,ng))**2

sns.set(style="whitegrid")
plt.bar(x,y)
plt.ylabel(r'$\mathrm{\left|\langle n|0\rangle\right|^2}$', fontsize=14)
plt.xlabel(r'$\mathrm{n}$', fontsize=14)
plt.tight_layout()
plt.show()
