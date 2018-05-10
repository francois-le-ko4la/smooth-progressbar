# smooth-progressbar
## Description:

This package provide a simple progress bar.

## Setup:
```shell
git clone https://github.com/francois-le-ko4la/smooth-progressbar.git
cd smooth-progressbar
make install
```

## Test:
```shell
make test
```

## Use:

```python
from smoothprogressbar import SmoothProgressBar
my_progressbar = SmoothProgressBar()
my_progressbar.start(10)

for i in range(1, 11):
    myPB.update(i, "task "+str(i))
    time.sleep(2)
my_progressbar.stop()
```

## Result:

    Processing (10.0%): |//                  | 0:00:01 | task 1
    Processing (20.0%): |////                | 0:00:03 | task 2
    Processing (30.0%): |//////              | 0:00:05 | task 3
    ...


## Project Structure
```
.
├── last_check.log
├── LICENSE
├── Makefile
├── MANIFEST.in
├── pictures
│   ├── classes_smooth-progressbar.png
│   └── packages_smooth-progressbar.png
├── README.md
├── requirements.txt
├── runtime.txt
├── setup.cfg
├── setup.py
├── smooth_progressbar
│   ├── __about__.py
│   ├── __init__.py
│   └── progressbar.py
└── tests
    ├── run_it.py
    ├── test_doctest.py
    └── test_pycodestyle.py
```

## Todo:

- [X] Create the project
- [X] Write code and tests
- [X] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [X] Validate features
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [ ] Clean & last check
- [ ] Release

## License

This package is distributed under the [GPLv3 license](./LICENSE)
## Dev notes
### Runtime

```
python-3.6.x

```
### Requirements

```
pycodestyle>=2.3.1
setuptools>=36.2.7

```
### UML Diagram
![alt text](pictures/classes_smoothprogressbar.png)

