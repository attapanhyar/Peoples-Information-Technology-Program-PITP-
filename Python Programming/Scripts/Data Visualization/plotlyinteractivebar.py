import plotly.graph_objects as go
fig = go.Figure(go.Bar(x=['A', 'B', 'C'], y=[20, 14, 23]))
fig.write_html('first_figure.html', auto_open=True)