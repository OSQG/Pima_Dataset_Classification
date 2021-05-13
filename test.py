z= [['hey','delete this'],['hey','del']]
validation_instances = []
for i in range(len(z)):
    validation_instances.append([])
    for j in range(len(z[i])):
        validation_instances[i].append(j)
for row in validation_instances:
    del row[-1]
print(z) # yup this cts out the old stuff too
# print(validation_instances)
a = z.clone()
for i in a:
    del i[-1]
print(z)