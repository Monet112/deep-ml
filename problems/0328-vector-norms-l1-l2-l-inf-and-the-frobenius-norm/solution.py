import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    arr=np.asarray(arr,dtype=float)
    match norm_type:
        case 'l1':
            return np.add.reduce(np.abs(arr.flatten()))
        case 'l2':
            return np.sqrt(np.add.reduce(arr.flatten()**2))
        case 'linf':
            return np.abs(arr).max()
        case 'frobenius':
            if arr.ndim==2:
                return np.linalg.norm(arr,'fro')
            else:
                raise ValueError
           


    pass
