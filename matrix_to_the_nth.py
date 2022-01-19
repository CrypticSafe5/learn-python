def multiply_matrices(first, second):
	output = [
		[
			first[0][0] * second[0][0] + first[0][1] * second[1][0],  # first row by first column
			first[0][0] * second[0][1] + first[0][1] * second[1][1],  # first row by second column
		],
		[
			first[1][0] * second[0][0] + first[1][1] * second[1][0],  # second row by first column
			first[1][0] * second[0][1] + first[1][1] * second[1][1],  # second row by second column
		],
	]
	return output

"""
[
	[1, 2],
	[1, 0]
]
[
	[1, 2, 3],
	[1, 2, 3],
	[1, 2, 3]
]
"""
def multiply_matrices_procedure(matrix_one, matrix_two):
	output = []
	inverted_matrix = invert_matrix(matrix_two)
	for row_index in matrix_one: # Iterate over the rows
		for value_index in range(0, len(matrix_one[row_index])): # Iterate over the individual values
			# Multiply the iterated values by the corresponding inverted_matrix value
	return output


def invert_matrix(matrix):
	new_matrix = []
	for row in matrix:
		for position in range(0, len(row)):
			value = row[position]
			if len(new_matrix) < len(matrix[0]):
				new_matrix.append([value])
			else:
				new_matrix[position].append(value)
	return new_matrix


def calc(matrix, n):
	total = matrix
	for power_multiplier in range(1, n):
		total = multiply_matrices_procedure(total, matrix)
	return test


invert_matrix([[1, 2], [1, 0]])
