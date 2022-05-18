import subprocess


def main():
  for i in range(1, 129):
    command = f"./bin/gentext data/var_alph/var_alph.{i:03}.txt 50 {i}"
    subprocess.run(command, capture_output=True, text=True, shell=True)


if __name__ == '__main__':
    main()
