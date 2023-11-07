# miR_RF-TOOL
The "miR_RF-TOOL" repository hosts a machine learning-based application designed to evaluate the authenticity of pre-microRNAs. 

---

# miR_RF Tool Description

The miR_RF Tool is a predictive tool for evaluating pre-microRNAs based on the machine learning algorithm Random Forest. It consists of Python and R scripts designed to process RNAfold Vienna output, extract features, perform machine learning analysis and generate predictions.

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
- The miR_RF Tool accommodates a range of input file formats. Whether it's a .txt, .out, or another format, the tool is engineered to process pre-miRNA data effectively, irrespective of the file extension. Feel free to use the format that best suits your data.
- Note: the header cannot contain spaces ("\t"). If you need to insert other info regarding the header, use "_" for connecting words or numbers.
  For example:
  >hsa-let-7a-1_first_example_1

### Input Example

Sample input file structure:

```plaintext
>hsa-let-7a-1
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
"miRNA name"       "prediction"
">hsa-let-7a-1"       "2"
```

### Installation

Before beginning the installation, I recommend creating a new directory to neatly store all the requirements for the miR_RF Tool. This will facilitate a clearer and more organized environment for running the tool efficiently. 
To create a new directory, for example named "miR_RF_Tool", in your current location, use the following command in the terminal:

```bash
mkdir miR_RF_tool
```
This command will create a new directory named "miR_RF_Tool" within the current location. Users can then move the necessary files here. 

1. Conda Installation in Command Line:
   - Follow the provided instructions in the 'CONDA installation instructions' file to install Conda on your system in the directory just created.

2. Activating the Conda environment:
   - Once Conda is installed, use the provided `configuration_file.yml` file to create an environment suitable for running the miR_RF Tool.
   Download the `configuration_file.yml` file and copy it in the new directory, as follows:

   ```bash
   cp configuration_file.yml ~/miR_RF_tool
   ```
   - In the command line, activate conda with the following command:

   ```bash
   conda activate
   ``` 
   
   - Remain in the directory containing the `configuration_file.yml` file and clone the following command:

   ```bash
   conda env create -f configuration_file.yml
   ```
   Note: Creating the environment may take some time, as Conda downloads and installs the necessary packages and dependencies.

   - After the project environment is created, activate it by using the following command:

   ```bash
   conda activate miR_RF
   ```
   This step ensures that the appropriate environment, complete with all the necessary channels and packages required to run the miR_RF Tool, is activated. The 
   configuration_file.yml contains a specific set of channel configurations and package installations essential for the execution of the tool.
   By following these steps, you will have the correct environment with pre-configured channels and packages, ready to utilize the miR_RF Tool efficiently.

2. Setting up the directory:
   - Add in the same directory where it is present the `configuration_file.yml` and ".sh" files, the provided following files:
      - `df_feat_ext.py`: Python script for feature extraction from pre-miRNAs;
      - `make_pred.R`: R script for making predictions using machine learning;
      - `trained_model.RDS`: Includes the pre-trained model data necessary for predictions;
      - `application.py`: Executor program coordinating the feature extraction and prediction processes

   Note: make sure that `configuration_file.yml`, `trained_model.RDS`, `df_feat_ext.py`, `make_pred.R` and `application.py` are located in the same directory. In 
   order to check, use the ls command along with the file names. For example:

   ```bash
   ~/miR_RF_tool$ ls
   Anaconda3-2023.09-0-Linux-x86_64.sh configuration_file.yml trained_model.RDS df_feat_ext.py make_pred.R application.py
   ```
   If any file is missing, the command will not display it in the directory listing. Therefore, add it.

   Alternatively, you can download all repository files: 
   To simplify the process of obtaining all the required files for the miR_RF Tool, a ZIP archive containing the complete repository content is available for 
   download. Follow the steps below to access the archive:
   - Access the Repository on GitHub;
   - Click on "Code" Dropdown;
   - Select "Download ZIP";
   - After downloading the ZIP file, extract its contents and place them in a directory of your choice. This consolidated archive provides all the essential 
   files required to run the miR_RF Tool seamlessly.


4. Running the miR_RF Tool:
   - To utilize the miR_RF Tool for predicting pre-miRNAs, use the following command in the terminal or command line interface:

   ```bash
   python3 application.py input_file output_file
   ```

   Replace input_file with the name of the file containing pre-miRNA data in the required format. Similarly, replace output_file with the desired name for the 
   prediction results file.

   Example Usage:

   ```bash
   python3 application.py miRNA_sequences.txt predictions.txt
   ```
   miRNA_sequences.txt: Example input file containing pre-miRNA data.
   predictions_output.txt: Output file to store the prediction results.

   Ensure that the input file follows the specified format (see Input requirements). Upon executing this command, the `application.py` program will 
   process the input data, execute feature extraction, and generate predictions using the trained model.

5. Example input file:
   
   Use the provided file, called "miRNA_sequences.txt", if needed, in order to obtain and run an input example. 
