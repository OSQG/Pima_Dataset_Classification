import csv




'''
The way that the probability of the different values contributes to what class they 
are is as follows : 
The P(A|B) = probability of A given B
Therefore, for each row of data :  
P(yes|attribute_i=value_i for each attribute) = 
    [P(yes)P(attribute_1=value_1|yes)P(attribute_2=value_2|yes)....]/P(attributes)
P(no|attribute_i=value_i for each attribute) = 
    [P(no)P(attribute_1=value_1|no)P(attribute_2=value+2|no)....]/P(attributes)
The ratio of yes to no given the attributes in the row = 
    [P(yes)P(attribute_1=value_1|yes)P(attribute_2=value_2|yes)....]/[P(no)P(attribute_1=value_1|no)P(attribute_2=value_2|no)....]
The individual P(attribute_i=value_i|class) is calculated by going through the data and calculating
how often these values appear for each given class 
'''
def NaiveBayes(testing, training):
    with open('pima.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        i=0
        for row in csvReader:
            while i<100:
                print(row)
                i+=1
    return