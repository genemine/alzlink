# 1. Description
This repository provides source codes to build the model for predicting AD-associated genes and to make predictions. The model is built using ExtraTree. The feature vectors of training and test genes are extracted from the brain gene network in the BaiHui database, which is available at https://github.com/genemine/BaiHui.


# 2. Usage
(1) After this repository is downloaded and unzipped, go into the folder. Then, make sure to unzip the **mat2pred.txt.zip** folder, which contains feature matrix of unlabeled genes to predict. <br><br>

(2) We have created a python script, named 'train_and_predict.py', which includes all source codes (i) to build the model for predicting AD-associated genes and (ii) to make predictions.
<br>
Assuming that you are currently in the downloaded folder, just run the following command and you will be able to built a model and make predictions:
```bash
 python train_and_test.py
```
**Note**: The three modules, which are **pandas, numpy and sklearn**, need to be installed before running the script.<br>

(3) After running the script, the prediction results will be saved to the file named 'prediction.txt', in which each row contains a gene and the predicted probabilistic score ranging from 0 and 1 that measures the likelihood for the gene to be associated with AD.


# 3. Contact
  If you have any questions, please contact us:<br>
    Cuixiang Lin, lincxcsu@csu.edu.cn <br>
    Jianxin Wang, jxwang@mail.csu.edu.cn<br>
    
