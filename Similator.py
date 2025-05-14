import random
import argparse
import math
from vpython import sphere, cylinder, vector, color, rate, scene

class Molecule:
    def __init__(self, position):
        self.position = position
        self.transmitted = False

    def add_position(self, position):
       self.position = self.position[0] + position[0], self.position[1] + position[1], self.position[2] + position[2]

    def return_new_position(self, position):
        return self.position[0] + position[0], self.position[1] + position[1], self.position[2] + position[2]


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

    def spherical_transmission(self, transmission_sphere_center = (0, 0, 0), transmission_sphere_radius = 10, reciever_distance = 15,  reciever_radius = 10 ): 
        molecules = [Molecule((transmission_sphere_center[0] + transmission_sphere_radius, transmission_sphere_center[1], transmission_sphere_center[2])) for _ in range(self.num_points)]
        transmitted = 0
        reciever_center = (transmission_sphere_center[0] + reciever_distance + reciever_radius, transmission_sphere_center[1], transmission_sphere_center[2])
        
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
                new_position = current_molecule.return_new_position(random_distance)
                if self._molecule_contacts_sphere(new_position, transmission_sphere_center, transmission_sphere_radius):
                    continue
                current_molecule.position = new_position

    def point_transmission_in_cylinder(self, cylinder_radius = 15, transmission_base = (0, 0, 0), reciever_distance = 15, reciever_radius = 10): 
        transmission_point = (transmission_base[0] , transmission_base[1] + cylinder_radius, transmission_base[2])
        molecules = [Molecule(transmission_point) for _ in range(self.num_points)]
        transmitted = 0
        reciever_center = (transmission_point[0] + reciever_distance + reciever_radius, transmission_point[1], transmission_point[2])
        
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
                new_position = current_molecule.return_new_position(random_distance)
                if self._molecule_outside_cylinder(new_position, (transmission_point[1], transmission_point[2]), cylinder_radius):
                    continue
                current_molecule.position = new_position

    def barrel_cylinder_animation(self, cylinder_radius = 3, transmission_base = (0, 0, 0), cylinder_height = 30, reciever_distance_to_cylinder = 5, reciever_radius = 10): 
        step = 0.4
        def key_input(evt):
            s = evt.key
            cam = scene.camera
            if s == 'w':
                cam.pos += vector(0, 0, -step)
            elif s == 's':
                cam.pos += vector(0, 0, step)
            elif s == 'a':
                cam.pos += vector(-step, 0, 0)
            elif s == 'd':
                cam.pos += vector(step, 0, 0)
            elif s == 'q':
                cam.pos += vector(0, step, 0)
            elif s == 'e':
                cam.pos += vector(0, -step, 0)

        scene.bind('keydown', key_input)
        
        
        
        transmission_point = (transmission_base[0] , transmission_base[1] + cylinder_radius, transmission_base[2])
        molecules = [sphere(pos=vector(*transmission_point), radius=0.2, color=color.red, make_trail=False) for _ in range(self.num_points)]
        transmitter = sphere(pos=vector(*transmission_point), radius=0.4, color=color.purple)
        transmitted = 0
        reciever_center = (transmission_point[0] + reciever_distance_to_cylinder + cylinder_height + reciever_radius, transmission_point[1], transmission_point[2])
        
        reciever_sphere = sphere(pos=vector(*reciever_center), radius=reciever_radius, color=color.blue)
        cylinder_obj = cylinder(pos=vector(*transmission_point), axis=vector(cylinder_height,0,0), radius=cylinder_radius, color=color.green, opacity=0.2)

        while transmitted < self.num_target_points:     
            rate(10)  
            remove_list = []
            for i in range(len(molecules)):
                current_molecule = molecules[i]
                if self._molecule_contacts_sphere((current_molecule.pos.x, current_molecule.pos.y, current_molecule.pos.z), reciever_center, reciever_radius):
                    transmitted += 1
                    print(f"Molecule {i} transmitted to the receiver at {current_molecule.pos}, total transmitted: {transmitted}")
                    remove_list.append(i)
                    continue
                random_distance = (random.choice([-1, 1]) * self.step_size, random.choice([-1, 1]) * self.step_size, random.choice([-1, 1]) * self.step_size)
                new_position = (current_molecule.pos.x + random_distance[0], current_molecule.pos.y + random_distance[1], current_molecule.pos.z + random_distance[2])
                if self._molecule_outside_cylinder_barrel(new_position, (transmission_point[1], transmission_point[2]), cylinder_radius, cylinder_height):
                    continue
                current_molecule.pos = vector(*new_position)
            for m in reversed(remove_list):
                ml = molecules.pop(m)

                
    def _molecule_contacts_sphere(self, position, sphere_center, sphere_radius):
        distance = ((position[0] - sphere_center[0]) ** 2 + (position[1] - sphere_center[1]) ** 2 + (position[2] - sphere_center[2]) ** 2) ** 0.5
        if distance <= sphere_radius:
            return True
        return False
    
    def _molecule_outside_cylinder(self, position, cylinder_axis, cylinder_radius):
        distance = ((position[1] - cylinder_axis[0]) ** 2 + (position[2] - cylinder_axis[1]) ** 2) ** 0.5
        if distance >= cylinder_radius:
            return True
        return False
    
    def _molecule_outside_cylinder_barrel(self, position, cylinder_axis, cylinder_radius, cylinder_height):
        if position[0] > cylinder_height:
            return False
        if position[0] < 0:
            return True
        distance = ((position[1] - cylinder_axis[0]) ** 2 + (position[2] - cylinder_axis[1]) ** 2) ** 0.5
        if distance >= cylinder_radius:
            return True
        return False
    

if __name__ == "__main__":
    sim = Similator()
    sim.barrel_cylinder_animation()
    