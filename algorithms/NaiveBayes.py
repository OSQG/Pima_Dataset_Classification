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
# preg = 0
# plasma=1
# bp=2
# thickness=3
# serum=4
# bmi=5
# pedigree=6
# age=7
def NaiveBayes(testing, training):
    yes=[]
    no=[]
    att_yes=[]
    att_no=[]
    for i in range(0,8):
        att_no.append([])
        att_yes.append([])
    with open('fakepima.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        i=0
        for row in csvReader:
            if row[8]=="yes":
                yes.append(row[8])
                for j in range(0,8):
                    att_yes[j].append(float(row[j]))
            else:
                for j in range(0,8):
                    att_no[j].append(float(row[j]))
                no.append(row[8])
    p_yes=len(yes)/(len(yes)+len(no))
    p_no=len(no)/(len(yes)+len(no))
    # print("att_yes")
    # print(att_yes)
    # print("stdev")
    # print(stdev(att_yes[0]))
    with open('test.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            # print("row")
            # print(row)
            y=[]
            n=[]
            for i in range(0,len(row)): #each attribute
                # print(i)

                first = 1/(stdev(att_yes[i])*(2*math.pi)**1/2)
                power_numerator = (float(row[i])-average(att_yes[i]))**2
                power_denominator = 2 * (stdev(att_yes[i]))**2
                power = -power_numerator/power_denominator
                probability = first*math.e**power
                y.append(probability)

                # print(att_no[i])
                # print(stdev(att_no[i]))
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
                test_p_no = test_p_no * n[i]
            # print(test_p_yes)
            # print(test_p_no)
            ratio = test_p_yes/test_p_no
            #print(ratio)
            if ratio>1:
                print("yes")
            else:
                print("no")
    return
