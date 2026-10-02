def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	expected_value=sum([i/n for i in range (1,n+1)])
	variance=sum([(i-expected_value)**2/n for i in range (1,n+1)])
	return (expected_value,variance)