---
layout: default
title: Features
nav_order: 2
permalink: /features/
---

# Features
{: .no_toc }

Optioner comes with some pretty eye catching features.
{: fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

[Create Issue][issues]{: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2}

## Error Handling

Optioner parses the arguments, detects errors and returns them to the user to deal with them as they please instead of raising errors and ruining the aesthetics. XD

```python
# all the work is done in the _argparse function of the options class.
class options:
    ...

    def _argparse(self):
        """_argparse: checks all the arguments and stores error if any
        
        Return:
            actualargs (list): all valid args found.
            argcheck (boolean): Boolean (True: all good, False: Found undefined args). NOTE: this can be used to determine if error has occured and then argerror can be displayed accordingly.
            argerror (str): error note (if all good, no error note)
            falseargs (list): wrong args if any. (if None, empty list)
        """

        ...
    
    ...
```

## Dealing with compulsory arguments
{: .d-inline-block }

New (v1.4)
{: .label .label-green}

Optioner provides an option to set compulsory arguments which will be necessary for the script to run.

`For example:`<br>
Suppose you have a script that takes two arguments -> '-s' and '-d'. Your script needs the '-d' option everytime it is run and hence it is compulsory for the user to provide this argument. However, '-s' does not pose such a compulsion.

Here's how to achieve this using Optioner:
```python
# the _argparse module automatically checks if any compulsory argument is missing, and updates the errors

class options:
    ...

    def _argparse(self):
        # when all checks are done and all the variables have been updated.

        ## FOR THIS
        # self._argcheck -> boolean -> True if no errors
        # self._compulsory_short (compulsory short arguments) and self._compulsory_long (long versions of the compulsory arguments) must have atleast one element.
        if self._argcheck and len(self._compulsory_short)>0 and len(self._compulsory_long)>0:
            # since length of compulsory short and long list will be same (each short arg must have a longer version), lets just take either short or long to define a range
            for i in range(len(self._compulsory_short)):
                # if both short and longer version of an arg is not present in the found list of args, then generate error. NOTE: self._gotargs is the list of all args that are identified from the user given arguments.
                if (self._compulsory_short[i] not in self._gotargs) and (self._compulsory_long[i] not in self._gotargs):
                    # store error and turn boolean variable to False (as there is error)
                    self._argerror = f'\'{self._compulsory_short[i]}\' or \'{self._compulsory_long[i]}\' argument is Compulsory'
                    self._argcheck = False
                    # make sure to break out of the loop. This means if there are 2 or more compulsory arguments then this code will generate error untill all the compulsory args are given
                    break
```


[issues]: https://github.com/d33pster/optioner/issues