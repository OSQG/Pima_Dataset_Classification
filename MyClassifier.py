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
        for i in lines:
            data.append(i.strip("\n").split(","))
        return data

    if classifier == "NB":
        NaiveBayes(None, None)
    elif classifier[-2:] == "NN":
        KNN(classifier[:-2], read_Data(testing_filename), read_Data(training_filename))
