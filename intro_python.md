*An introductory problem sequence for learning Python with askreduce.*


:
How do you open a terminal on your computer? How did this terminal software get on your computer?

::
On a modern Mac, you will have Terminal.app pre-installed in Applications/Utilities, which works fine. It's a good idea to "Keep in Dock" so that it's easy to get to.

iTerm2 is another popular terminal emulator for Macs, which you can download and install separately if you like.

On Windows, cmd.exe will give you a Windows "command line" of entirely the wrong kind. The Windows PowerShell is much better, but not recommended. You should use Git Bash, which you should get along with Git when you install from git-scm.com. It's a good idea to keep Git Bash easily accessible.

On *nix systems, you have lots of choices for terminals. The one that comes with your GUI system is probably fine. You may have access to virtual consoles, but these are not very commonly used for normal work.

A terminal emulator is a bit like a web browser in that it provides a more or less standard environment for a certain class of applications to run and provide an interface.


:
What shell are you connected to via your terminal?

::
Most people run bash as it is usually the default. Other alternatives include Z shell (zsh) and KornShell (ksh). The Z shell wrapper package oh-my-zsh is reasonably popular.

You can usually check your shell by running `echo $0`.

A shell is a program that provides a text-based interface to an operating system. It lets you run other programs, including other shells.


:
What are three ways to find the absolute path to your home directory?

::
One way:
cd
pwd

Another way:
echo ~

Yet another way:
echo $HOME


:
What environment variable controls the appearance of your shell prompt?

What are two different ways to display the contents of this variable?

How can you set the contents of this variable to be just "$ "?

::
Prompt appearance is controlled by `PS1`.

To get just `PS1`:
echo $PS1

To get all environment variables:
env

To set `PS1`:
export PS1="$ "


:
Compare a shell such as bash with Python. Is Python a shell?

::
Sort of! Especially IPython!


:
What are at least two ways to close a shell/terminal?

::
Depending on your system, `exit`, `logout`, using windowing system navigation (such as clicking something), and especially CTRL-D.


:
What does CTRL-C do?

::
CTRL-C will attempt to kill or otherwise stop a current process. It's very useful if you get into an infinite loop, for example.


:
What other keyboard shortcuts are useful for navigating text interfaces?

::
You should be fluent with at least the following, where "C" is CTRL and "M" is usually "ALT":

C-a: go to beginning of line
C-e: go to end of line
C-b: go back one character
M-b: go back one word
C-f: go forward one character
M-f: go forward one word
C-p: previous
C-n: next
C-r: reverse search
C-l: clear screen
C-k: kill to end of line (cut)
C-y: yank (paste)
C-t: transpose character


:
What text editor do you use? How do you start it? How did it get on your system?

::
You should be able to survive if you have only a terminal interface. `nano` is a good choice in a pinch because you can use it with the on-screen help.

It is a good idea to be comfortable with at least one of the two major coding editors: `vim` and `emacs`. There's some learning curve.

A GUI editor like Sublime Text, Atom, or even Notepad++ is not necessarily a bad choice for most work.

An IDE such as IDLE, Spyder, or PyCharm is also not necessarily a bad choice.


:
How did you install Anaconda Python 2.7?

::
This should be easy; see http://continuum.io/downloads


: How can you check your Python version?

::
python --version

Make sure you are running the version you think you are!


:
How can you check which executable runs when you type `python` at a shell?

::
which python


:
Where will your shell look for programs to run for you?

::
echo $PATH

You can alter your PATH just as we altered PS1. Anaconda works by altering your PATH so that the Anaconda Python is found first.


:
What other configuration can you do?

::
So much. Bash reads configuration from .bash_profile and .bashrc, for instance. You can get way into customizing your environment, and it can make you more effective and happier. I post my configuration here:

https://github.com/ajschumacher/.emacs.d


:
What is the standard method for installing Python packages?

::
pip install packagename

`pip` will find `packagename` on the Python Package Index (PyPI) and download and install it.

Anaconda has its own package management scheme, "conda," which I will continue to ignore.


:
How can you see all the Python packages you currently have installed?

::
One way:
pip list

Another way:
pip freeze

