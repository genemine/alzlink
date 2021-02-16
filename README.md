# 1. Description
This repository provides source codes to build the model for predicting AD-associated genes and to make predictions.


# 2. Usage
(1) After this repository is downloaded and unzipped, go into the folder. Then, make sure to unzip the **mat2pred.txt.zip** folder, which contains feature matrix of unlabeled genes to predict. <br>
(2) We have created a python script, named 'train_and_predict.py', which includes all source codes (i) to build the model for predicting AD-associated genes and (ii) to make predictions.
<br>
Assuming that you are in the folder of iREAD, just run the following command and you will be able to built a model and make predictions:
```bash
 python train_and_test.py
```
After running the script, the prediction results will be saved to the file named 'prediction.txt', in which each row contains a gene and the predicted probabilistic score ranging from 0 and 1 that measures the likelihood for the gene to be associated with AD.


# 3. Contact
  If you have any questions, please contact us:
    Cuixiang Lin, lincxcsu@csu.edu.cn <br>
    Jianxin Wang, jxwang@mail.csu.edu.cn<br>
    
