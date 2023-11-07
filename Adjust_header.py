import sys 

if __name__=="__main__":
    user_file = sys.argv[1]
    output_file = sys.argv[2]

with open(user_file, 'r') as file:
    lines = file.readlines()

modified_lines = []
for line in lines:
    if line.startswith('>'):
        modified_lines.append(line.replace('\t', ' ') or line.replace('\t', '_') or line.replace(',', ' ') or line.replace(',', '_'))
    else:
        modified_lines.append(line)

with open(output_file, 'w') as file:
    file.writelines(modified_lines)

# Why if I run this code, it gives me the error: Traceback (most recent call last):
  File "/home/acanevotti/miR_RF_TOOL/Adjust_header.py", line 4, in <module>
    user_file = sys.argv[1]
IndexError: list index out of range
