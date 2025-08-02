import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Placing the Sun
fig = plt.figure(figsize = (8,6), dpi = 100)
ax = fig.add_subplot(1,1,1, projection = '3d')
sun = np.array([0,0,0])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_label('Z axis')
ax.set_title('Trajectory Of The Parker Solar Probe')
ax.scatter(0,0,0, color = '#FFD700', edgecolors = '#FFB347', label = 'Sun', s=150)

# Defining a function for The Orbit Equation
def orbit(a, e, i, theta):
    r = (a*(1-e**2))/(1+e*np.cos(theta)) # orbit formula
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    inc_rad = np.radians(i)
    y_tilted = y*np.cos(inc_rad)
    z = y*np.sin(inc_rad)
    return x, y_tilted, z

# Defining a function for placing The Planet
def position(a, e, i, theta_in_rad):
    r = (a * (1 - e**2)) / (1 + e * np.cos(theta_in_rad))
    x = r * np.cos(theta_in_rad)
    y = r * np.sin(theta_in_rad)
    inc_rad = np.radians(i)
    y_tilted = y * np.cos(inc_rad)
    z = y * np.sin(inc_rad)
    return x, y_tilted, z

theta = np.linspace(0,2*np.pi, 1000)

earth_x, earth_y, earth_z = orbit(1.000, 0.0167, 0, theta) # a (AU), e, tilt (i)
venus_x, venus_y, venus_z = orbit(0.723, 0.0068, 3.4, theta)
mercury_x, mercury_y, mercury_z = orbit(0.387, 0.2056, 7.0, theta)

ax.plot(earth_x, earth_y, earth_z, label = 'Earth Orbit', color = '#7BC6E2')
ax.plot(venus_x, venus_y, venus_z, label = 'Venus Orbit', color = '#E6C07B')
ax.plot(mercury_x, mercury_y, mercury_z, label = 'Mercury Orbit', color = '#8B7D7B')

theta_earth = np.radians(180) # positions at the time of launch
theta_venus = np.radians(80)
theta_mercury = np.radians(50)

x_e, y_e, z_e = position(1.000, 0.0167, 0, theta_earth)
x_v, y_v, z_v = position(0.723, 0.0068, 3.4, theta_venus)
x_m, y_m, z_m = position(0.387, 0.2056, 7.0, theta_mercury)

ax.scatter(x_e, y_e, z_e, label = 'Earth', color = '#1B6CA8', edgecolors = '#CAF0F8', s = 50)
ax.scatter(x_v, y_v, z_v, label = 'Venus', color = '#C1923A', edgecolors = '#F9DDB1', s = 50)
ax.scatter(x_m, y_m, z_m, label = 'Mercury', color = '#87552D', edgecolors = '#A08679', s = 50)

