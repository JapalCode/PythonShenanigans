import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()

k = 8.99e9
e = 1.6e-19


class Charge:
    def __init__(self, position, charge):
        self.position = position
        self.charge = charge


charges = []

# take user inputs
user_finished = False
while not user_finished:
    posx = float(input("Please enter the x position of your charge: "))
    posy = float(input("Please enter the y position of your charge: "))
    chargeMag = int(input("Please enter the charge of your charge in units of e: "))
    charge = Charge([posx, posy], chargeMag * e)
    charges.append(charge)

    decision = input("Would you like to keep adding charges (y/n): ")
    if decision == "n":
        user_finished = True


def CalculateFieldStrength(position):
    E = 0
    for charge in charges:
        distance1 = position[0] - charge.position[0]  # take r12
        distance2 = position[1] - charge.position[1]
        distance = np.asarray([distance1, distance2])
        distanceMagnitude = np.sqrt(distance[0] ** 2 + distance[1] ** 2)
        distanceDirection = distance / distanceMagnitude
        fieldStrength = k * charge.charge * distanceDirection / distanceMagnitude
        E += fieldStrength
    return E


x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)
E = CalculateFieldStrength([X, Y])

ax.set_title("Electric Field Demonstration")

for charge in charges:
    if charge.charge > 0:
        ax.plot(charge.position[0], charge.position[1], "ro")
    else:
        ax.plot(charge.position[0], charge.position[1], "bo")


ax.quiver(X, Y, E[0], E[1])
plt.show()
