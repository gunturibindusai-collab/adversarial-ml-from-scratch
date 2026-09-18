# Adversarial ML From Scratch

A neural network, adversarial attacks (FGSM, PGD), and an adversarial-training
defense — all implemented from the underlying math, without a deep learning
framework doing the learning or attack computation for you.

## Why this exists

Most beginner ML portfolio projects call `model.fit()` and stop there. This
project goes the other way: every gradient, every attack, every defense is
derived and coded by hand, so the README and the code can actually explain
*why* it works, not just *that* it works.

## Project structure

```
adversarial-ml-from-scratch/
├── src/advml/        # the actual library code
│   ├── layers.py     # Linear layer: forward + backward, from scratch
│   ├── network.py    # stitches layers into a full network
│   └── attacks.py    # FGSM / PGD, implemented from the gradient math
├── tests/            # pytest tests — written alongside, not after
├── requirements.txt  # runtime dependencies
├── Makefile          # setup / test / lint shortcuts
└── pyproject.toml    # packaging config (so `advml` is importable)
```

## Setup

```
make setup
```

## Run tests

```
make test
```

## Roadmap

- [ ] `Linear` layer forward + backward pass (NumPy)
- [ ] Full network + training loop on MNIST
- [ ] Baseline clean-accuracy benchmark
- [ ] FGSM attack from scratch
- [ ] PGD attack from scratch
- [ ] Adversarial training defense
- [ ] Evaluation, plots, and write-up