The second way produces `requirements.txt` files that are used for coordinating versions across project teams, and for your own sanity.

Python developers use virtual environments to manage multiple projects with multiple sets of dependencies. You can find out more about `virtualenv` and the tools that make working with it easier, such as `virtualenvwrapper` and `pew`. We aren't going into this today, but you may want to eventually.


:
How can you easily check whether you have a Python package installed?

::
pip freeze | grep packagename

This is a shell technique for piping the output from one program to another - in this case, `grep`. `grep` is insanely useful even in the simple form shown here. Don't search with your eyes - the computer can search for you!


:
Install the Python package called "gogpy". What is the current version?

::
pip install gogpy
pip freeze | grep gogpy

There are other ways to check this, but what's shown is a pretty common pattern.


:
What does REPL stand for?

::
Read Evaluate Print Loop

This is a common way to interact with (mostly) interpreted programming languages. A shell is (arguably) a REPL too.

Consider a shell or Python REPL as a remote entity that has some internal state: variables, etc. You communicate with that entity by sending it text (programs, commands), it does things, and then it (often) sends back a response, again in text. The whole game is carefully choosing the text you send so that you produce the internal states and responses that will be helpful to you.


:
How do you start a basic Python REPL?

::
python


:
Use `type()` to find the types of these Python literals:

 * 42
 * 3.14
 * 'cow'
 * True
 * [1, 2, 3]

::
>>> type(42)
<type 'int'>
>>> type(3.14)
<type 'float'>
>>> type('cow')
<type 'str'>
>>> type(True)
<type 'bool'>
>>> type([1, 2, 3])
<type 'list'>


:
Experimenting at the REPL: Does it matter whether you use single or double quotes around Python strings?

::
As long as they match, you will be fine with either.

Experimenting at a REPL is a very good thing! Be careful if you are writing a bunch of code without testing it as you go - you probably want to be testing and experimenting as you go.

Experiments can be as simple as this:


>>> "cow"
'cow'
>>> 'cow'
'cow'
>>> 'cow"
  File "<stdin>", line 1
    'cow"
        ^
SyntaxError: EOL while scanning string literal
>>> "cow'
  File "<stdin>", line 1
    "cow'
        ^
SyntaxError: EOL while scanning string literal


("EOL" is "End Of Line")


:
Experimenting at the REPL: Can you put elements of different types into the same list?

::
Yes.

>>> [1, 3.4, False, "gnu",]
[1, 3.4, False, 'gnu']


:
Experimenting at the REPL: What does the Python operator "**" do?

::
>>> 2**3
8

This is exponentiation.


:
Experimenting at the REPL: What is `5 / 2` according to Python?

::
In Python 2:

>>> 5/2
2


:
What are two ways to get natural floating point division in Python 2?

::
It's pretty common to just make one of the numbers involved a float, e.g.,

>>> 5/2.0
2.5

or

>>> float(5)/2
2.5

The above approaches can abet annoying mistakes. Another alternative is to import the nicer behavior that Python 3 has:

>>> from __future__ import division
>>> 5/2
2.5


:
Experimenting at the REPL: What do you get at the REPL when you enter `1, 3`? What is the type?

::
>>> 1, 3
(1, 3)
>>> type((1, 3))
<type 'tuple'>


:
How can you point the identifier `x` at a Python list initialized as `[1, 2, 3]`?

::
>>> x = [1, 2, 3]

This is often referred to as "assignment" but especially since lists are mutable it is useful to remember that there is a distinction here.


:
What do you get if you call `dir` on `x`?

>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


:
What is the (short) documentation for `dir`?

::
>>> help(dir)


Help on built-in function dir in module __builtin__:

dir(...)
    dir([object]) -> list of strings

    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.

You may need to leave the help screen by pressing "q".


:
What are two ways to exit the Python interpreter?

::
One way:
>>> quit()

Another way:
CTRL-D


:
How do you start an IPython REPL?

::
ipython


:
IPython provides a lot of conveniences. How does this in IPython differ from the same thing in the base Python interpreter?

    x = [1, 2, 3]
    dir(x)

::
IPython automatically pretty-prints most output. You could do the same in a normal Python interpreter like this:

