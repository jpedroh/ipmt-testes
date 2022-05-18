import subprocess, sys, os

def main():
    pattern_file = sys.argv[1]
    text_file = sys.argv[2]
    
    idx = text_file.rindex(".")
    text_file_indexed = text_file[:idx]+'.idx'
    if not os.path.exists(text_file_indexed):
        ipmt_index = "./utils/ipmt index " + text_file
        subprocess.run(ipmt_index, capture_output=True, text=True, shell=True)
    
    with open(pattern_file, 'r') as f:
        lines = f.readlines()
        errors = []
        for line in lines:
            line = line.replace('\n', "")
            if "*" not in line:
                grep = "grep -o \'" + line + "\' " + text_file + " | wc -l"
                p = subprocess.run(grep, capture_output=True, text=True, shell=True)
                ipmt = "./utils/ipmt search " + " -c \'" + line + "\' " + text_file_indexed
                p1 = subprocess.run(ipmt, capture_output=True, text=True, shell=True)
                if p.stdout != p1.stdout:
                    errors.append([line, p.stdout.replace('\n', ''), p1.stdout.replace('\n', '')])
    
    if len(errors) == 0:
        print("Nenhum erro de corretude foi encontrado")
    else:
        print("Os seguintes erros foram achados:")
        for error in errors:
            print("No seguinte padrão", error[0], "produziu", error[2], "quando o esperado era", error[1])

if __name__ == '__main__':
    main()