import sys
import numpy
from algorithms.KNearestNeighbour import KNN
from algorithms.NaiveBayes import NaiveBayes

if __name__ == "__main__":
    training_filename = sys.argv[1]
    testing_filename = sys.argv[2]
    classifier = sys.argv[3]

    def read_Data(filepath):
        data = []
        f = open(filepath, "r")
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n").split(",")
            for i in range(0, len(line)):
                # Convert numeric values into float
                if line[i] != "yes" and line[i] != "no":
                    line[i] = float(line[i])
            data.append(line)
        f.close()
        return data

    if classifier == "NB":
        NaiveBayes(None, None)
    elif classifier[-2:] == "NN":
        KNN(int(classifier[:-2]), read_Data(testing_filename), read_Data(training_filename))
