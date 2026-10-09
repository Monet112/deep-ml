import torch

def train_logreg(X: torch.Tensor, y: torch.Tensor, learning_rate: float, iterations: int) -> tuple[list[float], list[float]]:
    """
    Train logistic regression using gradient descent with BCE loss.
    
    Args:
        X: Feature matrix of shape (n_samples, n_features) as Tensor
        y: Binary labels of shape (n_samples,) as Tensor
        learning_rate: Step size for gradient descent
        iterations: Number of training iterations
    
    Returns:
        Tuple of (coefficients, losses) where:
        - coefficients: List of learned weights (bias first, then feature weights), rounded to 4 decimals
        - losses: List of BCE loss values at each iteration, rounded to 4 decimals
    
    Notes:
        - Initialize all coefficients to zero
        - Add bias column as FIRST column of X
        - Use sum-based BCE loss: -sum(y*log(p) + (1-y)*log(1-p))
    """
    coeffs = torch.zeros(X.shape[1]+ 1, requires_grad=True)
    losses = []
    ones = torch.ones(X.shape[0], 1)
    X_with_bias = torch.cat((ones, X), dim=1)
    for i in range(iterations):
        logits = X_with_bias @ coeffs
        p = torch.sigmoid(logits)
        eps = 1e-15
        loss = -torch.sum(y * torch.log(p + eps) + (1 - y) * torch.log(1 - p + eps))
        losses.append(round(loss.item(), 4))
        loss.backward()
        with torch.no_grad():
            coeffs -= learning_rate * coeffs.grad
            coeffs.grad.zero_()
    coeffs = [round(c, 4) for c in coeffs.tolist()]

    return (coeffs, losses)