# Data from NASA Horizons System.
psp_data = [
    {"a": 0.594, "e": 0.711, "i": 7.53, "ta": 180.81},  # Launch
    {"a": 0.616, "e": 0.673, "i": 5.66, "ta": 216.63},  # Venus Flyby 1
    {"a": 0.553, "e": 0.699, "i": 3.36, "ta": 3.97},    # Perihelion 1
    {"a": 0.553, "e": 0.699, "i": 3.36, "ta": 178.99},  # Aphelion 1
    {"a": 0.553, "e": 0.699, "i": 3.36, "ta": 348.82},  # Perihelion 2
    {"a": 0.553, "e": 0.699, "i": 3.36, "ta": 352.60},  # Perihelion 3
    {"a": 0.552, "e": 0.700, "i": 3.36, "ta": 207.58},  # Venus Flyby 2
    {"a": 0.505, "e": 0.742, "i": 3.39, "ta": 358.67},  # Perihelion 4
    {"a": 0.505, "e": 0.742, "i": 3.39, "ta": 0.11},    # Perihelion 5
    {"a": 0.455, "e": 0.793, "i": 3.38, "ta": 165.68},  # Venus Flyby 3
    {"a": 0.454, "e": 0.792, "i": 3.38, "ta": 358.52},  # Perihelion 6
    {"a": 0.454, "e": 0.792, "i": 3.38, "ta": 342.90},  # Perihelion 7
    {"a": 0.454, "e": 0.793, "i": 3.38, "ta": 165.14},  # Venus Flyby 4
    {"a": 0.426, "e": 0.827, "i": 3.40, "ta": 359.18},  # Perihelion 8
    {"a": 0.426, "e": 0.827, "i": 3.40, "ta": 331.76},  # Perihelion 9
    {"a": 0.421, "e": 0.830, "i": 3.39, "ta": 190.08},  # Venus Flyby 5
    {"a": 0.412, "e": 0.850, "i": 3.39, "ta": 0.21},    # Perihelion 10
    {"a": 0.412, "e": 0.850, "i": 3.39, "ta": 334.86},  # Perihelion 11
    {"a": 0.412, "e": 0.850, "i": 3.39, "ta": 313.12},  # Perihelion 12
    {"a": 0.412, "e": 0.850, "i": 3.39, "ta": 8.78},    # Perihelion 13
    {"a": 0.412, "e": 0.850, "i": 3.39, "ta": 342.83},  # Perihelion 14
    {"a": 0.412, "e": 0.850, "i": 3.39, "ta": 319.57},  # Perihelion 15
    {"a": 0.412, "e": 0.850, "i": 3.39, "ta": 16.93},   # Perihelion 16
    {"a": 0.410, "e": 0.851, "i": 3.39, "ta": 187.12},  # Venus Flyby 6
    {"a": 0.399, "e": 0.867, "i": 3.39, "ta": 302.21},  # Perihelion 17
    {"a": 0.399, "e": 0.867, "i": 3.40, "ta": 32.84},   # Perihelion 18
    {"a": 0.399, "e": 0.867, "i": 3.40, "ta": 27.05},   # Perihelion 19
    {"a": 0.399, "e": 0.867, "i": 3.40, "ta": 21.03},   # Perihelion 20
    {"a": 0.398, "e": 0.867, "i": 3.40, "ta": 14.64},   # Perihelion 21
    {"a": 0.397, "e": 0.867, "i": 3.40, "ta": 174.94},  # Venus Flyby 7
    {"a": 0.387, "e": 0.882, "i": 3.40, "ta": 341.93},  # Perihelion 22
    {"a": 0.387, "e": 0.882, "i": 3.40, "ta": 295.79},  # Perihelion 23
    {"a": 0.387, "e": 0.882, "i": 3.40, "ta": 356.25},  # Perihelion 24
]

psp_x_all, psp_y_all, psp_z_all = [], [], []

for idx in range(len(psp_data) - 1):
    current = psp_data[idx]
    next_ = psp_data[idx + 1]

    a, e, i = current["a"], current["e"], current["i"]
    ta1 = current["ta"]
    ta2 = next_["ta"]

    if ta2 < ta1:
        ta2 += 360
    
    theta_vals = np.radians(np.linspace(ta1, ta2, 80))
    x_seg, y_seg, z_seg = orbit(a, e, i, theta_vals)

    psp_x_all.extend(x_seg)
    psp_y_all.extend(y_seg)
    psp_z_all.extend(z_seg)

psp_trail, = ax.plot([], [], [], color ='#800E13', label = 'PSP Path')
psp_dot, = ax.plot([], [], [], marker ='*', color ='#640D14', markersize = 6)

def update(frame):
    psp_trail.set_data(psp_x_all[:frame], psp_y_all[:frame])
    psp_trail.set_3d_properties(psp_z_all[:frame])
    psp_dot.set_data([psp_x_all[frame]], [psp_y_all[frame]])
    psp_dot.set_3d_properties([psp_z_all[frame]])
    return psp_trail, psp_dot

animation = FuncAnimation(fig = fig, func = update, frames = len(psp_x_all), interval = 15, repeat = False)
ax.legend(loc = 0)
animation.save('Parker_Solar_Probe_Trajectory.mp4', writer = 'ffmpeg')
plt.show()