from pprint import pprint
x = [1, 2, 3]
pprint(dir(x))

IPython makes things much more convenient.


:
What happens when you type "x." and then hit TAB?

::
IPython shows you a list of possible completions, which you should recognize from the output of `dir()`.

Tab-completion like this can also help you finish typing long commands or filenames.

Tab-completion is your friend. Look for it everywhere, and especially at the shell and in IPython.


:
IPython has "magic functions" that start with "%", and special syntax for accessing `help()` with an initial "?". What does "%paste" do?

::
?%paste

"Paste & execute a pre-formatted code block from clipboard."

This is very handy because it preserves indentation properly when you want to copy in a large chunk of code.


:
In IPython you can run normal shell commands by starting your line with an exclamation point.

Note that these commands run separately from IPython, so `!cd ~` will change the current directory but then immediately return and IPython will still be where it started. To change IPython's working directory you can use the magic function `%cd` though, so everything is fine.

Without leaving IPython, go to your home directory, make and enter a directory called `survival`, and make a file in that directory called `raft.py`.

::
%cd ~
!mkdir survival
%cd survival
!touch raft.py


:
Open `raft.py` in your editor and make it contain:

    raft_text = "one grade-a raft"
    print raft_text

How do these compare?

 * From IPython: `%load raft.py`
 * From a shell: `python raft.py` or `ipython raft.py`
 * From a shell: `python -i raft.py` or `ipython -i raft.py`
 * From a shell: `python -m pdb raft.py` or `ipython -m pdb raft.py`

::
 * IPython gives you the magic %load which behaves as if you had typed
   the contents of the file into the interpreter.
 * You can run a Python script all the way through and quit Python
   with `python scriptname`.
 * The `-i` flag will leave you in an interactive Python REPL after
   running through your code. This is useful because you can inspect
   the status of variables and do further experimenting.
 * Using `-m pdb` starts the Python debugger on your script. This can
   be useful for diagnosing complex problems. IPython can also use
   `ipdb` if you have it installed.


:
How can you make a Python script behave as an executable?

::
You need two things:
 * the file marked as executable to the operating system
 * Python specified as the way the file is run

To make the file eXecutable by the User (you), run the CHange MODe program from a shell, as:
chmod u+x raft.py

To specify Python as the interpreter for the file, the first line of the file should be a "shebang". The standard Python shebang is:
#!/usr/bin/env python

