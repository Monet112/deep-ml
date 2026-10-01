def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	for row in matrix:
		for i,element in enumerate(row):
			row[i]=scalar*element
	return matrix