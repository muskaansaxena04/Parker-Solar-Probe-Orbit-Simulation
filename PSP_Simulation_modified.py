import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import re

# Defining a Function for Orbit

def orbit(a, e, i, theta):
    r = (a * (1 - e**2)) / (1 + e * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    inc_rad = np.radians(i)
    y_tilted = y * np.cos(inc_rad)
    z = y * np.sin(inc_rad)
    return x, y_tilted, z


# Data From NASA JPL Horizons

def parse_daily_data(data_block):
    parsed_data = {}

    date_match = re.search(r'A\.D\.\s+(\d{4}-\w{3}-\d{2})', data_block)
    if date_match:
        parsed_data['Date'] = date_match.group(1)
    else:
        return None

    matches = re.findall(r'([A-Za-z]+)\s*=\s*([\d.E+-]+)', data_block)
    for key, value in matches:
        try:
            parsed_data[key] = float(value)
        except ValueError:
            parsed_data[key] = value

    return parsed_data

file_path = r"C:\Users\Muskaan\Desktop\new\All_Data.txt"

with open(file_path, "r") as file:
    content = file.read()

daily_blocks = re.split(
    r'(?=A\.D\.\s+\d{4}-\w{3}-\d{2})',
    content.strip()
)

all_data_list = []
for block in daily_blocks:
    if block.strip():
        daily_data = parse_daily_data(block)
        if daily_data:
            all_data_list.append(daily_data)

df = pd.DataFrame(all_data_list)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.sort_values('Date').reset_index(drop=True)

# Figure Setup

fig = plt.figure(figsize=(8, 6), dpi=100)
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('X axis (AU)')
ax.set_ylabel('Y axis (AU)')
ax.set_zlabel('Z axis (AU)')
ax.set_title('Trajectory of the Parker Solar Probe')

# Placing the Sun
ax.scatter(0, 0, 0, color='#FFD700', edgecolors='#FFB347', s=150, label='Sun')

theta = np.linspace(0, 2 * np.pi, 1000)

earth_x, earth_y, earth_z = orbit(1.000, 0.0167, 0, theta)
venus_x, venus_y, venus_z = orbit(0.723, 0.0068, 3.4, theta)
mercury_x, mercury_y, mercury_z = orbit(0.387, 0.2056, 7.0, theta)

ax.plot(earth_x, earth_y, earth_z, label='Earth Orbit', color='#7BC6E2')
ax.plot(venus_x, venus_y, venus_z, label='Venus Orbit', color='#E6C07B')
ax.plot(mercury_x, mercury_y, mercury_z, label='Mercury Orbit', color='#8B7D7B')

psp_x_all, psp_y_all, psp_z_all = [], [], []

for _, row in df.iterrows():
    a = row['A']
    e = row['EC']
    i = row['IN']
    ta = np.radians(row['TA'])

    x, y, z = orbit(a, e, i, ta)

    psp_x_all.append(x)
    psp_y_all.append(y)
    psp_z_all.append(z)

psp_trail, = ax.plot([], [], [], color='#800E13', label='PSP Path')
psp_dot, = ax.plot([], [], [], marker='*', color='#640D14', markersize=6)

def update(frame):
    psp_trail.set_data(psp_x_all[:frame], psp_y_all[:frame])
    psp_trail.set_3d_properties(psp_z_all[:frame])

    psp_dot.set_data([psp_x_all[frame]], [psp_y_all[frame]])
    psp_dot.set_3d_properties([psp_z_all[frame]])

    return psp_trail, psp_dot

animation = FuncAnimation(fig, update, frames=len(psp_x_all), interval=15, repeat=False)
ax.legend(loc=0)
animation.save('Parker_Solar_Probe_Trajectory_New.mp4', writer='ffmpeg')
plt.show()