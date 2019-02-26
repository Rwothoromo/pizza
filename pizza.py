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
rows = int(natural_numbers[0]) # no. of rows
columns = int(natural_numbers[1]) # no. of columns
min_ingredients = int(natural_numbers[2]) # min. no. of each ingredient-cells in a slice
max_cells = int(natural_numbers[3]) # max. no. of cells per slice

tomatoes = 0 # Total no. of tomatoes
mushrooms = 0 # Total no. of mushrooms
list_of_data_lists = []

for row in range(rows):
    tomatoes += data_list[row].count('T')
    mushrooms += data_list[row].count('M')

    tomato_indices = [(row, index) for index, value in enumerate(data_list[row]) if value == "T"] # positions of tomatoes
    mushroom_indices = [(row, index) for index, value in enumerate(data_list[row]) if value == "M"] # positions of mushrooms

    list_of_data_lists.append(data_list[row])


# data for output
S = int() # no. of pizza slices to cut
r1, c1, r2, c2 = int(), int(), int(), int()
# describe a slice of pizza delimited by the rows and columns (intersecting areas)


output_file.write("{}\n".format(S))
for i in range(S):
    output_file.write("{} {} {} {}\n".format(r1, c1, r2, c2))

output_file.close()
input_file.close()
