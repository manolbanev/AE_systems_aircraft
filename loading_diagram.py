import numpy as np
import matplotlib.pyplot as plt

# OEW data
OEW = 13450 # [kg]
x_cg_OEW = 0.224 # [MAC]

# Seat data
n_window_seats = 2
n_aisle_seats = 2
n_rows = 18
passenger_mass = 85 # [kg]

seat_pitch_in = 29 # [in]
seat_pitch = seat_pitch_in * 0.0254 / 2.303 # [MAC]

x_first_row = -2.23361 # [MAC]
x_last_row = x_first_row + (n_rows-1) * seat_pitch # [MAC]

# Cargo data
x_cg_front_cargo = -3 # [MAC]
x_cg_rear_cargo = 4.323 # [MAC]
m_front_cargo = 715 # [kg]
m_rear_cargo = 715 # [kg]

# fuel data
x_cg_fuel = 0.4186 # [MAC]
m_fuel = 1800 # [kg]


# Initialize mass and CG lists
x_front_list = []
x_rear_list = []
mass_front_list = []
mass_rear_list = []
mass_front_list.append(OEW)
mass_rear_list.append(OEW)
x_front_list.append(x_cg_OEW)
x_rear_list.append(x_cg_OEW)


# Cargo loading 
x_front_list.append( (x_front_list[-1]*mass_front_list[-1]  + x_cg_front_cargo*m_front_cargo ) / (mass_front_list[-1] + m_front_cargo) )
mass_front_list.append(mass_front_list[-1] + m_front_cargo)
x_rear_list.append( (x_rear_list[-1]*mass_rear_list[-1]  + x_cg_rear_cargo*m_rear_cargo ) / (mass_rear_list[-1] + m_rear_cargo) )
mass_rear_list.append(mass_rear_list[-1] + m_rear_cargo)

# Cargo loading part 2
x_front_list.append( (x_front_list[-1]*mass_front_list[-1]  + x_cg_rear_cargo*m_rear_cargo ) / (mass_front_list[-1] + m_rear_cargo) )
mass_front_list.append(mass_front_list[-1] + m_rear_cargo)
x_rear_list.append( (x_rear_list[-1]*mass_rear_list[-1]  + x_cg_front_cargo*m_front_cargo ) / (mass_rear_list[-1] + m_front_cargo) )
mass_rear_list.append(mass_rear_list[-1] + m_front_cargo)


# Front loading window seats
for i in range(n_rows):
    x_front_list.append( (x_front_list[-1]*mass_front_list[-1]  + (x_first_row + i*seat_pitch)*n_window_seats*passenger_mass ) / (mass_front_list[-1] + n_window_seats*passenger_mass) )
    mass_front_list.append(mass_front_list[-1] + n_window_seats*passenger_mass)

# Rear loading window seats
for i in range(n_rows):
    x_rear_list.append( (x_rear_list[-1]*mass_rear_list[-1]  + (x_last_row - i*seat_pitch)*n_window_seats*passenger_mass ) / (mass_rear_list[-1] + n_window_seats*passenger_mass) )
    mass_rear_list.append(mass_rear_list[-1] + n_window_seats*passenger_mass)

# Front loading aisle seats
for i in range(n_rows):
    x_front_list.append( (x_front_list[-1]*mass_front_list[-1]  + (x_first_row + i*seat_pitch)*n_aisle_seats*passenger_mass ) / (mass_front_list[-1] + n_aisle_seats*passenger_mass) )
    mass_front_list.append(mass_front_list[-1] + n_aisle_seats*passenger_mass)

# Rear loading aisle seats
for i in range(n_rows):
    x_rear_list.append( (x_rear_list[-1]*mass_rear_list[-1]  + (x_last_row - i*seat_pitch)*n_aisle_seats*passenger_mass ) / (mass_rear_list[-1] + n_aisle_seats*passenger_mass) )
    mass_rear_list.append(mass_rear_list[-1] + n_aisle_seats*passenger_mass)

