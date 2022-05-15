import sys

import matplotlib.pyplot as plt
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
  dataframe[['original_size', 'ipmt_size', 'zip_size']].plot(
      x='original_size',
      xlabel="Tamanho Original do Arquivo (MB)",
      ylabel="Tamanho Final do Arquivo (MB)",
      title="Benchmark de Tamanho do Arquivo"
  )
  plt.legend(["ipmt", "zip"])
  plt.savefig('./out/grafico_file_sizes.png')


def execution_time_graph(dataframe):
  dataframe[['original_size', 'ipmt_ms', 'zip_ms']].plot(
      x='original_size',
      xlabel="Tamanho Original do Arquivo (MB)",
      ylabel="Tempo de Execução (s)",
      title="Benchmark de Tempo de Execução"
  )
  plt.legend(["ipmt", "zip"])
  plt.savefig('./out/grafico_execution_time.png')


if __name__ == '__main__':
    main()
