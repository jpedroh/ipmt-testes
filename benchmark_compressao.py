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
    if file.endswith("MB") or file.endswith("txt"):
      print(f"Running test for {file}")
      result = do_benchmark_for_file(file)
      results.append(result)
      print(result)

  keys = ['original_size', 'ipmt_size', 'zip_size', 'ipmt_ms', 'zip_ms']

  with open('out/benchmark_compressao.csv', 'w', newline='') as out_file:
      dict_writer = csv.DictWriter(out_file, keys)
      dict_writer.writeheader()
      dict_writer.writerows(results)


def do_benchmark_for_file(input_file_name):
  # Fazemos a compressao com o ipmt
  ipmt_command = f"/usr/bin/time -f \"%E\" ./bin/ipmt zip {input_file_name}"
  ipmt_result = subprocess.run(ipmt_command, capture_output=True, text=True, shell=True)
  ipmt_ms = time_to_ms(ipmt_result.stderr.replace('\n', ''))

  # Fazemos a compressao com zip (benchmark)
  zip_command = f"/usr/bin/time -f \"%E\" zip {input_file_name}.zip {input_file_name}"
  zip_result = subprocess.run(zip_command, capture_output=True, text=True, shell=True)
  zip_ms = time_to_ms(zip_result.stderr.replace('\n', ''))

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


def time_to_ms(time):
  split = time.split(':')
  minutes = int(split[0])
  seconds = int(split[1].split('.')[0])
  ms = int(split[1].split('.')[1])

  return (minutes * 60 * 1000) + (seconds * 1000) + ms * 10

if __name__ == '__main__':
    main()
