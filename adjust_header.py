# Read the file
file_path = 'hseq.out'
output_file = "hseq_out_prova.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()

modified_lines = []
for line in lines:
    if line.startswith('>'):
        # Replace spaces with underscores in the header line
        modified_lines.append(line.replace('\t', ' ') or line.replace('\t', '_'))
    else:
        modified_lines.append(line)

# Write the modified lines back to the file
with open(output_file, 'w') as file:
    file.writelines(modified_lines)
