---
layout: default
title: "Use Cases"
nav_order: 3
permalink: /use-cases/
---

# Use Cases
{: .no_toc }

Here are some usecases to better understand the functionalities and use them
{: fs-6 .fw-300 }

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

```python
# Now that we imported the required module, 
# lets initialize a class object of options class

# for this, first define the arguments that needs to be passsed
# to the options class. --> shortargs, longargs

# NOTE: for each arg defined in shortarg must have their long version in the longargs list in the same order.

shortargs = ['h', 's'] # two short arguments will be created -> '-h' and '-s'

longargs = ['help', 'setup'] # long versions of short args --> '--help' and '--setup'

# now lets initialize the class
optionCTRL = options(shortargs, longargs, argv[1:])

# NOTE: we used argv[1:] which means a list of all the elements in the argv list 
#except the first one. The first element is always the current filename/filepath/file-relpath
```

```python
# now lets parse the arguments in-accordance with the defined arguments
# and the arguments provided by the user

gotargs, check, error, falseargs = optionCTRL._argparse()
```

See the details about gotargs, check, error and falseargs [here](https://d33pster.github.io/optioner/features/#error-handling){: target='_blank' }

[ghub]: https://github.com/d33pster/optioner