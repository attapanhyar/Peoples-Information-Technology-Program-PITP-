import plotly.express as px 
df = px.data.tips() 
fig = px.violin(df, x="day", y="total_bill")
fig.write_html('first_figure.html', auto_open=True)
