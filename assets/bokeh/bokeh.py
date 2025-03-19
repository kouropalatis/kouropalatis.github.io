from bokeh.plotting import figure, output_file, show

# Create an output file
output_file("bokeh_plot.html")

# Create a simple line graph
p = figure(title="Bokeh Line Chart", x_axis_label="X", y_axis_label="Y")
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], legend_label="Trend", line_width=2)

# Save the plot and show it
show(p)