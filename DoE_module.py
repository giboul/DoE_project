from itertools import combinations
import numpy as np
import pandas as pd
from formulaic import model_matrix
from scipy.linalg import hadamard
from scipy.stats import ttest_ind, t


def linear_spec(nx):
    return np.eye(nx)


def pure_interact_spec(nx):
    i1, i2 = np.array(list(combinations(range(nx), 2))).T
    cols = np.arange(nx)
    spec = np.zeros(i1.size, nx)
    spec[cols, i1] = 1
    spec[cols, i2] = 1
    return spec

def interact_spec(nx):
    return np.vstack((linear_spec(nx), pure_interact_spec(nx)))


default_spec_models = {
    k[:-5]: globals()[k]
    for k in globals()
    if k[-5:]=="_spec"
}


def x2fx(spec: str | np.ndarray, E: np.ndarray, cols_fmt="x%i"):

    nE, nx = E.shape

    if isinstance(spec, str):  # Either named scheme or Wilkinson notation
        if spec in default_spec_models:  # linear / interact / pure_intercat ...
            spec = default_spec_models[spec](nx)
        else:  # Use Wilkinson notation with the formulaic package
            if isinstance(E, np.ndarray):
                # Make a DataFrame from the experiment matrix
                # Default column names are (x1 x2 x3 x4 ...)
                factors = [cols_fmt % i for i in range(1, nx+1)]
                E = pd.DataFrame(E, columns=factors)
            elif not isinstance(E, pd.DataFrame):
                raise ValueError(
                    "With a string for `spec`, "
                    "provide an array or a DataFrame for `E`"
                )
            return model_matrix(spec, E)

    # spec in an ArrayLike, compute the model matrix directly
    na, nx = spec.shape
    E = np.array(E)
    spec = np.array(spec)
    return np.prod(E[:, :, None] ** spec.T[None, :, :], axis=1)


def standardize(E, transpose=False):
    axis = 1 if transpose else 0
    Emax = E.max(axis=axis)
    Emin = E.min(axis=axis)
    if (Emax == Emin).any():
        raise ValueError(f"Max == Min ({np.nonzero(Emin==Emax)[0]})")
    return 2*(E-Emin)/(Emax-Emin)-1


def dispersion(X):
    return np.linalg.inv(X.T @ X)


def corrcov(D):
    return D / np.sqrt(np.outer(np.diag(D), np.diag(D)))


def main():
    spec = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 0]
    ])
    E = np.array([
        [-1, -1, -1],
        [-1, -1,  0],
        [-1, -1,  1],
        [-1,  1,  0],
        [ 0,  0,  0],
        [ 1, -1,  0],
        [ 1,  1, -1],
        [ 1,  1,  0],
        [ 1,  1,  1]
    ])
    print(x2fx(spec, E))
    print(x2fx("linear", E))

if __name__ == "__main__":
    main()
