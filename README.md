# 1. Description
This repository provides source codes to build the model to predict AD-associated genes.


# 2. Usage
(1) After this repository is downloaded, make sure to unzip the **mat2pred.txt.zip** folder, which contains feature matrix of unlabeled genes to predict. <br>
(2) We have created a python script, named 'train_and_predict.py', which includes all source codes to build 



Using iREAD is very simple. Only one command needs to be issued form command line, and you would be able to identify IR events from RNA-seq data. For illustration purpose, we have included a test BAM file and a intron coordinate text file along with the iREAD package for testing the package. After you unzip the source package, you should see two folders inside: one is **data** containing test data, the other is **meta** containing text files of intron coordinates for mouse (Ensembl ver75) and human(Ensembl ver77), respectively.
<br><br>
To run the iREAD for IR detection, assuming that you are in the folder of iREAD, just issue the following command from shell:
```bash
 python demo.py
```



AD gene prediction
  (unzip a zip file in data file first)

1. Building models for AD gene prediction
Note 1: In the first line of the BASH, PERL and Python scripts in ADGenePred, the path for BASH, PERL and Python is set as follows by default:

    python demo.py

2. Contact
  If you have any questions, please contact at:

    Cuixiang Lin, lincxcsu@csu.edu.cn
    
