import plotly.express as px
ternplot=px.scatter_ternary #https://plotly.com/python/ternary-plots/

#Example of plots ternary diagram
#Careful the axis are automatically normalizing themselves, points at angles may be difficult to see
df = px.data.election()
fig = ternplot(df, a="Joly", b="Coderre", c="Bergeron")
print(df)
fig.show()