import plotly.figure_factory as ff 
df = [dict(Task="Admission", Start='2024-01-01', Finish='2024-05-02'), 
	dict(Task="Classes", Start='2024-05-02', Finish='2024-11-11'), 
	dict(Task="Assignments", Start='2024-10-06', Finish='2024-10-30') ,
    dict(Task = "Final Examination", Start= "2024-11-15", Finish = "2024-11-25" )]
fig = ff.create_gantt(df) 
fig.write_html('first_figure.html', auto_open=True)
