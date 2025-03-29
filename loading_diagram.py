
import numpy as np
import matplotlib.pyplot as plt

# OEW data
OEW = 5000 # [kg]
x_cg_OEW = 0.5 # [m]

# Seat data
n_window_seats = 2
n_aisle_seats = 2
n_rows = 18
passenger_mass = 85 # [kg]

seat_pitch_in = 29 # [in]
seat_pitch = seat_pitch_in * 0.0254 # [m]
seat_pitch = 1 # [m] # [m]

x_first_row = -10 # [m]
x_last_row = x_first_row + (n_rows-1) * seat_pitch # [m]

# Cargo data
x_cg_front_cargo = -12 # [m]
x_cg_rear_cargo = 10 # [m]
m_front_cargo = 1000 # [kg]
m_rear_cargo = 1000 # [kg]

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


# front loading window seats
for i in range(n_rows):
    x_front_list.append( (x_front_list[-1]*mass_front_list[-1]  + (x_first_row + i*seat_pitch)*n_window_seats*passenger_mass ) / (mass_front_list[-1] + n_window_seats*passenger_mass) )
    mass_front_list.append(mass_front_list[-1] + n_window_seats*passenger_mass)

# rear loading window seats
for i in range(n_rows):
    x_rear_list.append( (x_rear_list[-1]*mass_rear_list[-1]  + (x_last_row - i*seat_pitch)*n_window_seats*passenger_mass ) / (mass_rear_list[-1] + n_window_seats*passenger_mass) )
    mass_rear_list.append(mass_rear_list[-1] + n_window_seats*passenger_mass)

# front loading aisle seats
for i in range(n_rows):
    x_front_list.append( (x_front_list[-1]*mass_front_list[-1]  + (x_first_row + i*seat_pitch)*n_aisle_seats*passenger_mass ) / (mass_front_list[-1] + n_aisle_seats*passenger_mass) )
    mass_front_list.append(mass_front_list[-1] + n_aisle_seats*passenger_mass)

# rear loading aisle seats
for i in range(n_rows):
    x_rear_list.append( (x_rear_list[-1]*mass_rear_list[-1]  + (x_last_row - i*seat_pitch)*n_aisle_seats*passenger_mass ) / (mass_rear_list[-1] + n_aisle_seats*passenger_mass) )
    mass_rear_list.append(mass_rear_list[-1] + n_aisle_seats*passenger_mass)

x_lower_bound = min(x_front_list)
x_upper_bound = max(x_rear_list)

plt.plot(x_front_list, mass_front_list, 'ro-', label='Front Loading')
plt.plot(x_rear_list, mass_rear_list, 'bo-', label='Rear loading')
plt.axvline(x=x_lower_bound, color='k', linestyle='--', label='Lower Bound')
plt.axvline(x=x_upper_bound, color='k', linestyle='--', label='Upper Bound')
plt.axvline(x=x_lower_bound - 0.02*np.abs(x_lower_bound), color='k', linestyle='-', label='Lower Bound - 2%')
plt.axvline(x=x_upper_bound + 0.02*np.abs(x_upper_bound), color='k', linestyle='-', label='Upper Bound + 2%')
plt.title('Loading Diagram')
plt.xlabel('C.G. Position [m]')
plt.ylabel('Mass [kg]')
plt.legend()
plt.grid()
plt.show()