# Fuel loading
x_fuel_list = []
x_fuel_list.append(x_front_list[-1])
mass_fuel_list = []
mass_fuel_list.append(mass_front_list[-1])
x_fuel_list.append(( x_fuel_list[-1]*mass_fuel_list[-1] + x_cg_fuel*m_fuel) / (mass_fuel_list[-1] + m_fuel))
mass_fuel_list.append(mass_fuel_list[-1] + m_fuel)



#redo for new input parameters
# OEW data2
OEW2 = 14106.76 # [kg]
x_cg_OEW2 = 0.3689 # [MAC]

# Seat data2
n_window_seats2 = 2
n_aisle_seats2 = 2
n_rows2 = 14
passenger_mass2 = 85 # [kg]

seat_pitch_in2 = 29 # [in]
seat_pitch2 = seat_pitch_in2 * 0.0254 / 2.303 # [MAC]

x_first_row2 = -2.23361 # [MAC]
x_last_row2 = x_first_row2 + (n_rows2-1) * seat_pitch # [MAC]

# Cargo data2
x_cg_front_cargo2 = -3 # [MAC]
x_cg_rear_cargo2 = 4.323 # [MAC]
m_front_cargo2 = 1395 # [kg]
m_rear_cargo2 = 1395 # [kg]
# m_front_cargo2 = 556.108 # [kg]
# m_rear_cargo2 = 556.108 # [kg]

# fuel data2
x_cg_fuel2 = 0.4186 # [MAC]
m_fuel2 = 1143.24 # [kg]
# m_fuel2 = 2821.024 # [kg]

# Initialize mass and CG lists2
x_front_list2 = []
x_rear_list2 = []
mass_front_list2 = []
mass_rear_list2 = []
mass_front_list2.append(OEW2)
mass_rear_list2.append(OEW2)
x_front_list2.append(x_cg_OEW2)
x_rear_list2.append(x_cg_OEW2)

#cargo loading2
x_front_list2.append( (x_front_list2[-1]*mass_front_list2[-1]  + x_cg_front_cargo2*m_front_cargo2 ) / (mass_front_list2[-1] + m_front_cargo2) )
mass_front_list2.append(mass_front_list2[-1] + m_front_cargo2)
x_rear_list2.append( (x_rear_list2[-1]*mass_rear_list2[-1]  + x_cg_rear_cargo2*m_rear_cargo2 ) / (mass_rear_list2[-1] + m_rear_cargo2) )
mass_rear_list2.append(mass_rear_list2[-1] + m_rear_cargo2)

# Cargo loading2 part 2
x_front_list2.append( (x_front_list2[-1]*mass_front_list2[-1]  + x_cg_rear_cargo2*m_rear_cargo2 ) / (mass_front_list2[-1] + m_rear_cargo2) )
mass_front_list2.append(mass_front_list2[-1] + m_rear_cargo2)
x_rear_list2.append( (x_rear_list2[-1]*mass_rear_list2[-1]  + x_cg_front_cargo2*m_front_cargo2 ) / (mass_rear_list2[-1] + m_front_cargo2) )
mass_rear_list2.append(mass_rear_list2[-1] + m_front_cargo2)


# Front loading window seats2
for i in range(n_rows2):
    x_front_list2.append( (x_front_list2[-1]*mass_front_list2[-1]  + (x_first_row2 + i*seat_pitch2)*n_window_seats2*passenger_mass2 ) / (mass_front_list2[-1] + n_window_seats2*passenger_mass2) )
    mass_front_list2.append(mass_front_list2[-1] + n_window_seats2*passenger_mass2)

# Rear loading window seats2
for i in range(n_rows2):
    x_rear_list2.append( (x_rear_list2[-1]*mass_rear_list2[-1]  + (x_last_row2 - i*seat_pitch2)*n_window_seats2*passenger_mass2 ) / (mass_rear_list2[-1] + n_window_seats2*passenger_mass2) )
    mass_rear_list2.append(mass_rear_list2[-1] + n_window_seats2*passenger_mass2)

