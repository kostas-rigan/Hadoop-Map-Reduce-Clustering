import numpy as np
import pandas as pd
from random import randrange
import json

with open('config.json') as f:
    config = json.load(f)

centers = [tuple(config['center1']), tuple(config['center2']), tuple(config['center3'])]

data_points = config['data_points']
sequence = [randrange(len(centers)) for _ in range(data_points)]
kappa = config['kappa']
theta = config['theta']
skewed_distances_x = np.random.gamma(kappa, theta, data_points)
skewed_distances_y = np.random.gamma(kappa, theta, data_points)

x_points_lst = []
y_points_lst = []

for pos in sequence:
    tup = centers[pos]
    x_points_lst.append(tup[0])
    y_points_lst.append(tup[1])

x_points = np.array(x_points_lst)
y_points = np.array(y_points_lst)

x_points = x_points + skewed_distances_x
y_points = y_points + skewed_distances_y

points = pd.DataFrame({'x': x_points, 'y': y_points})
points.to_csv('data.txt', sep=',', index=False)