### Objects
[Console()](#console)<br />
[@Property: Console.size](#property-consolesize)<br />
[Console.__init__(self)](#consoleinitself)<br />
[Console.addmsg(self, msg)](#consoleaddmsgself-msg)<br />
[Console.addtab(self)](#consoleaddtabself)<br />
[Console.emptyline(self)](#consoleemptylineself)<br />
[Console.goback(self)](#consolegobackself)<br />
[Console.newline(self)](#consolenewlineself)<br />
[Console.print(self)](#consoleprintself)<br />
[ConsoleLabel()](#consolelabel)<br />
[ConsoleLabel.__init__(self, txt, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, tag_beg='', tag_end='', color=False)](#consolelabelinitself-txt-frmtfunction-consolestringalign_left-at-0x7f3c63f5df28-tag_beg-tag_end-colorfalse)<br />
[ConsoleLabel.__len__(self)](#consolelabellenself)<br />
[ConsoleLabel.__new__(cls, txt, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, *args, **kw)](#consolelabelnewcls-txt-frmtfunction-consolestringalign_left-at-0x7f3c63f5df28-args-kw)<br />
[ConsoleString.__repr__(self)](#consolestringreprself)<br />
[ConsoleString.__str__(self)](#consolestringstrself)<br />
[ConsoleString.align_left(self)](#consolestringalign_leftself)<br />
[ConsoleString.align_right(self)](#consolestringalign_rightself)<br />
[ConsoleProgress()](#consoleprogress)<br />
[ConsoleProgress.__init__(self, size, ratio, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, tag_beg='[', tag_end=']', block='#', empty='.')](#consoleprogressinitself-size-ratio-frmtfunction-consolestringalign_left-at-0x7f3c63f5df28-tag_beg-tag_end-block-empty)<br />
[ConsoleProgress.__len__(self)](#consoleprogresslenself)<br />
[ConsoleProgress.__new__(cls, size, ratio, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, tag_beg='[', tag_end=']', block='#', empty='.', *args, **kw)](#consoleprogressnewcls-size-ratio-frmtfunction-consolestringalign_left-at-0x7f3c63f5df28-tag_beg-tag_end-block-empty-args-kw)<br />
[ConsoleString.__repr__(self)](#consolestringreprself)<br />
[ConsoleString.__str__(self)](#consolestringstrself)<br />
[ConsoleString.align_left(self)](#consolestringalign_leftself)<br />
[ConsoleString.align_right(self)](#consolestringalign_rightself)<br />
[ConsoleString()](#consolestring)<br />
[@Property: ConsoleString.max_size](#property-consolestringmax_size)<br />
[@Property: ConsoleString.text](#property-consolestringtext)<br />
[ConsoleString.__init__(self, txt, frmt=None)](#consolestringinitself-txt-frmtnone)<br />
[ConsoleString.__new__(cls, txt, *args, **kw)](#consolestringnewcls-txt-args-kw)<br />
[ConsoleString.__repr__(self)](#consolestringreprself)<br />
[ConsoleString.__str__(self)](#consolestringstrself)<br />
[ConsoleString.align_left(self)](#consolestringalign_leftself)<br />
[ConsoleString.align_right(self)](#consolestringalign_rightself)<br />
[ElapseTime()](#elapsetime)<br />
[ElapseTime.__init__(self)](#elapsetimeinitself)<br />
[ElapseTime.__repr__(self)](#elapsetimereprself)<br />
[ElapseTime.__str__(self)](#elapsetimestrself)<br />
[ElapseTime.start(self)](#elapsetimestartself)<br />
[MultiThread()](#multithread)<br />
[@Property: MultiThread.func](#property-multithreadfunc)<br />
[MultiThread.__init__(self, func, elapse)](#multithreadinitself-func-elapse)<br />
[MultiThread.run(self)](#multithreadrunself)<br />
[MultiThread.stop(self)](#multithreadstopself)<br />
[Thread.__repr__(self)](#threadreprself)<br />
[Thread._bootstrap(self)](#thread_bootstrapself)<br />
[Thread._bootstrap_inner(self)](#thread_bootstrap_innerself)<br />
[Thread._delete(self)](#thread_deleteself)<br />
[Thread._reset_internal_locks(self, is_alive)](#thread_reset_internal_locksself-is_alive)<br />
[Thread._set_ident(self)](#thread_set_identself)<br />
[Thread._set_tstate_lock(self)](#thread_set_tstate_lockself)<br />
[Thread._stop(self)](#thread_stopself)<br />
[Thread._wait_for_tstate_lock(self, block=True, timeout=-1)](#thread_wait_for_tstate_lockself-blocktrue-timeout-1)<br />
[Thread.getName(self)](#threadgetnameself)<br />
[Thread.isDaemon(self)](#threadisdaemonself)<br />
[Thread.is_alive(self)](#threadis_aliveself)<br />
[Thread.join(self, timeout=None)](#threadjoinself-timeoutnone)<br />
[Thread.setDaemon(self, daemonic)](#threadsetdaemonself-daemonic)<br />
[Thread.setName(self, name)](#threadsetnameself-name)<br />
[Thread.start(self)](#threadstartself)<br />
[Percent()](#percent)<br />
[@Property: Percent.max_value](#property-percentmax_value)<br />
[@Property: Percent.ratio](#property-percentratio)<br />
[@Property: Percent.value](#property-percentvalue)<br />
[Percent.__init__(self, max_value)](#percentinitself-max_value)<br />
[Percent.__repr__(self)](#percentreprself)<br />
[Percent.__str__(self)](#percentstrself)<br />
[SmoothProgressBar()](#smoothprogressbar)<br />
[@Property: SmoothProgressBar.msg](#property-smoothprogressbarmsg)<br />
[SmoothProgressBar.__init__(self, enable_elapse=True, enable_msg=True)](#smoothprogressbarinitself-enable_elapsetrue-enable_msgtrue)<br />
[SmoothProgressBar.__refresh(self)](#smoothprogressbar__refreshself)<br />
[SmoothProgressBar.start(self, max_value)](#smoothprogressbarstartself-max_value)<br />
[SmoothProgressBar.stop(self)](#smoothprogressbarstopself)<br />
[SmoothProgressBar.update(self, value, msg='')](#smoothprogressbarupdateself-value-msg)<br />


#### Console()
```python
class Console(object):
```

```
This Class provides a simple way to manage the screen

Use:
    >>> c = Console()
    >>> c.addmsg("lorem ipsum dolor sit amet consectetur adipiscing elit")
    >>> c.print()
    lorem ipsum dolor sit amet consectetur adipiscing elit
    >>> c.addmsg("lorem ipsum dolor sit amet consectetur adipiscing elit")
    >>> c.newline()
    >>> c.addmsg("LOREM")
    >>> c.print()
    lorem ipsum dolor sit amet consectetur adipiscing elit
    LOREM
```

##### @Property: Console.size
```python
@property
def Console.size(self):

```
> <br />
> @Property<br />
> <br />
##### Console.__init__(self)
```python
def Console.__init__(self):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### Console.addmsg(self, msg)
```python
def Console.addmsg(self, msg):
```
> <br />
> Docstring empty<br />
> <br />
##### Console.addtab(self)
```python
def Console.addtab(self):
```
> <br />
> Docstring empty<br />
> <br />
##### Console.emptyline(self)
```python
def Console.emptyline(self):
```
> <br />
> Docstring empty<br />
> <br />
##### Console.goback(self)
```python
def Console.goback(self):
```
> <br />
> Docstring empty<br />
> <br />
##### Console.newline(self)
```python
def Console.newline(self):
```
> <br />
> Docstring empty<br />
> <br />
##### Console.print(self)
```python
def Console.print(self):
```
> <br />
> Docstring empty<br />
> <br />
#### ConsoleLabel()
```python
class ConsoleLabel(ConsoleString):
```

```
Why:
    It's usefull to manage the screen size.

Use:
    >>> c = ConsoleLabel("lorem ipsum dolor")
    >>> str(c)
    'lorem ipsum dolor'
    >>> c.max_size = 5
    >>> print(c.max_size)
    5
    >>> str(c)
    'lorem'
    >>> c.max_size = 15
    >>> str(c)
    'lorem ipsum dol'
```

##### ConsoleLabel.__init__(self, txt, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, tag_beg='', tag_end='', color=False)
```python
def ConsoleLabel.__init__(self, txt, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, tag_beg='', tag_end='', color=False):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### ConsoleLabel.__len__(self)
```python
def ConsoleLabel.__len__(self):
```
> <br />
> Return len(self).<br />
> <br />
##### ConsoleLabel.__new__(cls, txt, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, *args, **kw)
```python
def ConsoleLabel.__new__(cls, txt, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, *args, **kw):
```
> <br />
> Create and return a new object.  See help(type) for accurate signature.<br />
> <br />
##### ConsoleString.__repr__(self)
```python
def ConsoleString.__repr__(self):
```
> <br />
> Return repr(self).<br />
> <br />
##### ConsoleString.__str__(self)
```python
def ConsoleString.__str__(self):
```
> <br />
> Return str(self).<br />
> <br />
##### ConsoleString.align_left(self)
```python
def ConsoleString.align_left(self):
```
> <br />
> Docstring empty<br />
> <br />
##### ConsoleString.align_right(self)
```python
def ConsoleString.align_right(self):
```
> <br />
> Docstring empty<br />
> <br />
#### ConsoleProgress()
```python
class ConsoleProgress(ConsoleString):
```

```
Use:
    >>> str(ConsoleProgress(12, 0.1))
    '[#.........]'
    >>> str(ConsoleProgress(12, 0.4))
    '[####......]'
    >>> str(ConsoleProgress(12, 1))
    '[##########]'
    >>> len(ConsoleProgress(12, 1))
    12
```

##### ConsoleProgress.__init__(self, size, ratio, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, tag_beg='[', tag_end=']', block='#', empty='.')
```python
def ConsoleProgress.__init__(self, size, ratio, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, tag_beg='[', tag_end=']', block='#', empty='.'):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### ConsoleProgress.__len__(self)
```python
def ConsoleProgress.__len__(self):
```
> <br />
> Return len(self).<br />
> <br />
##### ConsoleProgress.__new__(cls, size, ratio, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, tag_beg='[', tag_end=']', block='#', empty='.', *args, **kw)
```python
def ConsoleProgress.__new__(cls, size, ratio, frmt=<function ConsoleString.align_left at 0x7f3c63f5df28>, tag_beg='[', tag_end=']', block='#', empty='.', *args, **kw):
```
> <br />
> Create and return a new object.  See help(type) for accurate signature.<br />
> <br />
##### ConsoleString.__repr__(self)
```python
def ConsoleString.__repr__(self):
```
> <br />
> Return repr(self).<br />
> <br />
##### ConsoleString.__str__(self)
```python
def ConsoleString.__str__(self):
```
> <br />
> Return str(self).<br />
> <br />
##### ConsoleString.align_left(self)
```python
def ConsoleString.align_left(self):
```
> <br />
> Docstring empty<br />
> <br />
##### ConsoleString.align_right(self)
```python
def ConsoleString.align_right(self):
```
> <br />
> Docstring empty<br />
> <br />
#### ConsoleString()
```python
class ConsoleString(str):
```

```
Console string is a string to print (stdout) with
fixed size and console code
The console code is not calsulate in 'max_size'.

Why:
    It's usefull to manage the screen size.

Use:
    >>> c = ConsoleString("lorem ipsum")
    >>> # console code:
    >>> c.tag_beg = "["
    >>> c.tag_end="]"
    >>> for i in range(15): c.max_size = i ; str(c)
    '[]'
    '[l]'
    '[lo]'
    '[lor]'
    '[lore]'
    '[lorem]'
    '[lorem ]'
    '[lorem i]'
    '[lorem ip]'
    '[lorem ips]'
    '[lorem ipsu]'
    '[lorem ipsum]'
    '[lorem ipsum] '
    '[lorem ipsum]  '
    '[lorem ipsum]   '
    >>> len(c)
    11
    >>> c.text
    'lorem ipsum'
    >>> c = ConsoleString("lorem")
    >>> for i in range(9): c.max_size = i ; str(c)
    ''
    'l'
    'lo'
    'lor'
    'lore'
    'lorem'
    'lorem '
    'lorem  '
    'lorem   '
    >>> c = ConsoleString("lorem", ConsoleString.align_right)
    >>> for i in range(9): c.max_size = i ; str(c)
    ''
    'l'
    'lo'
    'lor'
    'lore'
    'lorem'
    ' lorem'
    '  lorem'
    '   lorem'
```

##### @Property: ConsoleString.max_size
```python
@property
def ConsoleString.max_size(self):
@max_size.setter
def ConsoleString.max_size(self, max_size):

```
> <br />
> @Property<br />
> <br />
##### @Property: ConsoleString.text
```python
@property
def ConsoleString.text(self):

```
> <br />
> @Property<br />
> <br />
##### ConsoleString.__init__(self, txt, frmt=None)
```python
def ConsoleString.__init__(self, txt, frmt=None):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### ConsoleString.__new__(cls, txt, *args, **kw)
```python
def ConsoleString.__new__(cls, txt, *args, **kw):
```
> <br />
> Create and return a new object.  See help(type) for accurate signature.<br />
> <br />
##### ConsoleString.__repr__(self)
```python
def ConsoleString.__repr__(self):
```
> <br />
> Return repr(self).<br />
> <br />
##### ConsoleString.__str__(self)
```python
def ConsoleString.__str__(self):
```
> <br />
> Return str(self).<br />
> <br />
##### ConsoleString.align_left(self)
```python
def ConsoleString.align_left(self):
```
> <br />
> Docstring empty<br />
> <br />
##### ConsoleString.align_right(self)
```python
def ConsoleString.align_right(self):
```
> <br />
> Docstring empty<br />
> <br />
#### ElapseTime()
```python
class ElapseTime(object):
```

```
Calculate elapse time.

Use:
    >>> import time
    >>> t = ElapseTime()
    >>> #oups...
    >>> t
    Traceback (most recent call last):
    ...
    RuntimeError: start before...
    >>> t.start()
    >>> time.sleep(1)
    >>> t
    0:00:01
    >>> time.sleep(1)
    >>> t
    0:00:02
    >>> str(t)
    '0:00:02'
```

##### ElapseTime.__init__(self)
```python
def ElapseTime.__init__(self):
```
> <br />
> Init the default values<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  obj<br />
> <br />
##### ElapseTime.__repr__(self)
```python
def ElapseTime.__repr__(self):
```
> <br />
> Provides the string<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
##### ElapseTime.__str__(self)
```python
def ElapseTime.__str__(self):
```
> <br />
> Call repr<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
##### ElapseTime.start(self)
```python
def ElapseTime.start(self):
```
> <br />
> Store the current timestamp in self.__start_time<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
#### MultiThread()
```python
class MultiThread(Thread):
```

```
Use:
    >>> def mytask(): print("lorem ipsum dolor sit amet consectetur")
    >>> mthr = MultiThread(mytask, 0.25)
    >>> mthr.start() ; print("other task");time.sleep(1) ; mthr.stop()
    lorem ipsum dolor sit amet consectetur
    other task
    lorem ipsum dolor sit amet consectetur
    lorem ipsum dolor sit amet consectetur
    lorem ipsum dolor sit amet consectetur
    lorem ipsum dolor sit amet consectetur
```

##### @Property: MultiThread.func
```python
@property
def MultiThread.func(self):

```
> <br />
> @Property<br />
> <br />
##### MultiThread.__init__(self, func, elapse)
```python
def MultiThread.__init__(self, func, elapse):
```
> <br />
> <b>This constructor should always be called with keyword arguments. Arguments are:</b><br />
> <br />
> *group* should be None; reserved for future extension when a ThreadGroup<br />
> class is implemented.<br />
> <br />
> *target* is the callable object to be invoked by the run()<br />
> method. Defaults to None, meaning nothing is called.<br />
> <br />
> *name* is the thread name. By default, a unique name is constructed of<br />
> the form "Thread-N" where N is a small decimal number.<br />
> <br />
> *args* is the argument tuple for the target invocation. Defaults to ().<br />
> <br />
> *kwargs* is a dictionary of keyword arguments for the target<br />
> invocation. Defaults to {}.<br />
> <br />
> If a subclass overrides the constructor, it must make sure to invoke<br />
> the base class constructor (Thread.__init__()) before doing anything<br />
> else to the thread.<br />
> <br />
##### MultiThread.run(self)
```python
def MultiThread.run(self):
```
> <br />
> Method representing the thread's activity.<br />
> <br />
> You may override this method in a subclass. The standard run() method<br />
> invokes the callable object passed to the object's constructor as the<br />
> target argument, if any, with sequential and keyword arguments taken<br />
> from the args and kwargs arguments, respectively.<br />
> <br />
##### MultiThread.stop(self)
```python
def MultiThread.stop(self):
```
> <br />
> Docstring empty<br />
> <br />
##### Thread.__repr__(self)
```python
def Thread.__repr__(self):
```
> <br />
> Return repr(self).<br />
> <br />
##### Thread._bootstrap(self)
```python
def Thread._bootstrap(self):
```
> <br />
> Docstring empty<br />
> <br />
##### Thread._bootstrap_inner(self)
```python
def Thread._bootstrap_inner(self):
```
> <br />
> Docstring empty<br />
> <br />
##### Thread._delete(self)
```python
def Thread._delete(self):
```
> <br />
> Remove current thread from the dict of currently running threads.<br />
> <br />
##### Thread._reset_internal_locks(self, is_alive)
```python
def Thread._reset_internal_locks(self, is_alive):
```
> <br />
> Docstring empty<br />
> <br />
##### Thread._set_ident(self)
```python
def Thread._set_ident(self):
```
> <br />
> Docstring empty<br />
> <br />
##### Thread._set_tstate_lock(self)
```python
def Thread._set_tstate_lock(self):
```
> <br />
> Set a lock object which will be released by the interpreter when<br />
> the underlying thread state (see pystate.h) gets deleted.<br />
> <br />
##### Thread._stop(self)
```python
def Thread._stop(self):
```
> <br />
> Docstring empty<br />
> <br />
##### Thread._wait_for_tstate_lock(self, block=True, timeout=-1)
```python
def Thread._wait_for_tstate_lock(self, block=True, timeout=-1):
```
> <br />
> Docstring empty<br />
> <br />
##### Thread.getName(self)
```python
def Thread.getName(self):
```
> <br />
> Docstring empty<br />
> <br />
##### Thread.isDaemon(self)
```python
def Thread.isDaemon(self):
```
> <br />
> Docstring empty<br />
> <br />
##### Thread.is_alive(self)
```python
def Thread.is_alive(self):
```
> <br />
> Return whether the thread is alive.<br />
> <br />
> This method returns True just before the run() method starts until just<br />
> after the run() method terminates. The module function enumerate()<br />
> returns a list of all alive threads.<br />
> <br />
##### Thread.join(self, timeout=None)
```python
def Thread.join(self, timeout=None):
```
> <br />
> Wait until the thread terminates.<br />
> <br />
> This blocks the calling thread until the thread whose join() method is<br />
> called terminates -- either normally or through an unhandled exception<br />
> or until the optional timeout occurs.<br />
> <br />
> When the timeout argument is present and not None, it should be a<br />
> floating point number specifying a timeout for the operation in seconds<br />
> (or fractions thereof). As join() always returns None, you must call<br />
> isAlive() after join() to decide whether a timeout happened -- if the<br />
> thread is still alive, the join() call timed out.<br />
> <br />
> When the timeout argument is not present or None, the operation will<br />
> block until the thread terminates.<br />
> <br />
> A thread can be join()ed many times.<br />
> <br />
> join() raises a RuntimeError if an attempt is made to join the current<br />
> thread as that would cause a deadlock. It is also an error to join() a<br />
> thread before it has been started and attempts to do so raises the same<br />
> exception.<br />
> <br />
##### Thread.setDaemon(self, daemonic)
```python
def Thread.setDaemon(self, daemonic):
```
> <br />
> Docstring empty<br />
> <br />
##### Thread.setName(self, name)
```python
def Thread.setName(self, name):
```
> <br />
> Docstring empty<br />
> <br />
##### Thread.start(self)
```python
def Thread.start(self):
```
> <br />
> Start the thread's activity.<br />
> <br />
> It must be called at most once per thread object. It arranges for the<br />
> object's run() method to be invoked in a separate thread of control.<br />
> <br />
> This method will raise a RuntimeError if called more than once on the<br />
> same thread object.<br />
> <br />
#### Percent()
```python
class Percent(float):
```

```
Calc

Use:
    >>> #oups 1
    >>> p = Percent(0)
    Traceback (most recent call last):
    ...
    ValueError: max_value cant be 0
    >>> #oups 3
    >>> p = Percent(10)
    >>> p.ratio = 10
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> #correct usage:
    >>> p = Percent(10)
    >>> p.value = 2
    >>> p.value
    2
    >>> p
    20.0%
    >>> str(p)
    '20.0%'
    >>> p.ratio
    0.2
    >>> p = Percent(8)
    >>> for i in range(9): p.value = i ; print("{}-{}".format(p, p.ratio))
    0.0%-0.0
    12.5%-0.125
    25.0%-0.25
    37.5%-0.375
    50.0%-0.5
    62.5%-0.625
    75.0%-0.75
    87.5%-0.875
    100.%-1.0
```

##### @Property: Percent.max_value
```python
@property
def Percent.max_value(self):

```
> <br />
> @Property<br />
> <br />
##### @Property: Percent.ratio
```python
@property
def Percent.ratio(self):

```
> <br />
> @Property<br />
> <br />
##### @Property: Percent.value
```python
@property
def Percent.value(self):
@value.setter
def Percent.value(self, value):

```
> <br />
> @Property<br />
> <br />
##### Percent.__init__(self, max_value)
```python
def Percent.__init__(self, max_value):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### Percent.__repr__(self)
```python
def Percent.__repr__(self):
```
> <br />
> percent = str((self.get_percent() * 100))[0:4]<br />
> return " " * (5 - len(percent)) + percent<br />
> <br />
##### Percent.__str__(self)
```python
def Percent.__str__(self):
```
> <br />
> Return str(self).<br />
> <br />
#### SmoothProgressBar()
```python
class SmoothProgressBar(object):
```

```
Docstring empty
```

##### @Property: SmoothProgressBar.msg
```python
@property
def SmoothProgressBar.msg(self):
@msg.setter
def SmoothProgressBar.msg(self, msg):

```
> <br />
> @Property<br />
> <br />
##### SmoothProgressBar.__init__(self, enable_elapse=True, enable_msg=True)
```python
def SmoothProgressBar.__init__(self, enable_elapse=True, enable_msg=True):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### SmoothProgressBar.__refresh(self)
```python
def SmoothProgressBar.__refresh(self):
```
> <br />
> Docstring empty<br />
> <br />
##### SmoothProgressBar.start(self, max_value)
```python
def SmoothProgressBar.start(self, max_value):
```
> <br />
> Docstring empty<br />
> <br />
##### SmoothProgressBar.stop(self)
```python
def SmoothProgressBar.stop(self):
```
> <br />
> Docstring empty<br />
> <br />
##### SmoothProgressBar.update(self, value, msg='')
```python
def SmoothProgressBar.update(self, value, msg=''):
```
> <br />
> Docstring empty<br />
> <br />