# Front loading aisle seats2
for i in range(n_rows2):
    x_front_list2.append( (x_front_list2[-1]*mass_front_list2[-1]  + (x_first_row2 + i*seat_pitch2)*n_aisle_seats2*passenger_mass2 ) / (mass_front_list2[-1] + n_aisle_seats2*passenger_mass2) )
    mass_front_list2.append(mass_front_list2[-1] + n_aisle_seats2*passenger_mass2)

# Rear loading aisle seats2
for i in range(n_rows2):
    x_rear_list2.append( (x_rear_list2[-1]*mass_rear_list2[-1]  + (x_last_row2 - i*seat_pitch2)*n_aisle_seats2*passenger_mass2 ) / (mass_rear_list2[-1] + n_aisle_seats2*passenger_mass2) )
    mass_rear_list2.append(mass_rear_list2[-1] + n_aisle_seats2*passenger_mass2)

# Fuel loading
x_fuel_list2 = []
x_fuel_list2.append(x_front_list2[-1])
mass_fuel_list2 = []
mass_fuel_list2.append(mass_front_list2[-1])
x_fuel_list2.append(( x_fuel_list2[-1]*mass_fuel_list2[-1] + x_cg_fuel2*m_fuel2) / (mass_fuel_list2[-1] + m_fuel2))
mass_fuel_list2.append(mass_fuel_list2[-1] + m_fuel2)







# Plotting
x_lower_bound = min(x_front_list)
x_upper_bound = max(x_rear_list)

x_lower_bound2 = min(x_front_list2)
x_upper_bound2 = max(x_rear_list2)

print(x_lower_bound - (np.abs(x_upper_bound)+np.abs(x_lower_bound))*0.02)
print(x_upper_bound + (np.abs(x_upper_bound)+np.abs(x_lower_bound))*0.02)
print('--------------------')
print(x_lower_bound2 - (np.abs(x_upper_bound2)+np.abs(x_lower_bound2))*0.02)
print(x_upper_bound2 + (np.abs(x_upper_bound2)+np.abs(x_lower_bound2))*0.02)

# plot first loading diagram
plt.plot(x_front_list, mass_front_list, 'r',  alpha=0.3)
plt.plot(x_rear_list, mass_rear_list, 'b',  alpha=0.3)
plt.plot(x_fuel_list, mass_fuel_list, 'g',  alpha=0.3)

#plt.axvline(x=x_lower_bound, color='k', linestyle='--')
#plt.axvline(x=x_upper_bound, color='k', linestyle='--')
plt.axvline(x=x_lower_bound - (np.abs(x_upper_bound)+np.abs(x_lower_bound))*0.02, color='k', linestyle='-', alpha=0.5)
plt.axvline(x=x_upper_bound + (np.abs(x_upper_bound)+np.abs(x_lower_bound))*0.02, color='k', linestyle='-',  alpha=0.5)

#plot second loading diagram
plt.plot(x_front_list2, mass_front_list2, 'ro--', label='Front Loading')
plt.plot(x_rear_list2, mass_rear_list2, 'bo--', label='Rear loading')
plt.plot(x_fuel_list2, mass_fuel_list2, 'go--', label='Fuel Loading')
plt.axvline(x=x_lower_bound2, color='k', linestyle='--')
plt.axvline(x=x_upper_bound2, color='k', linestyle='--')
plt.axvline(x=x_lower_bound2 - (np.abs(x_upper_bound2)+np.abs(x_lower_bound2))*0.02, color='k', linestyle='-', label='Lower Bound')
plt.axvline(x=x_upper_bound2 + (np.abs(x_upper_bound2)+np.abs(x_lower_bound2))*0.02, color='k', linestyle='-', label='Upper Bound')

plt.title('Loading Diagram With Modifications')
plt.xlabel('C.G. Position w.r.t. LEMAC [MAC]')
plt.ylabel('Mass [kg]')
plt.legend()
plt.grid()
#plt.savefig('loading_diagram_modified_MTOW.png', dpi=500, bbox_inches='tight')
plt.show()