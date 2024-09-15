import numpy as np
import matplotlib.pyplot as plt


# Define the functions for the curves
def B0(t):
    x = -105 * (t**3) + (145 * (t**2)) + 40*t + 10
    y = -135 * (t**3) + (220 * (t**2)) + 5*t + 10
    return x, y


def B1(t):
    x = -135 * (t**3) + (210 * (t**2)) + 15*t + 90
    y = -40 * (t**3) - (20 * (t**2)) + 100*t + 100
    return x, y


def B2(t):
    x = 80 * (t**3) - (140 * (t**2)) + 10*t + 180
    y = 80 * (t**3) - (120 * (t**2)) - 20*t + 140
    return x, y


# Define the control points for each group
control_points = {
    "Group 1": [(10, 10), (50, 15), (75, 60), (90, 100)],
    "Group 2": [(90, 100), (105, 200), (150, 200), (180, 140)],
    "Group 3": [(180, 140), (190, 120), (160, 100), (130, 80)]
}

# Plotting the Bezier curves
t_values = np.linspace(0, 1, 100)

# Initialize plot
plt.figure(figsize=(10, 6))

# Plot B0(t)
x0, y0 = B0(t_values)
plt.plot(x0, y0, label="B0(t)")

# Plot B1(t)
x1, y1 = B1(t_values)
plt.plot(x1, y1, label="B1(t)")

# Plot B2(t)
x2, y2 = B2(t_values)
plt.plot(x2, y2, label="B2(t)")

# Plot control points
for group, points in control_points.items():
    x_points, y_points = zip(*points)
    plt.plot(x_points, y_points, 'o', label=group)

# Restrict the x-axis between 10 and 130
plt.xlim(10, 130)

# Set plot attributes
plt.xlabel('x')
plt.ylabel('y')
plt.title('Connected Bezier Curves')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()