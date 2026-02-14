import numpy as np
import matplotlib.pyplot as plt

speed = 10
angle_1 = 30
angle_2 = 45
angle_3 = 60
g = 9.81

angle_1_rad = np.deg2rad(angle_1)
angle_2_rad = np.deg2rad(angle_2)
angle_3_rad = np.deg2rad(angle_3)

T_1 = 2 * speed * np.sin(angle_1_rad) / g
T_2 = 2 * speed * np.sin(angle_2_rad) / g
T_3 = 2 * speed * np.sin(angle_3_rad) / g

time_1 = np.linspace(0, T_1, 100)
time_2 = np.linspace(0, T_2, 100)
time_3 = np.linspace(0, T_3, 100)

x_1 = speed * np.cos(angle_1_rad) * time_1
x_2 = speed * np.cos(angle_2_rad) * time_2
x_3 = speed * np.cos(angle_3_rad) * time_3

y_1 = speed * np.sin(angle_1_rad) * time_1 - 0.5 * g * time_1**2
y_2 = speed * np.sin(angle_2_rad) * time_2 - 0.5 * g * time_2**2
y_3 = speed * np.sin(angle_3_rad) * time_3 - 0.5 * g * time_3**2

fig, ax = plt.subplots()

ax.plot(x_1, y_1, "r--")
ax.plot(x_2, y_2, "g--")
ax.plot(x_3, y_3, "b--")

ax.grid()

ax.set_ylim(0, max(y_3) + 0.1 * max(y_3))
ax.set_xlim(0, max(x_2) + 0.1 * max(x_2))
ax.set_title("Projectiles simulation")
ax.set_xlabel("Distance /m")
ax.set_ylabel("Height /m")

plt.show()
