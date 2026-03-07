# A simple exemple of Dotplots on python https://plotly.com/python/dot-plots/

import plotly.express as px
df = px.data.medals_long()

fig = px.scatter(df, y="nation", x="count", color="medal", symbol="medal")
fig.update_traces(marker_size=10)
fig.show()
