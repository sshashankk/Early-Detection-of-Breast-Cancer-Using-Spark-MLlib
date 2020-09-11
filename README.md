# Early-Detection-of-Breast-Cancer-Using-Spark-MLlib-and-its-Analysis

### Abstract

Breast cancer is causing widespread deaths and is one of the most common causes of cancers
encountered around the world. These deaths can be reduced by early detection of cancerous
cells. Unfortunately, not all physicians are experts in distinguishing between the benign and
malignant tumors and the classification of tumor cells may take up to two days.
We used the distributed computation framework of Hadoop - Apache Spark for quicker
analytics and faster model generations to aid in early detection of breast cancer. 

The analytic deals with the diagnosis of breast cancer by analyzing survey images of breast cancer cells and
raw text data consisting of characteristics of the cell nuclei present in the image to classify if the tumor cell being observed is benign or malignant.

#Project Title:
Early Detection of Breast Cancer Using Spark MLlib and its Analysis

### Configuration: 
Python 2.7.13
Spark 1.6.0
Databricks csv package
Pandas
Pyspark-SQL
Pyspark-ml

### Directory Structure and files

1. Make directory in HDFS
   hdfs dfs -mkdir /user/user/<user_id>/project

2. Put the data set in HDFS
   hdfs dfs -put /user/<user_id>/project/breast-cancer-wisconsin.data.csv

3. Verfify the files
   hdfs dfs -ls /user/<user_id>/project/

### Building and executing the code

1. Start pyspark by typing the following cmd:

   pyspark --packages com.databricks:spark-csv_2.10:1.4.0 

2. Due to the limitation of creating a new SparkContext from my ID and creating my own context to run the python file
   We are limited to using the interactive mode of pyspark to execute the lines of code
   Using spark-submit to execute throws an error saying SparkContext is not defined as we explicitly cannot create a new SparkContext
   
3. The lines of code to be executed via the Pyspark Interactive mode(line by line) is contained in the Breast_Cancer_Classifier_Main.py file.

4. The output of this execution(on terminal) is a list of predictions that have been made by the ML model with respect to a Malign(1) cell or Bening(0) cell.

### Results

1. The classification goal is to predict whether the cell is Cancerous or not (Malignant/Benign)

2. Start pyspark by typing the following cmd:

   pyspark --packages com.databricks:spark-csv_2.10:1.4.0 

3. The lines of code to derive the result of the analytic ie. the accuracy of the ML model's prediction is to execute the lines of code
   contained in the Breast_Cancer_Classifier_Estimator.py file via the Pyspark Interactive mode(line by line).
   
4. The output of this execution will be visible on the terminal


