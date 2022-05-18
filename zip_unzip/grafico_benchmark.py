import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    file_name = sys.argv[1]
    category = sys.argv[2]
    dataframe = pd.read_csv(file_name)

    apply_dataframe_transformations(dataframe)

    file_sizes_graph(dataframe, category)
    execution_time_graph(dataframe, category)


def apply_dataframe_transformations(df):
    df['original_size'] = df['original_size'].transform(
        lambda x: x / 1024 / 1024)
    df['ipmt_size'] = df['ipmt_size'].transform(lambda x: x / 1024 / 1024)
    df['zip_size'] = df['zip_size'].transform(lambda x: x / 1024 / 1024)
    df['ipmt_ms'] = df['ipmt_ms'].transform(lambda x: x / 1000)
    df['zip_ms'] = df['zip_ms'].transform(lambda x: x / 1000)


def file_sizes_graph(dataframe, category):
    dataframe[['ipmt_size', 'zip_size']].plot(
        xlabel="Tamanho Original do Arquivo (MB)",
        ylabel="Tamanho Final do Arquivo (MB)",
        title=f"Benchmark de Tamanho do Arquivo ({category})"
    )

    x = np.linspace(1, max(dataframe['original_size']), len(
        dataframe['original_size']))
    plt.plot(x, x, 'b')

    plt.legend(["ipmt", "zip", 'original'])
    plt.savefig(f'./graphs/grafico_file_sizes_{category}.png')


def execution_time_graph(dataframe, category):
    dataframe[['original_size', 'ipmt_ms', 'zip_ms']].plot(
        x='original_size',
        xlabel="Tamanho Original do Arquivo (MB)",
        ylabel="Tempo de Execução (s)",
        title=f"Benchmark de Tempo de Execução ({category})"
    )

    plt.legend(["ipmt", "zip"])
    plt.savefig(f'./graphs/grafico_execution_time_{category}.png')


if __name__ == '__main__':
    main()
