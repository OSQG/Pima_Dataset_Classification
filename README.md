<p align="center">  
   <h1 align="center">Pima Classification</h1>
</p>

Aims:mag_right:
-----
- Implementing  the  K-Nearest  Neighbour  and  Naïve  Bayes  algorithms  and  evaluating them on the pima dataset using the stratified cross validation method. 

- Evaluating the performance of  other  classifiers  on  the  same  dataset  using  Weka. 

- Investigating  the  effect  of  feature selection, in particular the Correlation-based Feature Selection method (CFS) from Weka.

Input and Output
----------------
To run the program:
`python MyClassifier.py <training> <testing.csv> <classifier>`

- The `<classifier>` specifies either Naive Bayes as `NB` or `kNN` for Nearest Neighbour, where `k` is replaced with a number.

- The `training.csv` and `testing.csv` can be replaced with any datasets that you provide.

To run an example using the Pima and Testing sets provided:
`python MyClassifier.py pima.csv testing.csv 5NN`
