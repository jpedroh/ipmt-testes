import sys


def main():
    input_file_name = sys.argv[1]
    max_mega_bytes = int(sys.argv[2])
    mega_bytes = 1

    with open(input_file_name, 'r', errors="ignore") as in_file:
        lines = in_file.readlines()
        section = []
        cur_size = 0

        for i in range(0, len(lines)):
          if(mega_bytes == max_mega_bytes):
              break
          section.append(lines[i])
          cur_size += lines[i].__sizeof__()

          if(cur_size > mega_bytes * 1000 * 1000 * 2):
            print(f"Writing file of {mega_bytes}MB", cur_size)
            with open(f"{input_file_name}.{mega_bytes:03}MB", "w") as out_file:
                out_file.write("\n".join(section))
                out_file.close()
                mega_bytes += 1


if __name__ == '__main__':
    main()
