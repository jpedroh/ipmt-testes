import sys

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def main():
    text_file = sys.argv[1]
    with open(text_file, 'r', errors="ignore") as file:
        lines = file.readlines()
    with open(text_file, 'w') as file:
        for line in lines:
            if is_ascii(line):
                file.write(line)

if __name__=='__main__':
    main()