---
layout: default
title: "Use Cases"
nav_order: 3
permalink: /use-cases/
---

# Use Cases
{: .no_toc }

Here are some usecases to better understand the functionalities and use them
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

[Install][ghub]{: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2}

## Basic Arguments

Let's start with something basic: creating arguments for your script/project.

```python
# we will start by importing the options class from the optioner module

from optioner import options

# lets also import argv (argument list) from sys module

from sys import argv
```

{: .highlight }
For each arg defined in shortarg must have their long version in the longargs list in the same order.


```python
# Now that we imported the required module, 
# lets initialize a class object of options class

# for this, first define the arguments that needs to be passsed
# to the options class. --> shortargs, longargs

shortargs = ['h', 's'] # two short arguments will be created -> '-h' and '-s'

longargs = ['help', 'setup'] # long versions of short args --> '--help' and '--setup'

# now lets initialize the class
optionCTRL = options(shortargs, longargs, argv[1:])
```

{: .note }
We used `argv[1:]` which means a list of all the elements in the argv list except the first one. The first element is always the current filename/filepath/file-relpath.


```python
# now lets parse the arguments in-accordance with the defined arguments
# and the arguments provided by the user

gotargs, check, error, falseargs = optionCTRL._argparse()
```

See the details about gotargs, check, error and falseargs [here](https://d33pster.github.io/optioner/features/#error-handling){: target='_blank' }

## Compulsory Arguments with Basic Arguments

Let's just pickup after importing the modules
```python
# while initializing, include compulsory short and long args

comp_short = ['s']
comp_long = ['setup']

optionCTRL = options(shortargs, longargs, argv[1:], comp_short, comp_long)
```

{: .note }
This will make `-s` or `--setup` argument compulsory and will generate errors if it is not provided.


## Compulsion Override

With the above cases, the `setup` argument was made compulsory. But if you want to see the help text with  `help` argument, you dont necessarily need to use `setup` argument. 

Here the ignore module comes in.
```python
# during initialization:

ignore = ['-h', '--help']

optionCTRL = options(shortargs, longargs, argv[1:], comp_short, comp_long, ignore)
```

{: .note }
This will bypass compulsion logic.

## If this then not that

Making one or more arguments mutually exclusive can be done by this feature.

```python
# during init

ifthisthennotthat = [['h','help'], ['v', 'version']]
# NOTE: this will make -v or --version and -h or --help mutually exclusive

optionCTRL= options(shortargs, longargs, argv[1:], comp_short, comp_long, ignore, ifthisthennotthat)
```

## Actual usage in your Scrip/Project

Now that you know 

```python
# import modules

from optioner import options
from sys import argv

# define args

shortargs = ['h', 's', 'v']
longargs = ['help', 'setup', 'version']
compulsory_short = ['s']
compulsory_long = ['setup']
ignore = ['-h', '--help', '-v', '--version']
ifthisthennotthat = [['h', 'help'],['v', 'version'], ...] # must be even pairs, here this means if -h or --help is present, -v or --version cannot be there.
# there can be more such pairs.

# make class object

optionCTRL = options(shortargs, longargs, argv[1:], compulsory_short, compulsory_long, ignore, ifthisthennotthat)

# parse args

actualargs, check, error, falseargs = optionCTRL._argparse()

## define conditions ##

# if there is a error in arguments, check will be false
if not check:
    # print error
    print(error)
# if no error:
else:
    if '-h' in actualargs or '--help' in actualargs:
        # do something
    elif '-s' in actualargs or '--setup' in actualargs:
        # do something else
    else:
        pass
```
<p align='center'>END OF USE CASES</p>

[ghub]: https://github.com/d33pster/optioner