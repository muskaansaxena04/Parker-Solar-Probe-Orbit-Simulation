# Parker Solar Probe Orbit Simulation (Work in Progress)

This Python project simulates and animates the orbital trajectory of NASA’s Parker Solar Probe using real orbital elements obtained from the NASA JPL Horizons System. The simulation captures the spacecraft’s heliocentric motion through over 20 perihelions and multiple Venus gravity assists, showing how its orbit continuously shrinks as it approaches the Sun.

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
- **NASA JPL Horizons** data for orbital elements

## Orbital Mechanics & Physics Used

This simulation uses classical two-body orbital mechanics under Newtonian gravity. The following key equations and concepts are implemented:

- **Position in Orbit**  
  r = a*(1 - e^2)/1 + e*cos(theta)
  - To compute the radial distance r of the probe from the Sun at a given true anomaly θ

- **Kepler’s Laws of Planetary Motion**  
 Although not directly used in code, this principle applies to the simulation:
  - A planet (or spacecraft) sweeps out equal areas in equal times.
  - Implies that the probe moves faster near perihelion and slower near aphelion.

## What This Project Demonstrates

- Understanding of spacecraft motion using classical orbital mechanics.
- Application of real scientific data to simulate a real-world mission.
- Visualization of time-evolving orbital paths in 3D.

## Future Enhancements

This project is a work in progress and will continue to evolve as I deepen my understanding of orbital mechanics. Future versions of the simulation may include:
- Time-dependent changes in velocity to reflect the probe’s speed variation during its orbit (especially near perihelion and aphelion).
- Incorporation of other parameters like:
  - Perihelion distance (rp)
  - Aphelion distance (ra)
- Improved visual realism.
  
## Educational Purpose

This simulation is part of an ongoing independent academic exploration in orbital mechanics. It serves as a hands-on project to deepen my understanding of spacecraft trajectories, planetary motion and data-driven visualizations using Python. I will continue to expand the project as I learn more advanced topics in orbital mechanics.

## License

MIT License
