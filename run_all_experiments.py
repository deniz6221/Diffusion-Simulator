import subprocess
import sys
if __name__ == "__main__":
    
    script = "Similator.py"
    
    point_sim_params = [
        {
            "exp_type": "point",
            "reciever_distance": 5,
            "reciever_radius": 10
        },
        {
            "exp_type": "point",
            "reciever_distance": 10,
            "reciever_radius": 10
        },
        {
            "exp_type": "point",
            "reciever_distance": 15,
            "reciever_radius": 10
        },
        {
            "exp_type": "point",
            "reciever_distance": 20,
            "reciever_radius": 10
        },
        {
            "exp_type": "point",
            "reciever_distance": 25,
            "reciever_radius": 10
        },
        {
            "exp_type": "point",
            "reciever_distance": 15,
            "reciever_radius": 5
        },
        {
            "exp_type": "point",
            "reciever_distance": 15,
            "reciever_radius": 10
        },
        {
            "exp_type": "point",
            "reciever_distance": 15,
            "reciever_radius": 15
        },
        {
            "exp_type": "point",
            "reciever_distance": 15,
            "reciever_radius": 20
        }
    ]

    # transmision_sphere_radius = reciever_radius
    spherical_sim_params = [
        {
            "exp_type": "spherical",
            "reciever_distance": 5,
            "reciever_radius": 10,
            "tranmission_sphere_radius": 10
        },
        {
            "exp_type": "spherical",
            "reciever_distance": 10,
            "reciever_radius": 10,
            "tranmission_sphere_radius": 10
        },
        {
            "exp_type": "spherical",
            "reciever_distance": 15,
            "reciever_radius": 10,
            "tranmission_sphere_radius": 10
        },
        {
            "exp_type": "spherical",
            "reciever_distance": 20,
            "reciever_radius": 10,
            "tranmission_sphere_radius": 10
        },
        {
            "exp_type": "spherical",
            "reciever_distance": 25,
            "reciever_radius": 10,
            "tranmission_sphere_radius": 10
        },
        {
            "exp_type": "spherical",
            "reciever_distance": 15,
            "reciever_radius": 5,
            "tranmission_sphere_radius": 5
        },
        {
            "exp_type": "spherical",
            "reciever_distance": 15,
            "reciever_radius": 10,
            "tranmission_sphere_radius": 10
        },
        {
            "exp_type": "spherical",
            "reciever_distance": 15,
            "reciever_radius": 15,
            "tranmission_sphere_radius": 15
        },
        {
            "exp_type": "spherical",
            "reciever_distance": 15,
            "reciever_radius": 20,
            "tranmission_sphere_radius": 20
        }
    ]

    # Cylinder radius fixed = 15 spherical receiver radius fixed = 10
    #Vary distance to receiver: 5 to 40 µm (in steps of 5 µm)
    cylindrical_sim_params = [
        {
            "exp_type": "cylinder",
            "reciever_distance": 5,
            "reciever_radius": 10,
            "cylinder_radius": 15
        },
        {
            "exp_type": "cylinder",
            "reciever_distance": 10,
            "reciever_radius": 10,
            "cylinder_radius": 15
        },
        {
            "exp_type": "cylinder",
            "reciever_distance": 15,
            "reciever_radius": 10,
            "cylinder_radius": 15
        },
        {
            "exp_type": "cylinder",
            "reciever_distance": 20,
            "reciever_radius": 10,
            "cylinder_radius": 15
        },
        {
            "exp_type": "cylinder",
            "reciever_distance": 25,
            "reciever_radius": 10,
            "cylinder_radius": 15
        },
        {
            "exp_type": "cylinder",
            "reciever_distance": 30,
            "reciever_radius": 10,
            "cylinder_radius": 15
        },
        {
            "exp_type": "cylinder",
            "reciever_distance": 35,
            "reciever_radius": 10,
            "cylinder_radius": 15
        },
        {
            "exp_type": "cylinder",
            "reciever_distance": 40,
            "reciever_radius": 10,
            "cylinder_radius": 15
        }
    ]

    for params in point_sim_params:
        cmd = [sys.executable, script] + [f"--{k}={v}" for k, v in params.items()]
        subprocess.run(cmd)
    
    print("Point experiments completed.")
    for params in spherical_sim_params:
        cmd = [sys.executable, script] + [f"--{k}={v}" for k, v in params.items()]
        subprocess.run(cmd)
    
    print("Spherical experiments completed.")
    for params in cylindrical_sim_params:
        cmd = [sys.executable, script] + [f"--{k}={v}" for k, v in params.items()]
        subprocess.run(cmd)