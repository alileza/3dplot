from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv

x =[[],[]]
y =[[],[]]
z =[[],[]]

with open('/app/data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        try:
            x[int(row[0])].append(float(row[1]))
            y[int(row[0])].append(float(row[2]))
            z[int(row[0])].append(float(row[3]))
        except IndexError as err:
            x.append([])
            y.append([])
            z.append([])
            x[int(row[0])].append(float(row[1]))
            y[int(row[0])].append(float(row[2]))
            z[int(row[0])].append(float(row[3]))



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for index, value in enumerate(x):
    ax.scatter(x[index], y[index], z[index], c='r', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.savefig(f'/out/{index}.png')