## Pedigree Chart Solver - Artifical-Intelligence
###### [currently non-functional]
#### This is an artifical intelligence based solution to genetic pedigree charts. The program considers them as a constraint satisfaction problem (CSP) and solves them using search algorithms for CSPs. 
#### It takes input of pedigree charts as text files in a particular format[A file explaining the input and output formats will be added soon]. The generation of these text files can be automated with the help of image processing. 

### How to run it?
#### 1. Get inside the directory
#### 2. Locate your input in the "inputs" directory
#### 3. Enter the command as below-
> `python main.py <inputfile>`
##### Example:
> `python main.py 2.txt`
#### 4. Find your output file with same name in "outputs" output directory

 
### Function:
#### *The function of this program is to take the formatted input file, find which pattern of inheritance fits the pedigree chart and give a set of genotype values to the chart which fits in.*

### Description of directories:

#### "charts" 
##### - To store the actual pedigree chart files (image or PDF).
##### - It contains a reference chart to understand other pedigree charts.
##### - It contains a file "help.txt" which describes the set of rules to convert the pedigree chart into its text representation.

#### "inputs"
##### - To store the text representations of the charts which will act as direct input to the program.

#### "outputs"
##### - To store the output text files.

#### "safe" 
##### - To store the output files in case you don't want them to be overwritten by the program.

### Descrition of files:

#### "main.py"
##### - The main file which is to be run to run the program.

#### "problem.py"
##### - The file that stores important classes and function used in solvin ghte problem.

#### "util.py"
##### - This file stores a few important functions and data structures used for solving this problem. 
