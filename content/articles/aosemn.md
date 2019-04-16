Title: OSEMN is Awesome, but AOSEMN is Awesomer
Author: Cliff Clive
Date: 2019-04-16
Category: blog
Tags: python, datascience, design, workflow, mvp
Slug: aosemn
Status: hidden

The OSEMN (Obtain, Scrub, Explore, Model, Interpret) framework for data science has been widely adopted since [Hilary Mason introduced the concept in 2010](http://www.dataists.com/2010/09/a-taxonomy-of-data-science/). This is by no means the only workflow out there -- I particularly like Ciara Byrne's[Development Workflows for Data Scientists](https://resources.github.com/downloads/development-workflows-data-scientists.pdf) -- but they're all variations of the same core modules of a pipeline. I like OSEMN for the simple reason that it's easy to remember, and so it's more likely that I'll stick to the steps. (And that I can convince my students at [Metis](https://thisismetis.com) to use those steps in their own projects.)

## Design Matters

Workflows are effective because they provide direction that keep us moving through each stage of a project. When we adopt them, we minimize the time spent wondering about the next thing we should do. Without good design principles, though, a workflow is just a process. It can take us from point A to point B -- but how do we know which point B we're trying to get to?

There is one other principle that I feel is at least as important as any of the OSEMN five, particularly if our objective is to promote good workflows. And that principle is Design. This preliminary stage sets the course for all of the others. With a good project design in place, we know what we're trying to solve. We know how to determine what data is relevant. We know how to decide which models are more likely to get us there. Perhaps most importantly, we know how to tell other people what our model does and why they should care.

This is by no means a suggestion that Hilary Mason or other data scientists aren't spending time designing their projects before they start them. But by making it an explicit part of the workflow, I hope that new data scientists will develop the habit of thinking through their work before they download the first data set they can find and start hacking away at it.

But wait a second, Design doesn't start with an A... how does this fit into the acronym?

## Start by Writing an Abstract

_A problem well stated is a problem half-solved._

If we begin our work with the end in mind, that gives us a standard to evaluate all of the decisions we will make on the way to get there. Otherwise, we run the risk of deciding that decisions are good just because they work with the dataset that we've found. We should be in the business of building models that solve problems, not inventing problems that our models happen to solve.

This design process, broadly speaking, should follow these steps:

1. Identify your end user. Who has the problem, or is asking the question, that your work is going to solve?
2. Brainstorm ideas that may answer this question or solve this problem. This is a conversation that involves exploring the context of the problem and looking for specific challenges that can be solved with better use of data.
3. Prototype some of these ideas to create an MVP (minimum viable product). The key factors of a good MVP are that it is:
* Minimum: If something quicker or simpler can give a solution, go with that.
* Viable: It produces a solution, something that can take an input and produce an actionable (or insightful) output. It doesn't have to be a great solution, anything better than rolling the dice or flipping a coin is good enough.
* Product: The solution that your MVP arrives at should be something that your end users can apply to their problem.

Following a practice that I learned while working at Amazon, where every new project begins by writing a mock press release that describes their envisioned finished product, I'm an advocate for beginning data science projects by writing a mock **Abstract**, which sets the agenda for what we plan to accomplish and how we believe we can do it.

Starting with an Abstract gives us an opportunity to not only design the project, but put that design into writing. This will provide us with a plan of attack that we can follow for an end result, give us an opportunity to do some background research to better understand the problem space and other approaches that have been taken, and to give us a sanity check that our project idea is at least a fairly reasonable one.

Put your ideas into writing. Take a break and then read them again. Does this look like an idea worth pursuing? If not, take some time to think things through again.

## How to Write a Good Abstract

At the start of your project, you won't be able to summarize the work you haven't done yet. But you should be able to put together ideas for most of these questions. And putting some thought into spelling out how you will know when you've got an answer is going to be extremely helpful for establishing the right perspective at the beginning.

A good abstract should answer these questions:

- End User: who has this problem and what are their needs?
- Problem Statement: what are you trying to solve?
- Motivation: why does this problem matter and how will our results meet that need?
- Approach: what data should be useful for solving the problem and what kinds of models will able to turn the data into a solution?
- Results: what will our model output look like and how can we put it to use?
- Conclusions: once we have our results, how can we evaluate them to show that the model is working?

If we can provide well thought out answers to the first three questions, and provide a plan and conditions for success for the last three, we are setting ourselves up for a quick and effective workflow. 

## Build and Iterate

And now you're off! Spending some time writing out your mock Abstract and putting together a compelling plan will save you loads of time as you proceed with your project. You'll spend less time wondering what to do next when you know the direction you're heading. You'll avoid going into rabbit holes researching new ideas, because you'll be much better prepared to decide how well these ideas fit into your master plan. You'll know when you have a strong case to make for your model because you will have put in the time deciding what that case looks like, _before_ you've biased yourself with the need to justify the hours you've put into whatever it is that you've got.

