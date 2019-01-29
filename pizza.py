import sys

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')
data = input_file.read()
print("data: ", data)

data_list = data.split('\n')
print("data_list: ", data_list)

# step 1: determine which ingredient is the least in number (that's prolly the no. of slices)

# data from input
natural_numbers = data_list[0]
R = int(natural_numbers[0]) # no. of rows
C = int(natural_numbers[1]) # no. of columns
L = int(natural_numbers[2]) # min. no. of each ingredient-cells in a slice
H = int(natural_numbers[3]) # max. no. of cells per slice

tot_T = 0 # Total no. of tomatoes
tot_M = 0 # Total no. of mushrooms
list_of_data_lists = []

for i in range(R):
    tot_T += data_list[i].count('T')
    tot_M += data_list[i].count('M')

    T_indices = [(i, index) for index, value in enumerate(data_list[i]) if value == "T"] # positions of tomatoes
    M_indices = [(i, index) for index, value in enumerate(data_list[i]) if value == "M"] # positions of mushrooms

    list_of_data_lists.append(data_list[i])


# data for output
S = int() # no. of pizza slices to cut
r1, c1, r2, c2 = int(), int(), int(), int()
# describe a slice of pizza delimited by the rows and columns (intersecting areas)


output_file.write("{}\n".format(S))
for i in range(1, S+1):
    output_file.write("{} {} {} {}\n".format(r1, c1, r2, c2))

output_file.close()
input_file.close()
