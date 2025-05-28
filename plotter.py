import numpy as np
import pickle
import matplotlib.pyplot as plt

tao = 0.01

exp_type = "cylinder"
param1 = 10
param2 = 40

cropped_greatest_key = -1

file_path = f"records/{exp_type}_{param1}_{param2}.pkl"
data = pickle.load(open(file_path, "rb"))

greatest_key = -1

total_molecules = 0
for dct in data:
    for key in dct.keys():
        if key > greatest_key:
            greatest_key = key
        total_molecules += dct[key]
        
average_molecules = total_molecules / len(data)

if cropped_greatest_key != -1:
    greatest_key = cropped_greatest_key
t = 0
final_lst = []

while t <= greatest_key:
    val = 0
    for dct in data:
        val += dct.get(t, 0)
    final_lst.append(val)
    t += tao
    t = round(t, 2)
    

ary = np.array(final_lst)

avg = ary  / len(data)

time_lst = np.arange(0, len(avg) * tao, tao)

title = ""
if exp_type == "point":
    title = f"Point Tx With Rx Radius: {param1}, Distance: {param2}"
elif exp_type == "cylinder":
    title = f"Cylindrical Environment With Rx Radius: {param1}, Distance: {param2}"
elif exp_type == "spherical":
    title = f"Spherical Tx/Rx With Tx/Rx Radius: {param1}, Distance: {param2}"

if cropped_greatest_key != -1:
    title += f" (Cropped at t = {cropped_greatest_key})"

save_name = f"plots/{exp_type}_{param1}_{param2}.png"
if cropped_greatest_key != -1:
    save_name = f"plots/{exp_type}_{param1}_{param2}_cropped.png"

plt.plot(time_lst[:len(avg)], avg, label="", color='blue')
plt.xlabel("Time (s)")
plt.ylabel("Molecules Captured on Average")
plt.title(title)
plt.legend()
plt.grid()
#label the average number of molecules captured with a text
if cropped_greatest_key == -1:
    plt.text(0.5, 0.9, f"{average_molecules:.2f} molecules transmitted on average", transform=plt.gca().transAxes, fontsize=12, color='red', ha='center')
plt.savefig(save_name)

plt.show()