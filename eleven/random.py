import os
import torch
import random

import numpy as np

from dataclasses import dataclass
from contextlib import contextmanager


@dataclass
class Seeds:
    pythonhash: int = 0
    pythonrand: int = 0
    numpy: int = 0
    torch: int = 0


class SeedControl:
    r"""Manage random seeds"""

    def __init__(self, seeds=Seeds()):
        self.s = seeds

    def update_all_seeds(self, seed: int):
        """Fix all seeds to the same seed"""
        self.s = Seeds(
            pythonhash=seed,
            pythonrand=seed,
            numpy=seed,
            torch=seed
        )

        self.set_seeds()

    def set_seeds(self):
        """Set the random seeds in the environement"""
        os.environ['PYTHONHASHSEED'] = str(self.s.pythonhash)
        random.seed(self.s.pythonrand)
        np.random.seed(self.s.numpy)
        torch.manual_seed(self.s.torch)

    def get_seeds(self):
        return {
            'PythonHash': self.s.pythonhash,
            'PythonRand': self.s.pythonrand,
            'Numpy': self.s.numpy,
            'Torch': self.s.torch
        }


@contextmanager
def random_seeds(seeds: Seeds=Seeds()):
    """Set random seeds"""
    seed_control = SeedControl(seeds)
    seed_control.set_seeds()
    yield seed_control

