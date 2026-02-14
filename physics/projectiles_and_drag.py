import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

speed = 10
angle_1 = 30
angle_2 = 45
angle_3 = 60
g = 9.81

rho = 1000
C_d = 0.5
A = 1
m = 50
# F_d = C_d * rho * A * v^2


def calculateTrajectory(speed, angle):
    angle_rad = np.deg2rad(angle)
    T = 2 * speed * np.sin(angle_rad) / g
    t = np.linspace(0, T, 100)
    x = speed * np.cos(angle_rad) * t
    y = speed * np.sin(angle_rad) * t - 0.5 * g * t**2
    return x, y


def calculateDragTrajectory(speed, angle):
    angle_rad = np.angle_rad = np.deg2rad(angle)
    T = 2 * speed * np.sin(angle_rad) / g
    t = np.linspace(0.1, T, 100)
    print(m * np.log(t) / (C_d * rho * A))
    x = speed * np.cos(angle_rad) * t - m * np.log(t) / (C_d * rho * A)
    y = speed * np.sin(angle_rad) * t - 0.5 * g * t**2
    mask = x > 0
    return x[mask], y[mask]


x1, y1 = calculateTrajectory(speed, angle_1)
x2, y2 = calculateTrajectory(speed, angle_2)
x3, y3 = calculateTrajectory(speed, angle_3)

ax.plot(x1, y1, color="green")
ax.plot(x2, y2, color="blue")
ax.plot(x3, y3, color="red")

x1D, y1D = calculateDragTrajectory(speed, angle_1)
x2D, y2D = calculateDragTrajectory(speed, angle_2)
x3D, y3D = calculateDragTrajectory(speed, angle_3)


ax.plot(x1D, y1D, "g--")
ax.plot(x2D, y2D, "b--")
ax.plot(x3D, y3D, "r--")

ax.set_xlim(0, max(x2))
ax.set_ylim(0, max(y3))
ax.grid()

plt.show()
