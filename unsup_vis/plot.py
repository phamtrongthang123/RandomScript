
from itertools import product

import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import seaborn as sns

from typing import Tuple, List

from PIL import Image

import torch
import torchvision.transforms as T

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.manifold import TSNE
from scipy import stats

import argparse
import os
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Callable, Union

# from utils import plot_confusion_matrix, plot_scatter

plt.rcParams['figure.figsize'] = (30, 30)
mpl.rcParams['figure.dpi'] = 300
plt.rcParams['figure.dpi'] = 300


def plot_scatter(x: np.ndarray, colors: np.ndarray, save_path="scatter_plot.pdf") -> Tuple:
    """
    Render a scatter plot with as many as unique colors as the number of classes in `colors`
    Args:
        x: 2-D array output of t-sne algorithm
        colors: 1-D array containing the labels of the dataset
    Return:
        Tuple
    """
    # Choose a color palette with seaborn
    n_classes: int = len(np.unique(colors))
    palette: np.ndarray = np.array(sns.color_palette("hls", n_classes))

    # Create a scatter plot
    figure = plt.figure()
    ax = plt.subplot(aspect="equal")
    scatter = ax.scatter(x[:, 0], x[:, 1], lw=0, s=40, c=palette[colors.astype(int)])
    ax.axis("off")
    ax.axis("tight")

    # Add the labels for each digits corresponding to the label\
    txts: List = []

    for i in range(n_classes):
        # Position of each label at median of data points
        x_text, y_text = np.median(x[colors == i, :], axis=0)
        txt = ax.text(x_text, y_text, str(i), fontsize=20)
        txt.set_path_effects([
            PathEffects.Stroke(linewidth=5, foreground="w"),
            PathEffects.Normal()
        ])
        txts.append(txt)

    if save_path:
        print("Saving scatter plot at:", save_path)
        plt.savefig(save_path, dpi=300)
    return figure, ax, scatter


if __name__ == "__main__":
    batch = 32
    hidden = 100
    X_train = np.random.random([batch,hidden])*100
    y_train = np.random.randint(0,10,batch)
    tsne = TSNE(n_components=2, perplexity=7, learning_rate=20, n_iter=1000, n_jobs=-1, random_state=2611)
    X_transformed = tsne.fit_transform(X_train)
    plot_scatter(X_transformed, y_train, save_path="tsne.pdf")
