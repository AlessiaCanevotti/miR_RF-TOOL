# miR_RF-TOOL
The "miR_RF-TOOL" repository hosts a machine learning-based application designed to evaluate the authenticity of pre-microRNAs. 
Certainly! Based on the information you provided, here is a README template for your "miR_RF Tool" explaining the functionality and usage of the tool:

---

# miR_RF Tool Description

The miR_RF Tool is a predictive tool for evaluating pre-microRNAs based on machine learning. It consists of Python and R scripts designed to process RNAfold output, extract features, perform machine learning analysis, and generate predictions.

### Overview

The miR_RF Tool is comprised of Python and R scripts:
- **Python Script (Preprocessing):**
  - Extracts features from pre-miRNAs present in RNAfold output files.
  - Converts extracted features into numerical format and produces an intermediate file for R processing.
  - Input: RNAfold output file.
  - Output: Intermediate file with extracted features.
- **R Script (Machine Learning):**
  - Performs machine learning analysis on the intermediate file generated by the Python script.
  - Generates a text file containing predictions for each pre-miRNA in the input.
  - Input: Intermediate file generated by the Python script.
  - Output: Text file with predictions (2 for YES, 1 for NO) for each pre-miRNA.

### Input Requirements
The tool accepts RNAfold output files as input, structured in the following format:
- A file with a header line starting with ">" followed by five subsequent lines for each pre-miRNA. 
For every input string, made by the header line followed by the sequence, the output is composed by four lines corresponding to respectively:
1. MFE structure, reported within round brackets;
2. Ensemble structure, with energy reported in square brackets;
3. Centroid structure, with its energy and the minimal base-pair distance to all the structures in
the thermodynamic ensemble, reported in curly brackets.
4. Frequency of MFE structure in ensemble and ensemble diversity
   
- Multi-FASTA format is also supported.

### Prerequisites

1. Conda
2. Python
3. R

### Input Example

Sample input file structure:

```plaintext
>hsa-let-7a-1 MI0000060 Homo sapiens let-7a-1 stem-loop
UGGGAUGAGGUAGUAGGUUGUAUAGUUUUAGGGUCACACCCACCACUGGGAGAUAACUAUACAAUCUACUGUCUUUCCUA
(((((.(((((((((((((((((((((.....(((...((((....)))).))))))))))))))))))))))))))))) (-34.20)
{((((.(((((((((((((((((((((.....(((...((({....}))).))))))))))))))))))))))))))))} [-35.18]
(((((.(((((((((((((((((((((.....(((...((((....)))).))))))))))))))))))))))))))))) {-34.20 d=3.42}
 frequency of mfe structure in ensemble 0.203686; ensemble diversity 5.63
...
```

### Output Example

The output file contains pre-miRNA names and their corresponding predictions:

```plaintext
"miRNA name"                                               "prediction"
">hsa-let-7a-1 MI0000060 Homo sapiens let-7a-1 stem-loop"       "2"
```

### Installation

1. Conda installation in command line (use the provided CONDA installation instructions file)
2. Activating the Conda environment --> once Conda is installed, use the provided `configuration_file.yml` file to create an environment suitable for running the miR_RF Tool. In the command line, navigate to the directory containing the `configuration_file.yml` file and type the following command:

   ```bash
   conda env create -f configuration_file.yml
   Note: Creating the environment may take some time, as Conda downloads and installs the necessary packages and dependencies.

   After the environment is created, activate it by using the following command:

   ```bash
   conda activate miR_RF


