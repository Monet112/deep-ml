def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	determinant = 0
	if len(matrix)==1:
		return (matrix[0][0],matrix[0][0])
	elif len(matrix)==2:
		return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0],matrix[0][0]+matrix[1][1])
	else:
		for col in range(len(matrix)):
			sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
			sign = 1 if col % 2 == 0 else -1
			determinant += sign * matrix[0][col] * matrix_determinant_and_trace(sub_matrix)[0]
		trace=sum(matrix[i][i] for i in range(len(matrix)))
		return (determinant, trace)