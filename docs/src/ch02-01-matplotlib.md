# Matplotlib

[Matplotlib][1] is one of the most mature visualization libraries
in Python. It allows us to quickly create figures when we are
first exploring our data and models, and allows us to have a
lot of control over our final figures for publications.

Like many mature software projects, it can be a bit daunting 
to work with at first. There are a couple ways to approach things 
with Matplotlib, through what is known as the state-machine interface
of [matplotlib.pyplot][2] and the object oriented approach. Depending 
on our needs, we might prefer one over the other. We will take 
a look at both of these approaches. 


## Key Components of a Figure

There are several components of a Matplotlib figure. Understanding 
how each of these fit together will give us better control over our
visualizations. This is important when we want to present our work 
in papers, but it will also help us debug things when the default 
settings for figures don't quite come out right.

### Figure

This is the entire figure object. It keeps track of all the figure's 
[Axes][3], legends, titles, and the [canvas][4] object. 

```python
import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle('Empty Figure Without Axes')
plt.show()
```

<html>
<head>
<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
</head>
  <body>
    <img src="img/ch02-visualization/figure_empty.png" alt="empty" class="center" width="250"/>
  </body>
</html>

### Axes

`Axes` are an important part of Matplotlib's interface. These are what
you would consider the "plot" of your figure, the area in the image
that contains your data. A figure can have many `Axes`, but each `Axes`
can only have one `Figure`. Data limits for the figure can be controlled 
through `Axes` with `axes.Axes.set_xlim()` and `axes.Axes.set_ylim()`. Axes 
also hold titles and labels for each for each axis. Axes contain either 
two or three `Axis` objects.

### Axis

An `Axis` is acts as a scale delimeter for the `Axes`. They set the limits
of a figure and control the ticks of a plot.


## Creating Figures

While we will take a closer look at this over the next sections of this 
chapter, there are a couple of things you want to keep in mind when 
working with Matplotlib.

### Input Data

Matplotlib recommends using [Numpy][5] arrays as input types for figures.
You can often get away with using Python lists and [Pandas][6] dataframe
objects, but you might encounter some rough edges here and there when
using those object types.

### Two Iterfaces

As mentioned above, there are two main interfaces for Matplotlib, the
state-machine interface and the object-oriented interface. In the next
section, we will cover each of these approaches and talk about when you
would want to use each.

[comment]: References

[1]: https://matplotlib.org/
[2]: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot
[3]: https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes
[4]: https://matplotlib.org/3.2.2/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase
[5]: https://numpy.org/
[6]: https://pandas.pydata.org/
