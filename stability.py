import numpy as np
import matplotlib.pyplot as plt

def stability_plot():
    S = 50
    Sh = 10
    X_cg = np.linspace(0,20,10)
    X_ac = 0.25
    C_l_alpha_h = 1
    C_l_alpha_A = 1.2
    downwash = 0.03
    l_h = 20
    c = 4
    V_h = 100
    V = 110
    SM = 0.05
    S_h_S = np.zeros(len(X_cg))
    i = 0
    for x_cg in X_cg:
        S_h_S[i] = 1/((C_l_alpha_h/C_l_alpha_A)*(1-downwash)*(l_h/c)*(V_h/V)**2)*x_cg - (X_ac-SM)/((C_l_alpha_h/C_l_alpha_A)*(1-downwash)*(l_h/c)*(V_h/V)**2)
        i =i+1
    plt.plot(X_cg/c,S_h_S)
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.grid(True)
    plt.xlabel('X_cg/MAC')
    plt.ylabel('S_h/S')
    plt.show()

stability_plot()