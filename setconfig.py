import yaml
import pandas as pd

E = pd.read_csv("matrix_experiment.csv")
print(E)
config = yaml.safe_load("config.yaml")

