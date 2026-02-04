# Parker Solar Probe Orbit Simulation

This Python project simulates and animates the orbital trajectory of NASA’s Parker Solar Probe using real orbital elements obtained from the NASA JPL Horizons System. The simulation captures the spacecraft’s heliocentric motion through over 2,513 days of data including multiple perihelions and 7 Venus gravity assists, showing how its orbit continuously shrinks as it approaches the Sun.

The animation is rendered in 3D using matplotlib and includes the reference orbits of Earth, Venus and Mercury to provide spatial context for the probe’s unique path.

## Features

- Sun fixed at the origin in a heliocentric frame.
- 3D representation of Earth’s, Venus’s and Mercury’s orbits.
- Animated trajectory of Parker Solar Probe across multiple orbital revolutions.
- Uses accurate orbital parameters:
  - Semi-major axis (a)
  - Eccentricity (e)
  - Inclination (i)
  - True anomaly (θ)

## Tech Stack

- **Python 3**
- **NumPy** for mathematical operations
- **Matplotlib** for 3D plotting and animation
- **Pandas** for data retrieval 
- **NASA JPL Horizons** data for orbital elements

## Orbital Mechanics & Physics Used

This simulation uses classical two-body orbital mechanics. The following key equations and concepts are implemented:

- **Position in Orbit**  
  r = a(1 − e²) / (1 + e cos θ)
  - To compute the radial distance r of the probe from the Sun at a given true anomaly θ

- **Kepler’s Laws of Planetary Motion**  
 Although not directly used in code, this principle applies to the simulation:
  - A planet (or spacecraft) sweeps out equal areas in equal times.
  - Implies that the probe moves faster near perihelion and slower near aphelion.

## What This Project Demonstrates

- Understanding of spacecraft motion using classical orbital mechanics.
- Application of real scientific data to simulate a real-world mission.
- Visualization of time-evolving orbital paths in 3D.
  
## Educational Purpose

This simulation is an independent academic exploration in orbital mechanics. It serves as a hands-on project to deepen my understanding of spacecraft trajectories, planetary motion and data-driven visualizations using Python. 

The help of AI has been taken in a few parts such as retrieving data from a txt file as NASA JPL Horizons system provided the data in that format. Despite the use of AI, this project enhanced my understanding and experience with working on real-world data.

## License

MIT License
