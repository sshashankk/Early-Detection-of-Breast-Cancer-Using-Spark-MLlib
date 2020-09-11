from itertools import combinations
#Data Exploration and Importing the dataset from HDFS
from pyspark.sql import SQLContext
from pyspark.ml.evaluation import BinaryClassificationEvaluator

from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from itertools import combinations



sqlContext = SQLContext(sc)
df = sqlContext.load(source="com.databricks.spark.csv", header = 'true', inferSchema = 'true', path = '/user/srl506/project/breast-cancer-wisconsin.data.csv')

df_origional = df

#Encoding and assemblying process includes Indexing,feature transforming for merging multiple columns into a vector column.

#data = ['radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean','compactness_mean','concavity_mean']
data = ['radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean','compactness_mean','concavity_mean','concave points_mean','symmetry_mean','fractal_dimension_mean','radius_se','texture_se','perimeter_se','area_se','smoothness_se','compactness_se','concavity_se','concave points_se','symmetry_se','fractal_dimension_se','radius_worst','texture_worst','perimeter_worst','area_worst','smoothness_worst','compactness_worst','concavity_worst','concave points_worst','symmetry_worst','fractal_dimension_worst']


input  = ['radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean','compactness_mean','concavity_mean','concave points_mean','symmetry_mean','fractal_dimension_mean','radius_se','texture_se','perimeter_se','area_se','smoothness_se','compactness_se','concavity_se','concave points_se','symmetry_se','fractal_dimension_se','radius_worst','texture_worst','perimeter_worst','area_worst','smoothness_worst','compactness_worst','concavity_worst','concave points_worst','symmetry_worst','fractal_dimension_worst']

 
for r in range (1, len(input)+1):
    list1 = list(combinations(input,r))
    with open("/scratch/srl506/file.txt", "a") as f:
        for col in list1:
            df = df_origional
            stages = []
            label_stringIdx = StringIndexer(inputCol = 'diagnosis', outputCol = 'label')
            stages += [label_stringIdx]
            assemblerInputs =  col
            assembler = VectorAssembler(inputCols=assemblerInputs, outputCol='features')
            stages += [assembler]
            #Pipeline to chain multiple Transformers and Estimators together to specify our machine learning workflow
            pipeline = Pipeline(stages = stages)
            pipelineModel = pipeline.fit(df)
            df = pipelineModel.transform(df)
            selectedCols = ['label', 'features']
            df = df.select(selectedCols)

            #Randomly split data into train and test sets, and set seed for reproducibility
            train, test = df.randomSplit([0.8, 0.2], seed = 4)


            #Applying the Machine Learning Algorithm on the training dataset
            lr = LogisticRegression(featuresCol = 'features', labelCol = 'label', maxIter=10)
            lrModel = lr.fit(train)

            #Performing predictions w.r.t the test dataset
            predictions = lrModel.transform(test)
            # Evaluating the accuracy of the Analytic using LogisticRegression model

            evaluator = BinaryClassificationEvaluator()
            print("Accuracy =",evaluator.evaluate(predictions), " for columns ",col)
            if (float(evaluator.evaluate(predictions)) > 0.999):
                print("Writing to a file")
                f.write("Accuracy ="+ str(evaluator.evaluate(predictions))+ " for columns "+str(col)+"\n")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        