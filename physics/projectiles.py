import numpy as np
import matplotlib.pyplot as plt

# PROJECTILE MOTION SIM
speed = 50
angle = 45  # degrees
g = 9.81
angle_rad = np.deg2rad(angle)
speed_x = speed * np.cos(angle_rad)
speed_y = speed * np.sin(angle_rad)


time = np.linspace(0, 10, 100)


x = speed_x * time
y = speed_y * time - 0.5 * g * time**2  # s = ut + 1/2 at^2
mask = y > 0


fig, ax = plt.subplots()
ax.plot(x[mask], y[mask])

ax.set_ylim(0, max(y) + 10)


plt.show()
