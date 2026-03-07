import numpy as np
import pandas as pd
from scipy.linalg import hadamard
from formulaic import model_matrix
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_theme()


E = pd.DataFrame(hadamard(8)[:, 1:5], columns=["Fr", "s", "c", "o"])
sns.heatmap(E, annot=True, cmap="coolwarm")
plt.show()
E.to_csv("matrix_experiment.csv", index=False)

M = model_matrix("Fr+s+c+o + Fr:s + Fr:c + Fr:o + s:c + s:o + c:o", E)
plt.figure(layout="tight")
sns.heatmap(M, annot=True, cmap="coolwarm")
plt.show()
E.to_csv("matirx_model.csv", index=False)