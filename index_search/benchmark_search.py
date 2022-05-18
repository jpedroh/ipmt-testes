import subprocess, sys, csv, datetime, os

patters = {}

def pre_process_patterns(pattern_file):
    with open(pattern_file, 'r') as f:
        lines = f.readlines()
        n_line = ""
        for line in lines:
            line = line.replace('\n', "")
            if "*" not in line:
                patters[n_line].append(line)
            else:
                n_line = line.replace('*', '')
                patters[n_line] = []

def get_time(cmd, patterns, file_name):
    times = []

    for pattern in patterns:
        process = "/usr/bin/time -f \"%E\" " + cmd + " '" + pattern + "' " + file_name
        p = subprocess.run(process, capture_output=True, text=True, shell=True)
        times.append(p.stderr.replace("Command exited with non-zero status 1\n", "").replace('\n', ''))
    
    sum_time = datetime.timedelta()

    for time in times:
        (m, s) = time.split(':')
        (s, ms) = s.split('.')
        ms += '0'
        d = datetime.timedelta(minutes=int(m), seconds=int(s), milliseconds=int(ms))
        sum_time +=d
    
    sum_time /= 2

    return str(sum_time)

def write_csv(text_file):
    idx = text_file.rindex(".")
    text_file_indexed = text_file[:idx]+'.idx'

    process = "./utils/ipmt index " + text_file
    subprocess.run(process, capture_output=True, text=True, shell=True)
    csv_name = text_file+".csv"

    with open(csv_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['', 'grep', 'pmt', 'ipmt'])

        for size in patters:
            lst = []
            lst.append(size)
            lst.append(get_time("grep -c -o", patters[size], text_file))
            lst.append(get_time("./utils/pmt -c", patters[size], text_file))
            lst.append(get_time("./utils/ipmt search -c", patters[size], text_file_indexed))
            writer.writerow(lst)

def main():
    if len(sys.argv) == 3:
        pre_process_patterns(sys.argv[1])
        write_csv(sys.argv[2])
    else:
        pat_file = "./dataset/patterns_exato_completo.txt"
        pre_process_patterns(pat_file)
        suffix_text_file = "./dataset/textos/"
        for f in ["english.50MB", "english.100MB", "english.200MB", "english.1024MB"]:
            write_csv(suffix_text_file+f)
        pat_file = "./dataset/patterns_dna_completo.txt"
        pre_process_patterns(pat_file)
        suffix_text_file = "./dataset/textos/"
        for f in ["dna.50MB", "dna.100MB", "dna.200MB"]:
            write_csv(suffix_text_file+f)

if __name__ == '__main__':
    main()
