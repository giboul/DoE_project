import itertools
import numpy as np
from formulaic import model_matrix


def factorial_design(order: int, num_levels: int=2) -> np.ndarray:
    levels = np.linspace(-1, 1, num_levels)
    r = np.arange(num_levels**order)[:, None]
    powers = num_levels**np.arange(order)[::-1]
    digits = (r // powers) % num_levels
    return levels[digits]


def standardize(E: np.ndarray, transpose: bool=False) -> np.ndarray:
    axis = 1 if transpose else 0
    Emax = E.max(axis=axis)
    Emin = E.min(axis=axis)
    if (Emax == Emin).any():
        raise ValueError(f"Max == Min ({np.nonzero(Emin==Emax)[0]})")
    return 2*(E-Emin)/(Emax-Emin)-1


def dispersion(X: np.ndarray) -> np.ndarray:
    return np.linalg.inv(X.T @ X)


def corrcov(D: np.ndarray) -> np.ndarray:
    return D / np.sqrt(np.outer(np.diag(D), np.diag(D)))


def vif(C: np.ndarray) -> np.ndarray:
    return np.diag(np.linalg.inv(C))


def simplex_sampling(q: int, m :int) -> np.ndarray:
    idx = np.arange(m+q-1)
    combs = np.array(list(itertools.combinations(idx, q-1)))
    parts = np.diff(
        np.hstack([
            -1*np.ones((len(combs),1)),
            combs,
            (m+q-1)*np.ones((len(combs),1))
        ]),
        axis=1
    ) - 1
    return (parts / m)[::-1]
