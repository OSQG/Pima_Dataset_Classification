from math import sqrt

# Calculate the Euclidean distance between two vectors
def euclidean_distance(vector1, vector2):
	distance = 0.0
	for i in range(len(vector1)):
		distance += (vector1[i] - vector2[i])**2
	return sqrt(distance)

# Get k nearest neighbours
def get_neighbours(k, test_instance, training):
    distances_sorted = []
    for training_row in training:
        # Store training row and dist as a tuple to sort later
        dist = euclidean_distance(test_instance, training_row)
        distances_sorted.append((training_row, dist))
    # Sort the distances
    distances_sorted.sort(key=lambda tup: tup[1])
    # Get k nearest neigbours
    neighbours = []
    for i in range(k):
        # Get the k closet rows
        neighbours.append(distances_sorted[i][0])
    return neighbours

def KNN(k, testing, training):
    predictions = []
    for testing_row in testing:
        k_neighbours = get_neighbours(k, testing_row, training)
        yes = 0
        no = 0
        for i in k_neighbours:
            if i[-1] == "yes":
                yes = yes + 1
            elif i[-1] == "no":
                no = no + 1
        if no > yes:
            predictions.append("no")
        else:
            predictions.append("yes")
    # for i in predictions:
    #     print(i)
    return predictions