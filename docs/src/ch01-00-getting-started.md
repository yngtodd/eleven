# Getting Started with Python

We will be using Python throughout the course. Why Python and not
another language like Julia or R? While Julia and R have a lot to
bring to the table, Python has been a de facto choice for many 
data scientists. And for good reason, Python's ecosystem is mature;
there are countless libraries that you can use in your daily work.
Inevitably, we will introduce some of these libraries ourselves. 
Python is also not limited to data analysis. If ever you would 
like to expolore applications outside of data science, Python is 
not a bad initial choice.

> *Side Note*:\
> if you are interested other languages, you are in good
> company. Jacob is a big fan of Haskell and Todd loves Rust and still
> appreciates C. We can't include all of the languages we care about in
> this course, but if you would like to know how you can use another language
> over the course of your PhD, let us know! We can get you connected with
> people that would also like to use your language of choice (especially
> if it is Haskell or Rust). There are people at the lab that use R, 
> and there are people who are interested in pushing things further with Julia.

### Anaconda

We will start by using [Anaconda][1], a distribution of Python 
including a package manager with many of the packages commonly 
used in data science, and a way to manage programming environments. 
While not the only way to get started with Python, this is one of the 
most common approaches. Many collaborators at ORNL will be familiar 
with Anaconda, and it is an easy way to quickly get people on the same 
page when setting up their compute environments.

#### Installation

As of Fall 2020, the Anaconda is distributing Python 3.8. 

##### Graphical Installer

For a graphical installer of Python, follow the download instructions [here][1]. 

##### Command Line Installation

If you prefer to work on the command line, you can find various versions 
of bash install scripts in the [Anaconda archive][2]. Make sure that you 
grab the appropriate 64 bit installer for you operating system in the archive,
then download it using wget:

```bash
wget https://repo.anaconda.com/archive/<Filename>
```

where `<Filename>` is the name of the bash script found in the archive. For
example, if you are on a 64 bit Linux system, use

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
```

Once you have that install script, follow the steps outlined after running the 
installer:

```bash
bash <Filename>
```


[comment]: References

[1]: https://www.anaconda.com/products/individual
[2]: https://repo.anaconda.com/archive/
