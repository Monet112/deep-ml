import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    m, n = A.shape
    li_columns = []  # Keeps track of the independent columns found so far
    for col_idx in range(n):
        current_col = A[:, col_idx]
        if not li_columns:
            if np.linalg.norm(current_col) > tol:
                li_columns.append(current_col)
            continue
        LI_matrix = np.column_stack(li_columns)
        c, residuals, rank, s = np.linalg.lstsq(LI_matrix, current_col, rcond=None)
        projection = LI_matrix @ c
        residual_vector = current_col - projection
        if np.linalg.norm(residual_vector) > tol:
            li_columns.append(current_col)
    return len(li_columns)
