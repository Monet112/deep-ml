def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode=='row':
		means=[sum(row)/len(row) for row in matrix]
	elif mode=='column':
		means=[sum([row[i]for row in matrix])/len(matrix)  for i in range(len(matrix[0]))]	
	return means