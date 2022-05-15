from math import log2
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
  file_name = sys.argv[1]
  dataframe = pd.read_csv(file_name)

  apply_dataframe_transformations(dataframe)

  file_sizes_graph(dataframe)
  execution_time_graph(dataframe)


def apply_dataframe_transformations(df):
  df['original_size'] = df['original_size'].transform(lambda x: x / 1024 / 1024)
  df['ipmt_size'] = df['ipmt_size'].transform(lambda x: x / 1024 / 1024)
  df['zip_size'] = df['zip_size'].transform(lambda x: x / 1024 / 1024)
  df['ipmt_ms'] = df['ipmt_ms'].transform(lambda x: x / 1000)
  df['zip_ms'] = df['zip_ms'].transform(lambda x: x / 1000)


def file_sizes_graph(dataframe):
  dataframe[['ipmt_size', 'zip_size']].plot(
      xlabel="Tamanho Original do Arquivo (MB)",
      ylabel="Tamanho Final do Arquivo (MB)",
      title="Benchmark de Tamanho do Arquivo"
  )
  
  x = np.linspace(1, max(dataframe['original_size']), len(dataframe['original_size']))
  plt.plot(x, x, 'b')

  plt.legend(["ipmt", "zip", 'original'])
  plt.savefig('./out/grafico_file_sizes.png')


def execution_time_graph(dataframe):
  dataframe[['original_size', 'ipmt_ms', 'zip_ms']].plot(
      x='original_size',
      xlabel="Tamanho Original do Arquivo (MB)",
      ylabel="Tempo de Execução (s)",
      title="Benchmark de Tempo de Execução"
  )
  x = np.linspace(1, max(dataframe['original_size']), len(dataframe['original_size']))
  n2 = (x**2)*0.15
  plt.plot(x, n2, 'r')

  plt.legend(["ipmt", "zip", '$O(n^2)$'])
  plt.savefig('./out/grafico_execution_time.png')


if __name__ == '__main__':
    main()
