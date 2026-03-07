import plotly.graph_objects as go #for isosurface
import numpy as np

#Example
X, Y, Z = np.mgrid[-40:40:40j, -40:40:40j, -40:40:40j]

# ellipsoid
values = X * X * 0.5 + Y * Y + Z * Z * 2
print(X)
print(values)
fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=10,
    isomax=2000,
    surface_count=4,
    caps=dict(x_show=False, y_show=False)
    ))
fig.show()