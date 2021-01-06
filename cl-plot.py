#!/usr/bin/env python3
"""
Plot heatmap or contour graphs from MadnAnalysis parameter scan

Author: Ed van Bruggen <edvb@uw.edu>
"""

import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import os
import sys
from scipy.interpolate import griddata

np.set_printoptions(threshold=sys.maxsize, linewidth=np.inf)

exp_data = np.zeros((6,7))
obs_data = np.zeros((6,7))
directory = 'monosbb'
data = []

for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    mhs = int(filename.split('-')[1])
    mzp = int(filename.split('-')[2].split('.')[0])
    with open(path, "r") as file:
        lines = file.readlines()
        xsec = float(lines[3])
        exp = float(lines[1].split()[3])
        obs = float(lines[1].split()[4])
        data.append(np.array([mhs, mzp, xsec, exp, obs]))
        exp_data[(mhs-50)//20,mzp//500-1] = exp/xsec
        obs_data[(mhs-50)//20,mzp//500-1] = obs/xsec
    # print(f"{mhs} {mzp}: {mzp//500},{(mhs-50)//20}")
# print(exp_data)
# print(obs_data)
# print(data)
data = np.asarray(data)

def plot_heatmap(data, name):
    ax = sns.heatmap(data, annot=True, linewidth=0.5)

    ax.set_xlabel("M_Z' (GeV)")
    ax.set_ylabel("M_S (GeV)")
    ax.set_title(f'CL {name} Results')
    ax.invert_yaxis()
    ax.set_yticklabels(list(range(50, 170, 20)))
    ax.set_xticklabels(list(range(500, 4000, 500)))
    plt.show()
    fig = plt.figure()

    fig.savefig('plot.png')

# d = np.asarray([list(map(float,x.split())) for x in a.splitlines()[1:]])

def plot_contour(data):
    # grid = grid_x, grid_y = np.mgrid[50:150:51j, 500:3500:501j]
    grid = grid_x, grid_y = np.mgrid[0:1800:101j, 0:1200:101j]
    v = griddata(data[:,[1,0]], data[:,-1]/data[:,-3], (grid_x, grid_y), method='linear')
    plt.contourf(grid_x,grid_y,np.log(v), alpha =  1.0, levels = np.linspace(-6,5,100), vmin = -5, vmax = 5)
    plt.colorbar()
    # CS = plt.contour(grid_x,grid_y,v, alpha =  1.0, levels = np.logspace(-2,2,10), colors = 'w')
    # plt.clabel(CS, CS.levels, inline=True, fontsize=10)
    CS = plt.contour(grid_x,grid_y,v, alpha =  1.0, levels = [1.0], colors = 'black')
    plt.clabel(CS, CS.levels, inline=True, fontsize=10)
    plt.xlabel("M_Z' (GeV)")
    plt.ylabel("M_S (GeV)")
    plt.title(f'CL Observed Contour')
    plt.ylim(50,150)
    plt.xlim(500,2000)
    # plt.yticklabels(list(range(50, 170, 20)))
    # plt.xticklabels(list(range(500, 4000, 500)))
    plt.gcf().set_size_inches(5,5)
    plt.show()

# plot_heatmap(exp_data, 'Expected')
# plot_heatmap(obs_data, 'Observed')
plot_contour(data)

