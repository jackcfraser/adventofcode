import random

print("Advent of code day 1!")

# values in arrays
#amount = 10

# generate some data
#num_range = range(10)
#left_array = [random.choice(num_range) for _ in range(amount)]
#right_array = [random.choice(num_range) for _ in range(amount)]

left_array = []
right_array = []

line_count = 0

with open("1.txt") as file:
    for line in file:
        line_count+=1
        arr = line.split()
        left_array.append(int(arr[0]))
        right_array.append(int(arr[1]))



# sorting arrays should pair them up in the right order
left_array_sorted = sorted(left_array)
right_array_sorted = sorted(right_array)

#print("Ordered | Unordered")
#print(f"{left_array} | {left_array_sorted}")
#print(f"{right_array} | {right_array_sorted}")


# by storing in an array, we can retrieve the distance for each pair at a later point.
dist_array = []
similarity_array = []

for i in range(line_count):
    num_occurences = right_array_sorted.count(left_array_sorted[i])
    similarity_array.append(left_array_sorted[i] * num_occurences)

    dist = abs(left_array_sorted[i] - right_array_sorted[i])
    dist_array.append(dist)

print(f"Total distance is {sum(dist_array)}")
print(f"Total similarity score is {sum(similarity_array)}")

