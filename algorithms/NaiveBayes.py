import csv
import math

def average(attribute):
    sum=0.0
    for i in range(len(attribute)):
        sum = sum + attribute[i]
    ave = sum/len(attribute)
    return ave

def stdev(attribute):
    sum=0
    for i in range(len(attribute)):
        sum = sum + attribute[i]
    ave = sum/len(attribute)
    # print("average is "+str(ave))
    squared = 0
    for i in range(len(attribute)):
        squared+=(attribute[i]-ave)**2
    result = ((squared)/len(attribute))**0.5
    # print("standard deviation is "+str(result))
    return result

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
    results = []
    yes=[]
    no=[]
    att_yes=[]
    att_no=[]

    # data in training is looks like this [[0.22, 0.11, ... , "yes"] , ... , [0.23, 0.2, ..., "no"]] 
    for row in training:
        # If the last attribute for each row is yes then append the yes row to yes and the attributes only to att_yes
        if row[-1] == "yes":
            yes.append(row[-1])
            # Takes everything expect last attribute which is the class yes or no
            att_yes.append(row[:-1])
        # Same but for no
        elif row[-1] == "no":
            no.append(row[-1])
            att_no.append(row[:-1])
    
    p_yes=len(yes)/(len(yes)+len(no))
    p_no=len(no)/(len(yes)+len(no))

    # data in training is looks like this [[0.22, 0.11, ... , 0.54] , ... , [0.23, 0.2, ..., 0.67]] 
    for row in testing:
        y=[]
        n=[]
        for i in range(len(row)): #each attribute
            if i < len(att_yes):
                first = 1/(stdev(att_yes[i])*(2*math.pi)**1/2)
                power_numerator = (float(row[i])-average(att_yes[i]))**2
                power_denominator = 2 * (stdev(att_yes[i]))**2
                power = -power_numerator/power_denominator
                probability = first*math.e**power
                y.append(probability)
            
            if i < len(att_no):          
                first = 1/(stdev(att_no[i])*(2*math.pi)**1/2)
                power_numerator = (float(row[i])-average(att_no[i]))**2
                power_denominator = 2 * (stdev(att_no[i]))**2
                power = -power_numerator/power_denominator
                probability = first*math.e**power
                n.append(probability)

        # Now that all the probabilities have been calculated for the different attributes in this row,
        test_p_yes = p_yes
        test_p_no = p_no
        for i in range(0,len(y)): # each attribute
            test_p_yes = test_p_yes * y[i]
        for i in range(0, len(n)):
            test_p_no = test_p_no * n[i]
        ratio = test_p_yes/test_p_no
        if ratio < 1:
            results.append("no")
        else:
            results.append("yes")
    return results
