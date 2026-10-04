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
import sympy as sp
from sympy import *
import numpy as np
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import axes3d

Ec1 = 30
s1_min = -3
s2_min = -3
sep = 7
Ej1 = 26
Ej2 = 10
ng1 = 1/2
ng2 = 1/2

def Psi_cop(Ej1,Ec1,Ej2,s1,s2,ng1,ng2):
    
    a = -((ng2**2)/(ng1**2))
    b = 2*Ec1*(ng2/ng1) + Ec1
    c = - 2*(Ec1**2)*(ng1/ng2) + Ec1**2
    d = -((ng1**2)/(ng2**2))*(Ec1**3)
    roots = np.roots([a, b, c, d])
    
    Ec2 = abs(min(roots))
    Ei = abs((Ec1-Ec2)/3)
    a = np.arctan( ((Ec1 - Ec2)/Ei) + np.sqrt( (((Ec1 - Ec2)/Ei) + 1) ) )
    
    A1 = Ec1*np.cos(a)**2 + Ec2*np.sin(a)**2 - Ei*np.sin(a)*np.cos(a)
    B1 = Ec2*np.sin(a)*(ng2/ng1) - Ec1*np.cos(a)
    C1 = Ec1
    
    A2 = Ec1*np.sin(a)**2 + Ec2*np.cos(a)**2 + Ei*np.sin(a)*np.cos(a)
    B2 = - Ec1*np.sin(a)*(ng1/ng2) - Ec2*np.cos(a)
    C2 = Ec2
    
    eta1 = np.sqrt( abs(B1/(8*Ej1)) )
    eta2 = np.sqrt( abs(B2/(8*Ej2)) )
    nu1 = eta1*np.sqrt(abs(A1/B1))
    nu2 = eta2*np.sqrt(abs(A2/B2))
    Ng1 = ng1*np.sqrt(abs(C1/A1))
    Ng2 = ng2*np.sqrt(abs(C2/A2))
    S1 = s1
    S2 = s2

    E = np.sqrt(16/m.pi)*((nu1*nu2)**(1/4))*np.exp( -4*( nu1*(S1 - Ng1)**2 +nu2*(S2 - Ng2)**2 ) )
    return E

Autovalor = []

estados1 = arange(s1_min, s1_min + sep,1)
estados2 = arange(s2_min, s2_min + sep,1)

cont = 0

while cont < len(estados1):

    if len(estados1) == len(estados2):
        i = estados1[cont]
        j = estados2[cont]
        Autovalor.append(abs(Psi_cop(Ej1,Ec1,Ej2,i,j,ng1,ng2))**1)
        cont = cont + 1
    else:
        print("Se debe verificar que el número de estados debe ser la misma.")
    
print(Autovalor)

total = 0
for i in Autovalor:
    total = total + i
print(total)

x = (estados1)
dx=np.ones(len(estados1))
y = (estados2)
dy=np.ones(len(estados2))
z = np.zeros(len(Autovalor))
dz = Autovalor #abs(Psi_cop(Ej1,Ec1,Ej2,X,Y,ng1,ng2))**1

fig = plt.figure(figsize=(12, 8))
axl = fig.add_subplot(111, projection='3d')
axl.bar3d(x,y,z,dx,dy,dz)
axl.set_xlabel(r'$\mathrm{s_i}$', fontsize=14)
axl.set_ylabel(r'$\mathrm{s_j}$', fontsize=14)
axl.set_zlabel(r'$\mathrm{\left|\langle s_is_j|0_i0_j\rangle\right|}$', fontsize=14)
plt.savefig('3')
plt.show()

#----------PRUEVA----------------

def Psi_dec(Ej,Ec,n,ng):
    eta = m.sqrt( Ec/(8*Ej) )
    N = ( ((8*eta)/(m.pi))**(1/4) )*np.exp(-4*eta*((n-ng)**2))
    return N


Autovalor_pruev = []

a = -((ng2**2)/(ng1**2))
b = 2*Ec1*(ng2/ng1) + Ec1
c = - 2*(Ec1**2)*(ng1/ng2) + Ec1**2
d = -((ng1**2)/(ng2**2))*(Ec1**3)
roots = np.roots([a, b, c, d])
Ec2 = abs(min(roots))

cont = 0
while cont < len(estados1):
    if len(estados1) == len(estados2):
        i = estados1[cont]
        j = estados2[cont]
        Autovalor_pruev.append( abs(Psi_dec(Ej1,Ec1,i,ng1)*Psi_dec(Ej2,Ec2,j,ng2))**1 )
        cont = cont + 1
    else:
        print("Se debe verificar que el número de estados debe ser la misma.")

print(Autovalor_pruev)
x = (estados1)
dx=np.ones(len(estados1))
y = (estados2)
dy=np.ones(len(estados2))
z = np.zeros(len(Autovalor_pruev))
dz = Autovalor_pruev

fig = plt.figure(figsize=(12, 8))
axl = fig.add_subplot(111, projection='3d')
axl.bar3d(x,y,z,dx,dy,dz)
axl.set_xlabel(r'$\mathrm{s_i}$', fontsize=14)
axl.set_ylabel(r'$\mathrm{s_j}$', fontsize=14)
axl.set_zlabel(r'$\mathrm{\left|\langle s_i|0_i\rangle\langle s_j|0_j\rangle\right|}$', fontsize=14)
plt.savefig('4')
plt.show()

print(Ec2,abs((Ec1-Ec2)/3))
