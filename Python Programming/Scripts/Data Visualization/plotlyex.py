import plotly.graph_objects as go
fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[3, 1, 6]))
fig.write_html('first_figure.html', auto_open=True)