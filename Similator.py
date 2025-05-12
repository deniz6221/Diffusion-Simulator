import random
import argparse
import math

class Molecule:
    def __init__(self, position):
        self.position = position
        self.transmitted = False

    def add_position(self, position):
       self.position = self.position[0] + position[0], self.position[1] + position[1], self.position[2] + position[2]


class Similator:
    def __init__(self):
        self.num_points = 1000
        self.num_target_points = 600
        self.tao = 0.01
        self.D = math.pow(10, -10)  # Diffusion coefficient in m^2/s
        self.step_size = math.sqrt(self.D*2*self.tao) * 1e6 # Step size in micrometers

    def point_transmission(self, reciever_distance = 15, transmission_coordinate = (0, 0, 0), reciever_radius = 10):

        molecules = [Molecule(transmission_coordinate) for _ in range(self.num_points)]
        transmitted = 0
        reciever_center = (transmission_coordinate[0] + reciever_distance + reciever_radius, transmission_coordinate[1], transmission_coordinate[2])
        
        while transmitted < self.num_target_points:       
            for i in range(len(molecules)):
                if transmitted >= self.num_target_points:
                    break
                current_molecule = molecules[i]
                if current_molecule.transmitted:
                    continue
                if self._molecule_contacts_sphere(current_molecule.position, reciever_center, reciever_radius):
                    transmitted += 1
                    print(f"Molecule {i} transmitted to the receiver at {current_molecule.position}, total transmitted: {transmitted}")
                    current_molecule.transmitted = True
                    continue
                random_distance = (random.choice([-1, 1]) * self.step_size, random.choice([-1, 1]) * self.step_size, random.choice([-1, 1]) * self.step_size)
                current_molecule.add_position(random_distance)              
            

    def _molecule_contacts_sphere(self, position, reciever_center, reciever_radius):
        distance = ((position[0] - reciever_center[0]) ** 2 + (position[1] - reciever_center[1]) ** 2 + (position[2] - reciever_center[2]) ** 2) ** 0.5
        if distance <= reciever_radius:
            return True
        return False
    

if __name__ == "__main__":
    sim = Similator()
    sim.point_transmission()
    