import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_theme()

R = np.loadtxt("hmax.csv", delimiter=",").T
P_lin = np.loadtxt("out.txt")
P_log = np.loadtxt("out_loglog.txt")

plt.axline((0, 0), slope=1, ls="-.", c="gray")
plt.plot(R, P_lin, 'o', marker=r"$\ast$", label="Linear")
plt.plot(R, P_log, '.', label="Logarithmic")
plt.legend()
plt.show()
