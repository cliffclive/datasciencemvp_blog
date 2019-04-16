Title: The Data Science MVP Template
Author: Cliff Clive
Date: 2019-04-16
Category: blog
Tags: python, datascience, engineering, workflow, mvp, etl
Slug: datasciencemvp_thetemplate


[Data Science MVP](https://github.com/cliffclive/datasciencemvp)  is a template to jumpstart a minimum viable product (MVP), or rough draft of a data science project.

It is implemented as a [cookiecutter template](https://cookiecutter.readthedocs.io/en/latest/) that generates a directory tree containing subdirectories that hold data, notebooks, reports, source code, etc., with code stubs that present a logical workflow for assembling a pipeline for a reproducible data science project. (In its current version it is a modification of the [cookiecutter data-science](https://drivendata.github.io/cookiecutter-data-science/) template, although that is likely to change in the future.)

At its heart is a Jupyter notebook (stored as `mpv.ipynb` in the `/notebooks` directory) with markdown and code cells pre-filled with suggestions for how to proceed through building an MVP. Each code cell has a commented-out `%%writefile` command that will write the cell's contents to into a Python script stored in the `/src` directory. In the top-level directory, there is a `main.py` script that executes the entire pipeline as implemented in the `/src` directory.

Once the `mvp.ipynb` notebook is completed and the code is exported to `/src`, the data scientist can focus on making iterative improvements to each step in the pipeline. When the project is complete, it should be easy to export the models and source code into a Python package that can be shared with others.

## How do I use this?

### Install cookiecutter and generate the template project files

First you will need to install `cookiecutter` if you haven't already

```bash
pip install cookiecutter
```

and then run the following command from the terminal to create a new project directory loaded with the files and folders from the template:

```bash
cookiecutter https://github.com/cliffclive/datasciencemvp
```

The prompt in the terminal will guide you through naming your project and its filepath, and then populate the project directories. 

Once it's all set up, initialize a git repo in the project's top level directory and you can get to work.

### Read through `main.py` and the default scripts in `/src`

After you've built the template, you'll want to go into the `/notebooks` folder and start editing `mvp.ipynb`. But first take a look at `main.py` in the top level directory, which is reproduced here:

```python
import src.data.make_dataset
import src.features.build_features
import src.models.train_model
import src.models.predict_model
import src.visualization.visualize

# Usage: 
# $ python main.py
if __name__ == "__main__":
    src.data.make_dataset.run()
    src.features.build_features.run()
    src.models.train_model.run()
    src.models.predict_model.run()
    src.visualization.visualize.run()
```

Note that `main.py` is importing all of the scripts that will be built by the `%%writefile` commands in `mvp.ipynb`, and that each of these scripts contains a `run()` function that executes a module of the pipeline. If you run this script at the commandline right out of the box, it will produce this output:

```bash
 $ python main.py
src.data.make_dataset.run()
...processing raw data
...saving interim data
...processing interim data
...processing external data
...
src.features.build_features.run()
...reading interim data
...building features dataframe
...performing train/test split
...saving processed data
...
src.models.train_model.run()
...importing ml models
...building ml model
...reading train/test datasets
...training ml model
...saving ml model
...
src.models.predict_model.run()
...loading trained model
...loading new data
...making some predictions
...
src.visualization.visualize.run()
...drawing some charts
...saving the charts
...
```

As you can see, the default `run()` functions provided in the repo each print out their name and some suggestions for the types of actions you will want to implement inside them. Note that with no inputs and outputs for any of these `run()` functions, these are expected to run independently of each other. But you are free to reimplement these however you see fit.

### Work through `mvp.ipynb` and build the first draft of your pipeline

With the dummy code in the included scripts, and the code stubs in the `mvp.ipynb` notebook, you should have a pretty good idea what steps to take to get a baseline model up and running. 

Keep in mind that right now we're just concerned with engineering a pipeline that builds _a_ model, _any_ model. It doesn't have to be a great model. We're just engineering a system that can quickly translate ideas into results. Your best ideas will come later, and they'll come faster if you have the right tools in place to quickly test and refine them.

### Interpret your results and iterate on your pipeline

When you're done with your MVP, you should have a trained model, and some charts and reports to interpret how well your model performs. This gives you everything you need to go back and make changes at any step where you think improvements can be made, whether it's in collecting more data, engineering more features, choosing a new model, and so on.

If all of the steps are running independently, you can re-run your pipeline after any changes and see how they impact the end-to-end workflow. Take care to save any data that you've downloaded or formatted, and re-load the data from disc any time you re-run your pipeline... unless you're working on the Obtaining or Scrubbing data stages. Quick iterations are key to staying productive.

### Save your work!

At this point, how you proceed is up to you. Your reproducible pipeline lives in the scripts in the `/src` directory and any updates need to be added to those files in order to run the pipeline with `main.py`. You can use Jupyter notebooks, an interactive Python environment, an IDE, or a text editor and the commandline to play with new ideas -- `/src` is a Python package so you can import any of the functions you've written from the top directory. 

Just make sure that every time you find something that works, you edit the relevant file in `/src` and run `main.py` again make sure it doesn't break anything. And commit those changes to git right away!

### Come back later and check for updates

This is still a work in progress. I'm playing around with it, and my students at [Metis](https://thisismetis.com) are working with it and providing feedback. I'd love to hear your suggestions for how to make this workflow even better.

I wouldn't recommend applying any of these changes to a `datasciencemvp` project that you're already working on -- once you've built a project from the template you're free to make your own adjustments. But if everything is working as it should, the hope is that this will help you finish projects faster and be ready to use the latest version on your next one.