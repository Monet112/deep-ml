import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	gradient=np.asarray(gradient)
	magnitude=np.linalg.norm(gradient,2)
	direction=np.nan_to_num(np.divide(gradient,magnitude), nan=0.0, posinf=0.0, neginf=0.0)
	descent_direction=np.multiply(-1, direction)
	return {'magnitude':magnitude,'direction':direction,'descent_direction':descent_direction}