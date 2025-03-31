import numpy as np
import matplotlib.pyplot as plt


def controlability_plot(X_cg,X_ac,C_l_h,C_l_A,l_h,c,V_h,V,S_h_S,C_m_ac):
    i = 0
    for x_cg in X_cg:
        S_h_S[i] = 1/((C_l_h/C_l_A)*(l_h/c)*(V_h/V)*2)*x_cg + (C_m_ac/C_l_A - X_ac)/((C_l_h/C_l_A)*(l_h/c)*(V_h/V)*2)
        i = i+1
    plt.plot(X_cg/c,S_h_S, label='Controlability')
    plt.ylim(bottom=0)
    plt.grid(True)
    plt.xlabel('X_cg/MAC')
    plt.ylabel('S_h/S')
    plt.legend()
    
