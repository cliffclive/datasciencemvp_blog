Title: After the MVP — Moving to a Dev Workflow
Author: Cliff Clive
Date: 2019-08-02
Category: blog
Tags: python, datascience, design, workflow, mvp, dev
Slug: mvp2dev
Status: published

# After the MVP — Moving to a Dev Workflow

From an engineering perspective, building a minimum viable product is an opportunity to quickly test an idea and see if it works. It doesn't need to be the best solution, it should just be a usable solution. If it is, then we can move on to the development stage and make it work well.

The objectives of the MVP stage are:

- Formulate a workable business question.
- Define a strategy for models that convert the available data into actionable insights.
- Obtain (and clean) the data, explore meaningful relationships between variables, identify biases in the data set and your team's beliefs, build and evaluate a model.
- Determine whether the model is good enough to be worth building out with more data, better features, etc.

If we've done all of these and it looks like our model is a good candidate for solving our business problem, then we want to put some work into optimizing it. Now we want to move from our MVP on to a Dev stage.

# The Dev Workflow

When we're done with our MVP, we have coded up a workflow that can access our data, convert it into predictive features, build and train a model with some subset of our observations, and evaluate its performance on a holdout set.

If we've built the MVP correctly, we should be able to load our notebook on another computer, click Cells/Run All, and it should execute without fail. (Assuming the other computer has all of our dependencies installed — this is easily provided for with conda environments, a topic I will cover in another post.)

Since the MVP is a proof of concept, then we should have built it fairly quickly. Think of the motto "Fail Fast" — if an idea is not going to work, we want to know that as soon as possible. So when your MVP is done, it shouldn't be made of the most beautiful code you've ever written. It should be written clearly enough that other data scientists will be able to follow along and understand what you did. But it shouldn't be any nicer than that.

But now we have a new objective. We know that our code works and that our model is looking like a good candidate to solve our business problem. Now we want to be able to explore ideas to make our model perform even better. In the MVP stage, we wanted to get from data to model results as fast as possible without taking shortcuts. In the Dev stage, we now want to play with variations on that process efficiently and find the best one. 

We can do this much more effectively if we clean up our code so that we only have to look at the parts we want to change.

# Developing With Packages

At this point I strongly recommend converting as much of your MVP code as possible into clean Python functions, and then putting the useful ones into a Python package. This may seem like a job for a software engineer, not a data scientist, but here are three advantages for taking the time to do this:

- Working with a package will make your iterations go faster.
- It will be easier to share your work with your team and the community.
- It's the right way to do things.

Besides, if you make your code open source, or share it with your team, you can always get software engineers to clean it up and make things work even better.

Once you've built and published your package, the Dev workflow is easy. Make a copy of your MVP notebook (copy mvp.ipynb to dev.ipynb), import your package and replace all of the messy code blocks with the functions you packed them in. Now your code should be much more readable, and the only things you need to change are the parameters you want to experiment with as you try to improve your model.

You are now ready to begin the Dev stage of your project. For every variation of your model that you would like to explore, make a new copy of dev.ipynb and make the relevant edits to the code cells, and edit the related markdown cells to describe your new approach.

# Preparing a Python Package — Refactoring Your Code

There are many, many design philosophies to organizing code into a useful set of functions. This can feel like an overwhelming task the first time you do it. With practice, you learn what works for you, and you'll start incorporating a lot of these (or your own) ideas into your workflow every time you code.

For a general overview, I recommend this process:

### 1. Map Out Your Code

Identify the data sources used, the locations where the data is stored, the variables that the data is loaded into, operations (functions and transformations) carried out on those variables, and the outputs created along each step of the way.

### 2. Identify Access Points

When you make future passes through this workflow, which variables and parameters will you actually want to change? These should be the only ones that are visible outside of the functions you will build to contain the rest of your code. Access points are here defined as the inputs, parameters, and outputs of the functions you will want to write.

### 3. Write Functions to Encapsulate Your Work

Good design principles for writing clean code is outside the scope of this post, but here are some of the most important points:

- Give your functions descriptive names; I recommend using a verb for the first word in a function's name.
- Keep them simple; they should take few inputs and do only one thing to them.
- A function that does more than one thing should be a pipeline that calls other, simpler, functions in sequence.

Well-written functions make it eash to write human-readable code. When you're done encapsulating your MVP code into these functions, and then replace those code blocks with the new functions, it should read like a recipe that even the non-technical members of your team can read and understand.

# Building a Python Package — v 0.0.1

If this is your first time building a Python package, don't worry, it's not so hard. The official [Python Packaging User Guide](https://packaging.python.org/tutorials/packaging-projects/) provides a simple tutorial that takes about 15 minutes to work through and post your package to TestPyPI (the testing grounds for PyPI, the Python Packaging Index, which is where `pip` installs packages from). 

If you are unfamiliar with how Python modules and packages work, take a quick look at the [Python documentation for packages and modules](https://docs.python.org/3/tutorial/modules.html#packages). You will want to create a working directory for building your package (similar to the `packaging_tutorial` directory in the Python Packaging User Guide), and inside of that you will want to created a subdirectory that contains your modules (or scripts), as in the `example_pkg` directory in the same guide. You will write your functions in `xxxx.py` files inside this subdirectory. 

If you are happy with your package and want to upload it to PyPI (the User Guide above only covers through how to upload to TestPyPI), you'll want to run the command

```
twine upload -u PYPI_USERNAME dist/*
```

You may also be interested in setting up docstrings, unit tests, and continuous integration. Brendan Herger's [cheat sheet](https://www.hergertarian.com/cheat-sheet-publishing-a-python-package) to publishing Python packages gives a decent overview to these topics, with links to more in-depth resources.