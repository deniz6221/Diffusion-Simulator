# Molecular Diffusion Simulator

This project simulates molecular diffusion in different environments using a stochastic approach with random walk models. It can be used to study molecular communication in various environments including point-to-point transmission, spherical transmission, and cylindrical environments.

## Features

- Point-to-point molecular transmission
- Spherical transmission simulation
- Cylindrical environment simulation
- 3D visualization with VPython
- Interactive barrel cylinder animation
- Data collection and storage for analysis

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The simulator can be run with different experiment types using command-line arguments:

### Point-to-Point Transmission

```bash
python similator.py --exp_type point --reciever_distance 15 --reciever_radius 10
```

### Spherical Transmission

```bash
python similator.py --exp_type spherical --reciever_distance 15 --reciever_radius 10 --transmission_sphere_radius 10
```

### Cylindrical Environment

```bash
python similator.py --exp_type cylinder --reciever_distance 15 --reciever_radius 10 --cylinder_radius 15
```

### Interactive Barrel Visualization

```bash
python similator.py --exp_type barrel --reciever_distance 5 --reciever_radius 10
```

## Parameters

- `--exp_type`: Type of experiment (point, spherical, cylinder, barrel)
- `--reciever_distance`: Distance to the receiver (default: 15)
- `--reciever_radius`: Radius of the receiver (default: 10)
- `--transmission_sphere_radius`: Radius of transmission sphere (default: 10)
- `--cylinder_radius`: Radius of the cylinder (default: 15)

## Visualization Controls

In the interactive barrel visualization:
- Use WASD keys to navigate horizontally
- Use Q/E to move up/down
- Press X to exit the simulation

## Output

Simulation results are stored in the `records/` directory with filenames indicating the experiment parameters.
