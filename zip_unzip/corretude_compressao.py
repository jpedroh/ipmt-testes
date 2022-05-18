import subprocess
import sys

def main():
  input_file_name = sys.argv[1]

  # Fazemos a compressao
  compression_command = f"./bin/ipmt zip {input_file_name}"
  subprocess.run(compression_command, capture_output=True, text=True, shell=True)

  # Fazemos a descompressao
  decompression_command = f"./bin/ipmt unzip {input_file_name}.myz"
  subprocess.run(decompression_command, capture_output=True, text=True, shell=True)

  # Fazemos um diff entre o arquivo de entrada e o resultado da decompressão
  diff_command = f"diff {input_file_name} {input_file_name}.original"
  diff_result = subprocess.run(diff_command, capture_output=True, text=True, shell=True)

  if diff_result.returncode != 0:
    print("[ERRO] A saida dos arquivos foi diferente.")

if __name__ == '__main__':
    main()
