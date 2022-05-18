import subprocess, sys, csv, datetime, os

def index_file(file_name):
    process = "/usr/bin/time -f \"%E\" ./utils/ipmt index " + file_name
    p = subprocess.run(process, capture_output=True, text=True, shell=True)
    return (p.stderr.replace('\n', ''))

def main():
    names = ["english.50MB", "english.100MB", "english.200MB", "english.1024MB", "dna.50MB", "dna.100MB", "dna.200MB"]
    values = []
    suffix_text_file = "./dataset/textos/"
    for f in names:
        values.append(index_file(suffix_text_file+f))
    
    with open("index_values.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(names)
        writer.writerow(values)

if __name__ == '__main__':
    main()
