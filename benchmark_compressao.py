import glob
import os
import subprocess
import sys
import resource
import csv


def main():
  results = []
  files = os.listdir(sys.argv[1])
  files.sort()
  for file_name in files:
    file = f"{sys.argv[1]}/{file_name}"
    if file.endswith("MB"):
      print(f"Running test for {file}")
      result = do_benchmark_for_file(file)
      results.append(result)
      print(result)

  keys = ['original_size', 'ipmt_size', 'zip_size', 'ipmt_ms', 'zip_ms']

  with open('out/benchmark.csv', 'w', newline='') as out_file:
      dict_writer = csv.DictWriter(out_file, keys)
      dict_writer.writeheader()
      dict_writer.writerows(results)


def do_benchmark_for_file(input_file_name):
  # Fazemos a compressao com o ipmt
  ipmt_command = f"/usr/bin/time -f \"%E\" ./bin/ipmt zip {input_file_name}"
  subprocess.run(ipmt_command, capture_output=True, text=True, shell=True)
  ipmt_ms = int(resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime * 1000)

  # Fazemos a compressao com zip (benchmark)
  zip_command = f"/usr/bin/time -f \"%E\" zip {input_file_name}.zip {input_file_name}"
  subprocess.run(zip_command, capture_output=True, text=True, shell=True)
  zip_ms = int(resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime * 1000)

  # Verificamos e salvamos os tamanhos de cada arquivo
  original_size = os.path.getsize(input_file_name)
  ipmt_size = os.path.getsize(f"{input_file_name}.myz")
  zip_size = os.path.getsize(f"{input_file_name}.zip")

  return {
      'original_size': original_size,
      'ipmt_size': ipmt_size,
      'zip_size': zip_size,
      'ipmt_ms': ipmt_ms,
      'zip_ms': zip_ms
  }


if __name__ == '__main__':
    main()
