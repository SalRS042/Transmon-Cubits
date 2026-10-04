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

maxEc1 = 35

Ej11 = 15
Ej21 = 25
Ng11 = 1/2
Ng21 = 1/2
s11 = 0
s21 = 0

Ej12 = 15
Ej22 = 25
Ng12 = 1/2
Ng22 = 1/2
s12 = 0
s22 = 1

Ej13 = 15
Ej23 = 25
Ng13 = 1/2
Ng23 = 1/2
s13 = 1
s23 = 0

Ej14 = 15
Ej24 = 25
Ng14 = 1/2
Ng24 = 1/2
s14 = 1
s24 = 1

Ec_min_acuerdo = 2

EC1 = np.linspace(Ec_min_acuerdo, maxEc1, 500)

def Energia(ng1,ng2,EC1,Ej1,Ej2,s1,s2):
    
    Autovalor = []

    cont = 0
    while cont < len(EC1):
    
        from scipy.integrate import quad
        from scipy.special import erf
        import cmath    
        import numpy as np

        Ec1 = EC1[cont]
        
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
        
        Ng1 = ng1*np.sqrt(abs(C1/A1))
        Ng2 = ng2*np.sqrt(abs(C2/A2))
    
        def Energia(A,s,N,Ej):
            if s == 0:
                return ( 1/2 - 1/(8*np.sqrt( A/(8*Ej) )) )*np.sqrt( 8*A*Ej )
            else:
                return A*(s - N)**2 - Ej**2/( 4*(A*(s-N+1)**2 - Ej**2/( 4*(A*(s-N+2)**2 - Ej**2/( 4*(A*(s-N+3)**2 - Ej**2/( 4*(A*(s-N+3)**2) )))))))
        
        E = Energia(A1,s1,Ng1,Ej1) + Energia(A2,s2,Ng2,Ej2)
        Autovalor.append( E )
        cont = cont + 1
    autovalor = []
    for i in arange(0,len(Autovalor)):
        if ( abs(Autovalor[i]) > 25):
            autovalor.append(0)
        else:
            autovalor.append(Autovalor[i])
    print(Ei,Ec2)
    return autovalor

plt.plot(EC1, Energia(Ng11,Ng21,EC1,Ej11,Ej21,s11,s21),label=r'$\mathrm{\lambda_{s_1 = 0, s_2 = 0 }}$ - Analytic')
plt.plot(EC1, Energia(Ng12,Ng22,EC1,Ej12,Ej22,s12,s22),label=r'$\mathrm{\lambda_{s_1 = 0, s_2 = 1 }}$ - Analytic')
plt.plot(EC1, Energia(Ng13,Ng23,EC1,Ej13,Ej23,s13,s23),label=r'$\mathrm{\lambda_{s_1 = 1, s_2 = 0 }}$ - Analytic')
plt.plot(EC1, Energia(Ng14,Ng24,EC1,Ej14,Ej24,s14,s24),label=r'$\mathrm{\lambda_{s_1 = 1, s_2 = 1 }}$ - Analytic')
plt.xlabel(r'$\mathrm{E_{C_1}}$', fontsize=14)
plt.ylabel(r'$\mathrm{\lambda_{s_1,s_2}}$', fontsize=14)
plt.grid(True)
plt.ylim(-25,25)
plt.legend(loc="lower right")
plt.savefig('secreto')
plt.show()
