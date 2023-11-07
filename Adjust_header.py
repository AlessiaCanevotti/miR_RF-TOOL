import sys 

if __name__=="__main__":
    user_file = sys.argv[1]
    output_file = sys.argv[2]

with open(user_file, 'r') as file:
    lines = file.readlines()

modified_lines = []
for line in lines:
    if line.startswith('>'):
        modified_lines.append(line.replace('\t', ' ') or line.replace('\t', '_'))
    else:
        modified_lines.append(line)

with open(output_file, 'w') as file:
    file.writelines(modified_lines)
