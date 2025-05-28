import numpy as np
import pickle
import matplotlib.pyplot as plt

tao = 0.01

exp_type = "point"
param1 = 10
param2 = 20

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

plt.plot(time_lst[:len(avg)], avg, label="Averaged Captured Molecules", color='blue')
plt.xlabel("Time (s)")
plt.ylabel("Molecules Captured")
plt.title("Averaged Data Over Time")
plt.legend()
plt.grid()
#label the average number of molecules captured with a text
if cropped_greatest_key != -1:
    plt.text(0.5, 0.9, f"{average_molecules:.2f} molecules transmitted on average", transform=plt.gca().transAxes, fontsize=12, color='red', ha='center')

plt.show()