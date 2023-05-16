"""
Plots the distribution of the entities in the dataset
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

plt.rcParams["font.family"] = "serif"

def plot_entities(dfs, save_path):

    fig, ax = plt.subplots(1, figsize=(10, 5), dpi = 300)

    # x ticks (all keys)
    x = list(dfs.keys())

    ys = {}
    # loop over columns
    for i, col in enumerate(dfs[x[0]].columns[1:5]):
        # y values
        y = [df[col].mean() for df in dfs.values()]

        # add to dict
        ys[col] = y


    # plot with bars, next to each other
    width = 0.2
    for i, col in enumerate(ys.keys()):
        ax.bar(np.arange(len(x)) + width * i, ys[col], width, label=col.split("_")[-1])

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