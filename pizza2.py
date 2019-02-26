import sys
import numpy as np

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')
first_line = input_file.readline()

data_list = first_line.split('\n')

# data from input
natural_numbers = data_list[0].split(' ')
rows = int(natural_numbers[0]) # no. of rows
columns = int(natural_numbers[1]) # no. of columns
min_ingredients = int(natural_numbers[2]) # min. no. of each ingredient-cells in a slice
max_cells = int(natural_numbers[3]) # max. no. of cells per slice

# pizza grid
pizza = np.empty((0, columns), str)
results = []
for i in range(rows):
    # add row to the pizza we are constructing
    pizza = np.append(pizza, np.array([list(input_file.readline().rstrip())]), axis=0)

    # reset counters on each column
    start, end, mushrooms, tomatoes = 0, 0, 0, 0

    # before reaching the end of a column, count the ingredients
    while end < columns:
        if pizza[i][end] == 'M':
            mushrooms += 1
        elif pizza[i][end] == 'T':
            tomatoes += 1
        end += 1

        # remove ingredient if slice is too big
        if end - start > max_cells:
            if pizza[i][start] == 'M':
                mushrooms -= 1
            elif pizza[i][start] == 'T':
                tomatoes -= 1
            start += 1

        # bingo! we have a slice? save it to results
        if (end - start <= max_cells) and (mushrooms >= min_ingredients) and (tomatoes >= min_ingredients):
            results.append("{} {} {} {}".format(i, start, i, end - 1)) # send in a slice (row_n, col_start, row_n, col_end) of pizza

            # reset and search for any other valid slices on this row :-)
            start = end
            tomatoes, mushrooms = 0, 0

pizza = np.reshape(pizza, (rows, columns))

# transpose such that columns are now rows
pizza_transposed = pizza.T

results1 = []
final_results = []
# iterate the columns instead of the rows
for i in range(columns):
    # reset counters on each column
    start, end, mushrooms, tomatoes = 0, 0, 0, 0

    # before reaching the end of a column, count the ingredients
    while end < rows:
        if pizza_transposed[i][end] == 'M':
            mushrooms += 1
        elif pizza_transposed[i][end] == 'T':
            tomatoes += 1
        end += 1

        # remove ingredient if slice is too big
        if end - start > max_cells:
            if pizza[i][start] == 'M':
                mushrooms -= 1
            elif pizza[i][start] == 'T':
                tomatoes -= 1
            start += 1

        # bingo! we have a slice? save it to results
        if (end - start <= max_cells) and (mushrooms >= min_ingredients) and (tomatoes >= min_ingredients):
            results1.append("{} {} {} {}".format(start, i, end, i)) # send in a slice (row_n, col_start, row_n, col_end) of pizza

            # reset and search for any other valid slices on this row :-)
            start = end
            tomatoes, mushrooms = 0, 0

# data for output
S = len(results) # no. of pizza slices to cut
results1_count = len(results1)
if results1_count > S:
    results = results1
    S = results1_count

output_file.write("{}\n".format(S))

for i in results:
    output_file.write("{}\n".format(i))

output_file.close()
input_file.close()
