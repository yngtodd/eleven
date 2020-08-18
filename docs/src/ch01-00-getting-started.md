# Getting Started with Python

We will be using Python throughout the course. Why Python and not
another language like Julia or R? While Julia and R have a lot to
bring to the table, Python has been a de facto choice for many 
data scientists. And for good reason, Python's ecosystem is mature;
there are countless libraries that you can use in your daily work.
Inevitably, we will introduce some of these libraries ourselves. 
Python is also not limited to data analysis. If ever you would 
like to explore applications outside of data science, Python is 
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

## Anaconda

We will start by using [Anaconda][1], a distribution of Python 
including a package manager with many of the packages commonly 
used in data science, and a way to manage programming environments. 
While not the only way to get started with Python, this is one of the 
most common approaches. Many collaborators at ORNL will be familiar 
with Anaconda, and it is an easy way to quickly get people on the same 
page when setting up their compute environments.

#### Installation

As of Fall 2020, the Anaconda is distributing Python 3.8. Don't worry if you
find that you need to use a different version of Python. Anaconda can help you
manage multiple versions of Python within `conda environments`. Just don't use 
Python 2. It is no longer supported by the Python Foundation, the governing 
body of Python.

> *Side Note*:\
> For much of this book we are assuming that you are using a Unix like operating
> system (Linux, MacOS, BSD). If you are using Windows, please let us know! We
> can help you sort out some potential issues you may have. For much of the 
> computing at ORNL, particularly when it comes to the supercomputers, Linux 
> is the default. We do not demand that you use a Unix like OS, but you may have
> to do some extra leg work.

#### Graphical Installer

For a graphical installer of Python, follow the download instructions [here][1]. 

#### Command Line Installation

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

#### Verifying our Installation

Once you have installed Anaconda, let's check to see that everything is working 
well. Let's start by checking where Python is installed:

```bash
which python
```

This will give you a path to where Python is installed. For example, my Python is 
installed in the following path:

```bash
which python
>>> /home/yngtodd/.local/opt/anaconda3/bin/python
```
We will discuss paths and the Linux filesystem a bit later on. For now, Let's make sure
that the path you get from `which python` includes `anaconda3/bin/python`. If instead you see
`/usr/bin/python`, then we need to do some debugging as you are using what is known as 
system Python instead of Anaconda.

> *Side Note*:\
> You may wonder what `which` is. This is a Unix program that is installed in Unix-like
> operating systems by default. It tells you the path to where any program you run on the 
> command line lives. Knowing more about the command line environment will be useful for us,
> but we need to get up and running with Python first! If you are curious and want to look 
> further into this, try `man which` to see the manual page for `which` (`man` is another
> default Unix program). What happens if you run `which which`?


### Resources

1. Corey Schafer's [YouTube video][3] on installing Anaconda
2. Anaconda [Docs][4]

[comment]: References

[1]: https://www.anaconda.com/products/individual
[2]: https://repo.anaconda.com/archive/
[3]: https://www.youtube.com/watch?v=YJC6ldI3hWk
[4]: https://docs.anaconda.com/anaconda/user-guide/getting-started/
