import numpy as np
import matplotlib.pyplot as plt

def stability_plot(X_cg,X_ac,C_l_alpha_h,C_l_alpha_A,l_h,c,V_h,V,S_h_S,downwash,SM):
    i = 0
    for x_cg in X_cg:
        S_h_S[i] = 1/((C_l_alpha_h/C_l_alpha_A)*(1-downwash)*(l_h/c)*(V_h/V)**2)*x_cg - (X_ac-SM)/((C_l_alpha_h/C_l_alpha_A)*(1-downwash)*(l_h/c)*(V_h/V)**2)
        i =i+1
    plt.plot(X_cg/c,S_h_S,label = 'Stability')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.grid(True)
    plt.xlabel('X_cg/MAC')
    plt.ylabel('S_h/S')
    plt.legend()


