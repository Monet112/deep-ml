
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	dot=sum([v_i*L[i] for i,v_i in enumerate(v)])
	mag_sq=sum([L_i**2 for L_i in L])
	return [(dot/mag_sq)*L_i for L_i in L]
