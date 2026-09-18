"""
Tests for the from-scratch layers.

Notice this test is written BEFORE Linear is implemented. That's on
purpose — this is test-driven development. Right now this test FAILS
(red). Once we implement Linear.forward in layers.py, it turns green.
"""
import numpy as np

from advml.layers import Linear


def test_linear_forward_shape():
    layer = Linear(in_features=2, out_features=3)
    x = np.array([0.5, 0.8])
    z = layer.forward(x)
    assert z.shape == (3,)