(If you're surprised that `env` is making an appearance again here, check out `man env`.)

Now you can run `raft.py` at the command line, as:
./raft.py


:
Try `import raft` from IPython. You'll see output. Refactor the `print` line into a `__main__` block so that you get no output when you `import`, but you get output when you run the script at the command line.

::
#!/usr/bin/env python

raft_text = "one grade-a raft"

if __name__ == '__main__':
    print raft_text

(This is also an example, slightly weird, of using `if` in Python.)


:
Python modules usually don't have output (or do anything, in fact) when they are imported. One exception is the `this` module. Try `import this`.

::
import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

(Notice the emphasis on namespaces.)


:
After `import raft`, how can you access the `raft_text`?

::
import raft
raft.raft_text


:
What if you want to import `raft_text` without the `raft` module namespace? Give two ways to import it directly.

::
One way:
from raft import raft_text

Another way:
from raft import *

The second way, with the *, is less well-liked because it imports everything to the root namespace, which can clutter the namespace with tons of identifiers.


:
What if you don't like the provided name? How can you import `raft_text` as `rt`, for example?

::
from raft import raft_text as rt

You can do this for modules as well, like:
import raft as super_cool_raft


:
What are the common import lines for `numpy` and `pandas`?

::
import numpy as np
import pandas as pd

You'll use these a lot, eventually.


:
If you change and save a file you're treating as a module, like `raft.py`, how can you reload it into a Python REPL?

::
Assuming you initially did `import raft`:
reload(raft)

We'll do more with this in a moment.


:
How do you run IPython Notebook on your computer?

::
One popular invocation is:

ipython notebook --pylab=inline

Whether to load `pylab` is up to you; many find it useful.

(There's also the Anaconda Launcher.)


:
How do you run Spyder on your computer?

::
You can start it from the command line:

spyder

(There's also the Anaconda Launcher.)


:
Ensure Spyder is using IPython. What is your present working directory? How do you change it to be `~/survival/`?

::
You can do it before inside the IPython terminal, or use the GUI: "Browse a working directory" and then "Set as current console's working directory" in the upper right.


:
Open `raft.py` in the Spyder editor. How do you run a selection from the editor?

::
Select what you want to run, then (on a Mac) press Command-Enter.

There are many more ways to execute sections of Python code inside Spyder. Feel free to explore the interface.


:
What's the value of `x`, `y`, and `z` after this?

    x = [1, 2, 3]
    y = x + [4]
    z = x.append(5)

::
x is [1, 2, 3, 5]
y is [1, 2, 3, 4]
z is None

Be careful with this sort of thing! Check carefully as you code!


:
Extension: How can you check whether a variable is `None`?

::
Use `is`. For example, the following is not uncommon:

if x is not None:
    # Do something about x


:
What other methods are there for lists?

How can you get help on list methods?

How can you get the LENgth of a list?

::
Using `dir()` or tab completion on a list (or `list`):

append
count
extend
index
insert
pop
remove
reverse
sort

Help still works via e.g., `help(list.pop)` or `?list.pop`.

The `len` function will give you the length.

>>> len([1, 2, 3])
3

Other useful functions include `sorted`, `reverse`, and `sum`.


:
Can you add a list and an integer? What about multiplication? What about a string and an integer? Can you add a string and a string? What happens?

::
You should find some useful phenomena.


:
Python functions are defined like this:

    def silly_subtract(x, y):
        return x - y

Load this definition in your REPL. Some of the following will fail. Why?

 * `silly_subtract(10, 7)`
 * `silly_subtract(10, y=7)`
 * `silly_subtract(x=10, 7)`
 * `silly_subtract(x=10, y=7)`
 * `silly_subtract(y=7, 10)`
 * `silly_subtract(y=7, x=10)`

::
The ones that don't work produce `SyntaxError: non-keyword arg after keyword arg`, which should make sense.


:
Put a function `make_rafts` in `raft.py` that takes arguments `num_rafts` and `num_passengers`. It should return a list of `num_rafts` strings, and each "raft" string should be all asterisks, and `num_passengers` long.

::
def make_rafts(num_rafts, num_passengers):
    return ["*" * num_passengers] * num_rafts


:
Give `num_passengers` a default value of 8.

::
def make_rafts(num_rafts, num_passengers=8):
    return ["*" * num_passengers] * num_rafts


:
Add a multi-line comment in docstring position for the function, explaining what it does. (Note that [PEP 8](https://www.python.org/dev/peps/pep-0008/) suggests code lines be no longer than 79 characters, and text lines no longer than 72.)

::
def make_rafts(num_rafts, num_passengers=8):
    """
    Returns a list of `num_rafts` strings with each "raft" string
    being `num_passengers` asterisks.
    """
    return ["*" * num_passengers] * num_rafts

Style conventions for docstrings may vary, but whatever the style, the docstring of a loaded function is what you get back from `help`, so make it helpful.


:
Change the `__main__` block to print the result of `make_rafts(1)`.

::
if __name__ == '__main__':
    print make_rafts(1)


:
Extension: Make the `raft.py` script accept command-line input for the number of rafts.


:
You aren't using the `raft_text` any more. Comment it out using a one-line comment.

::
# raft_text = "one grade-a raft"


:
DON'T COMMENT OUT CODE. Version control preserves old code; don't litter your code with carcasses. Remove the `raft_text` line entirely.

::
(the line is gone)

This rule doesn't apply to quick experiments, but in general you really don't want to be carrying around dead code. It makes things confusing and harder to maintain.

Line comments should be used to include natural human language that helps make an algorithm clearer, for example.


:
What does `make_rafts` do when it receives a negative `num_rafts`? Add behavior to `raise ValueError("Helpful message")` on untenable arguments.

::
def make_rafts(num_rafts, num_passengers=8):
    """
    Returns a list of `num_rafts` strings with each "raft" string
    being `num_passengers` asterisks.
    """
    if num_rafts < 0 or num_passengers < 0:
        raise ValueError("Negative quantities don't make sense!")
    return ["*" * num_passengers] * num_rafts


:
Extension: You can write some one-line `if` statements (etc.) in Python. This is sometimes discouraged because it can be less readable. But say you want `x` to be 'big' if `y` is over 10, and 'small' otherwise. How can you do it in one line?

::
x = 'small' if y < 20 else 'big'


:
Write a `for` loop that announces the departure of four rafts (by number) using `range`.

::
for raft_id in range(4):
    print "raft", raft_id + 1, "is away!"

Other ways to print:

print "raft %s is away!" % (raft_id + 1)

print "raft " + str(raft_id + 1) + " is away!"


:
Write a `for` loop that prints out each raft from `make_rafts(4)` on its own line.

::
for raft in make_rafts(4):
    print raft


:
Write a `for` loop that prints out each raft from `make_rafts(4)` on its own line, but with each subsequent raft farther from the shore.

::
for raft_id, raft in enumerate(make_rafts(4)):
    print " " * raft_id + raft

This is using tuple unpacking to assign to `raft_id` and `raft`.


:
Say `x` and `y` have values. How can you swap their values in one line? How does this demonstrate tuple packing and unpacking?

::
x = 1
y = 100
x, y = y, x
(x, y) = y, x
x, y = (y, x)
(x, y) = (y, x)


:
The `random` module includes a function `randint`. Write a new function `used_rafts` that takes one argument, `num_rafts`, and returns that many rafts with random capacities from 2 to 12.

::
from random import randint
#...
def used_rafts(num_rafts):
    """
    Returns a list of `num_rafts` strings with each "raft" string
    being randomly from two to twelve asterisks.
    """
    rafts = []
    for _ in range(num_rafts):
        rafts.append("*" * randint(2, 12))
    return rafts


:
Get a dozen used rafts and make a new list with the lengths of each raft.

::
rafts = used_rafts(12)
lengths = []
for raft in rafts:
    lengths.append(len(raft))


:
Get a dozen used rafts and make a new list with the lengths of each raft, but only use one line of code to do it.

::
rafts = used_rafts(12)
lengths = [len(raft) for raft in rafts]

This is called a list comprehension.


:
Extension: How can you use `map` to achieve the same result?


:
You can add an "if" filter to the end of a list comprehension. Write a line that gives you just the rafts that seat more than six.

::
[raft for raft in rafts if 6 < len(raft)]


:
Extension: How can you use `filter` to achieve the same result?


:
Add up the lengths of all the rafts.

::
sum(len(raft) for raft in rafts)

(That isn't quite a "list" comprehension, but it works.)


:
Extension: How can you use `reduce` to achieve the same result?


:
Re-write `used_rafts` to use a list comprehension.

::
def used_rafts(num_rafts):
    """
    Returns a list of `num_rafts` strings with each "raft" string
    being randomly from two to twelve asterisks.
    """
    return ["*" * randint(2, 12) for _ in range(num_rafts)]


:
Extension: Some functions take other functions as arguments. The `key` argument to the `sorted` function is itself a function, for example. Say you want to sort your rafts by how close they are to 7-passenger, for some reason. How would you do this?

::
sorted(rafts, key=lambda x: abs(len(x) - 7))

In Python the lambda syntax lets you define anonymous (nameless) functions. For example, these are equivalent:

def myfun(x):
    return x**2

myfun = lambda x: x**2


:
Sort your rafts.

::
rafts = sorted(rafts)

(This happens to work in a reasonable way because of the default sort for strings.)


:
Use slicing to get the first raft.

::
rafts[0]


:
Use slicing to get the last raft.

::
rafts[-1]


:
Use slicing to get the second and third rafts.

::
rafts[1:3]


:
Use slicing to get the first two rafts.

rafts[:2]

This is very useful for checking out a small part of a big list!


:
Use slicing to get the last two rafts.

::
rafts[-2:]

This is very useful for checking out a small part of a big list!


:
Use slicing to get every other raft.

::
rafts[::2]


:
Use slicing to get the rafts in reverse order.

::
rafts[::-1]


