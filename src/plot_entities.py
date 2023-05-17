"""
Plots the distribution of the entities in the dataset
"""

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
from pathlib import Path

plt.rcParams["font.family"] = "serif"


def plot_entities(dfs, save_path = None):
    """
    Plots the distribution of the entities in each of the subcorpora

    Parameters
    ----------
    dfs : dict
        Dictionary with the dataframes for each subcorpus (key = subcorpus name)
    save_path : str
        Path to save the plot to. If None, the plot is not saved.
    """

    fig, ax = plt.subplots(1, figsize=(10, 6), dpi = 300)

    # define colour palette
    palette = cm.get_cmap("Paired").colors
    palette = [palette[3], palette[0], palette[1], palette[2]]

    # x ticks (all keys)
    x = list(dfs.keys())

    ys = {}

    # loop over columns and get mean for each subcorpus
    for col in dfs[x[0]].columns[1:5]:
        y = [df[col].mean() for df in dfs.values()]
        ys[col] = y


    # plot with bars, next to each other
    width = 0.2
    for i, col in enumerate(ys.keys()):
        ax.bar(np.arange(len(x)) + width * i, ys[col], width, label=col.split("_")[-1], color = palette[i])

    # set x ticks
    ax.set_xticks(np.arange(len(x)) + width, x)

    # set legend
    ax.legend()

    # set labels
    ax.set_xlabel("Subcorpus")

    ax.set_title("Relative frequency per 10.000 words")

    plt.tight_layout()


    if save_path:
        plt.savefig(save_path)

    

def main():
    path = Path(__file__)
    results_path = path.parents[1] / "out"

    results = {}
    # loop over files
    for f in results_path.iterdir():
        if f.name.endswith(".csv"):
            # read file
            df = pd.read_csv(f)
            # add to results
            results[f.name] = df

    # plot
    plot_entities(results, path.parents[1] / "out" / "entities.png")
    

if __name__ == "__main__":
    main()