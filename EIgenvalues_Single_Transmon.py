import scipy as s
import scipy
from scipy import *
import math as m
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from numpy import *
import numpy as np
from matplotlib import *
import numpy as np
import seaborn as sns

ec = np.linspace(0, 20, 500)
Ej = 15
#n = 0
ng = 1/2
#Ec = ec

def Energia(n,ng,Ec,Ej):
    def energia(n,ng,Ec,Ej):
        if n == 0:
            return ( 1/2 - 1/(8*np.sqrt( Ec/(8*Ej) )) )*np.sqrt( 8*Ec*Ej )
        else: 
            return 4*Ec*(n-ng)**2 - Ej**2/( 4*(4*Ec*(n-ng+1)**2 - Ej**2/( 4*(4*Ec*(n-ng+2)**2 - Ej**2/( 4*(4*Ec*(n-ng+3)**2 - Ej**2/( 4*(4*Ec*(n-ng+3)**2) )))))))
    Autovalor = []
    cont = 0
    while cont < len(ec):
        Ec = ec[cont]
        E = energia(n,ng,Ec,Ej)
        Autovalor.append( E )
        cont = cont+1
    autovalor = []
    for i in arange(0,len(Autovalor)):
        if ( abs(Autovalor[i]) > 25):
            #autovalor.append((Autovalor[i-3] + Autovalor[i-2] + Autovalor[i-1] + Autovalor[i+1] + Autovalor[i+2] + Autovalor[i+3])/6)
            autovalor.append(0)
        else:
            autovalor.append(Autovalor[i])
    return autovalor
        

n = 0
E_0 = []

B = np.array([[0,1,0,0],
               [1,0,1,0],
               [0,1,0,1],
               [0,0,1,0]])

A = np.array([[(n-ng)**2,0,0,0],
              [0,(n+1-ng)**2,0,0,],
              [0,0,(n+2-ng)**2,0,],
              [0,0,0,(n+3-ng)**2]])


for i in ec:
    H = 4*i*A - (Ej/2)*B
    autovalores = np.linalg.eigvals(H)
    E_0.append(autovalores[0])
    
n = 1
E_1 = []

B = np.array([[0,1,0,0],
               [1,0,1,0],
               [0,1,0,1],
               [0,0,1,0]])

A = np.array([[(n-ng)**2,0,0,0],
              [0,(n+1-ng)**2,0,0,],
              [0,0,(n+2-ng)**2,0,],
              [0,0,0,(n+3-ng)**2]])

for i in ec:
    H = 4*i*A - (Ej/2)*B
    autovalores = np.linalg.eigvals(H)
    E_1.append(autovalores[0])
    
x = ec
y1 = Energia(0,ng,x,Ej)
y2 = E_0
y3 = Energia(1,ng,x,Ej)
y4 = E_1

sns.set(style="whitegrid")

# Plotting
sns.lineplot(x=x, y=y1,label=r'$\mathrm{\lambda_{n = \left[0\right]}}$ Analyticall - Taylor')
sns.lineplot(x=x, y=y2,label=r'$\mathrm{\lambda_{n = \left[0\right]}}$ Numericall')
sns.lineplot(x=x, y=y3,label=r'$\mathrm{\lambda_{n = \left[1\right]}}$ Analyticall - Cont. Frac.')
sns.lineplot(x=x, y=y4,label=r'$\mathrm{\lambda_{n = \left[1\right]}}$ Numericall')
plt.xlabel(r'$\mathrm{E_C}$', fontsize=14)
plt.ylabel(r'$\mathrm{\lambda_{n = \left[0,1\right]}}$', fontsize=14)
plt.ylim(-15,20)
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig('5')
plt.show()
