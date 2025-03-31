from controlability import controlability_plot
from stability import stability_plot
import matplotlib.pyplot as plt
import numpy as np

def scissor_plot():
   
    X_cg = np.linspace(-20,20,10)
    C_l_h = -0.5
    C_l_A = 0.5
    l_h = 20
    c = 4
    V_h = 100
    V = 110
    S_h_S = np.zeros(len(X_cg))
    C_m_ac = -0.5
    X_ac = 0.25
    downwash = 0.03
    SM = 0.05
    C_l_alpha_A = 1
    C_l_alpha_h = 1
   
    controlability_plot(X_cg,X_ac,C_l_h,C_l_A,l_h,c,V_h,V,S_h_S,C_m_ac)
    stability_plot(X_cg,X_ac,C_l_alpha_h,C_l_alpha_A,l_h,c,V_h,V,S_h_S,downwash,SM)
    plt.show()

scissor_plot()