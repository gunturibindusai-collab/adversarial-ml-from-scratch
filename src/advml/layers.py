"""
Neural network layers, implemented from scratch — no autograd.

Each layer will implement:
- forward(x): compute the output given an input
- backward(grad_output): compute the gradient w.r.t. the input, and
  store gradients w.r.t. its own parameters (weights/bias)

We fill these in step by step as we derive the math for each piece.
"""


class Linear:
    """A fully-connected layer: z = Wx + b."""

    def __init__(self, in_features: int, out_features: int):
        raise NotImplementedError("We'll implement this together next.")

    def forward(self, x):
        raise NotImplementedError

    def backward(self, grad_output):
        raise NotImplementedError
