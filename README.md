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

### Runtime

```
python-3.6.x

```
### UML Diagram
![alt text](pictures/classes_smoothprogressbar.png)

### Objects
[Console()](#console)<br />
[@Property Console.size](#property-consolesize)<br />
[Console.addmsg()](#consoleaddmsg)<br />
[Console.emptyline()](#consoleemptyline)<br />
[Console.addtab()](#consoleaddtab)<br />
[Console.goback()](#consolegoback)<br />
[Console.newline()](#consolenewline)<br />
[Console.print()](#consoleprint)<br />
[ConsolePrgBr()](#consoleprgbr)<br />
[ConsolePrgBr.update()](#consoleprgbrupdate)<br />
[ConsolePrgBr.get()](#consoleprgbrget)<br />
[ConsoleProgress()](#consoleprogress)<br />
[ConsoleProgress.update()](#consoleprogressupdate)<br />
[ConsoleString()](#consolestring)<br />
[@Property ConsoleString.enable](#property-consolestringenable)<br />
[@Property ConsoleString.max_size](#property-consolestringmax_size)<br />
[@Property ConsoleString.tag_size](#property-consolestringtag_size)<br />
[@Property ConsoleString.max_text_size](#property-consolestringmax_text_size)<br />
[@Property ConsoleString.current_text_size](#property-consolestringcurrent_text_size)<br />
[ConsoleString.align_left()](#consolestringalign_left)<br />
[ConsoleString.align_right()](#consolestringalign_right)<br />
[ConsoleString.update()](#consolestringupdate)<br />
[ElapseTime()](#elapsetime)<br />
[ElapseTime.start()](#elapsetimestart)<br />
[MultiThread()](#multithread)<br />
[@Property MultiThread.func](#property-multithreadfunc)<br />
[MultiThread.run()](#multithreadrun)<br />
[MultiThread.stop()](#multithreadstop)<br />
[Percent()](#percent)<br />
[@Property Percent.whole](#property-percentwhole)<br />
[@Property Percent.part](#property-percentpart)<br />
[@Property Percent.value](#property-percentvalue)<br />
[SmoothProgressBar()](#smoothprogressbar)<br />
[@Property SmoothProgressBar.msg](#property-smoothprogressbarmsg)<br />
[SmoothProgressBar.start()](#smoothprogressbarstart)<br />
[SmoothProgressBar.stop()](#smoothprogressbarstop)<br />
[SmoothProgressBar.update()](#smoothprogressbarupdate)<br />

#### Console()
```python
class Console(object):
```

```
This Class provides a simple way to manage the screen

Use:
    >>> c = Console()
    >>> c.addmsg("lorem ipsum dolor").print()
    lorem ipsum dolor
    >>> c.addmsg("lorem ipsum dolor").newline().addmsg("LOREM").print()
    lorem ipsum dolor
    LOREM
```

##### @Property Console.size
```python
@property
def Console.size(self):
```
> <br />
> screen size (columns)<br />
> <br />
##### Console.addmsg()
```python

def Console.addmsg(self, msg):
```
> <br />
> store a message<br />
> <br />
##### Console.emptyline()
```python

def Console.emptyline(self):
```
> <br />
> store an empty line<br />
> <br />
##### Console.addtab()
```python

def Console.addtab(self):
```
> <br />
> store a tab<br />
> <br />
##### Console.goback()
```python

def Console.goback(self):
```
> <br />
> store a goback caracter<br />
> <br />
##### Console.newline()
```python

def Console.newline(self):
```
> <br />
> store a new line<br />
> <br />
##### Console.print()
```python

def Console.print(self):
```
> <br />
> print the buffer<br />
> <br />
#### ConsolePrgBr()
```python
class ConsolePrgBr(object):
```

```
This class print all components according to parameters.

Use:
>>> from smoothprogressbar.percent import Percent
>>> from smoothprogressbar.elapse import ElapseTime
>>> size = 40
>>> percent = Percent(10)
>>> percent.part = 2
>>> msg = "lorem ipsum dolor sit amet consectetur adipiscing elit"
>>> elapse = ElapseTime()
>>> elapse.start()
>>> prgbr = ConsolePrgBr(debug=True)
>>> prgbr.update(size, percent, msg, str(elapse)).get()
'Processing: [ 20.0%] [...] 0:00:00 lorem'
>>> size = 70
>>> prgbr = ConsolePrgBr(debug=True)
>>> prgbr.update(size, percent, msg, str(elapse)).get()
'Processing: [ 20.0%] [###...............] 0:00:00 lorem ipsum dolor si'
>>> prgbr = ConsolePrgBr(enable_elapse=False, enable_msg=False, debug=True)
>>> prgbr.update(size, percent, msg, str(elapse)).get()
'Processing: [ 20.0%] [#########......................................]'
>>> prgbr = ConsolePrgBr(enable_elapse=True, enable_msg=False, debug=True)
>>> prgbr.update(size, percent, msg, str(elapse)).get()
'Processing: [ 20.0%] [#######................................] 0:00:00'
>>> prgbr = ConsolePrgBr(enable_elapse=False, enable_msg=True, debug=True)
>>> prgbr.update(size, percent, msg, str(elapse)).get()
'Processing: [ 20.0%] [####..................] lorem ipsum dolor sit am'
```

##### ConsolePrgBr.update()
```python

def ConsolePrgBr.update(self, size, percent, msg=, elapse=):
```
> <br />
> Update() the progress bar<br />
> <br />
##### ConsolePrgBr.get()
```python

def ConsolePrgBr.get(self):
```
> <br />
> Get the string<br />
> <br />
#### ConsoleProgress()
```python
class ConsoleProgress(ConsoleString):
```

```
Use:
    >>> c = ConsoleProgress()
    >>> str(c.update(12, 0.1))
    '[#.........]'
    >>> str(c.update(12, 0.4))
    '[####......]'
    >>> str(c.update(12, 1))
    '[##########]'
    >>> len(c.update(12, 1))
    12
```

##### ConsoleProgress.update()
```python

def ConsoleProgress.update(self, size, ratio):
```
> <br />
> None<br />
> <br />
#### ConsoleString()
```python
class ConsoleString(object):
```

```
Console string is a string to print (stdout) with
fixed size.

'[XXXXXXXXX ]                  '
 -          -                    : tag size
  ----------                     : text size
|------------------------------| : max size

Why:
    It's usefull to manage the screen size.

Use:
    >>> #oups
    >>> c = ConsoleString("lorem", max_size="3")
    Traceback (most recent call last):
    ...
    TypeError: invalid literal for int() with base 10: '3'
    >>> c = ConsoleString("lorem", max_size=3)
    >>> c
    lor
    >>> c = ConsoleString("lorem")
    >>> # tag
    >>> c.tag_beg = "["
    >>> c.tag_end="]"
    >>> for i in range(9): c.max_size = i ; str(c)
    ''
    '['
    '[]'
    '[l]'
    '[lo]'
    '[lor]'
    '[lore]'
    '[lorem]'
    '[lorem] '
    >>> len(c)
    8
    >>> c.text
    'lorem'
    >>> c = ConsoleString("lorem")
    >>> for i in range(9): c.max_size = i ; str(c.align_left())
    ''
    'l'
    'lo'
    'lor'
    'lore'
    'lorem'
    'lorem '
    'lorem  '
    'lorem   '
    >>> c = ConsoleString("lorem")
    >>> for i in range(9): c.max_size = i ; str(c.align_right())
    ''
    'l'
    'lo'
    'lor'
    'lore'
    'lorem'
    ' lorem'
    '  lorem'
    '   lorem'
    >>> txt = "lorem ipsum dolor sit amet consectetur adipiscing elit"
    >>> str(c.update(text=txt, max_size=15, tag_beg="*** "))
    '*** lorem ipsum'
```

##### @Property ConsoleString.enable
```python
@property
def ConsoleString.enable(self):
```
> <br />
> Enable object<br />
> <br />
##### @Property ConsoleString.max_size
```python
@property
def ConsoleString.max_size(self):
```
> <br />
> string max size<br />
> <br />
##### @Property ConsoleString.tag_size
```python
@property
def ConsoleString.tag_size(self):
```
> <br />
> Tag size<br />
> <br />
##### @Property ConsoleString.max_text_size
```python
@property
def ConsoleString.max_text_size(self):
```
> <br />
> Tag size setter<br />
> <br />
##### @Property ConsoleString.current_text_size
```python
@property
def ConsoleString.current_text_size(self):
```
> <br />
> Text size according to text_size and max_text_size<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  min(text_size, len(text))<br />
> <br />
##### ConsoleString.align_left()
```python

def ConsoleString.align_left(self):
```
> <br />
> Apply 'align-left' to the string<br />
> <br />
##### ConsoleString.align_right()
```python

def ConsoleString.align_right(self):
```
> <br />
> Apply 'align-right' to the string<br />
> <br />
##### ConsoleString.update()
```python

def ConsoleString.update(self, text=None, max_size=None, tag_beg=None, tag_end=None):
```
> <br />
> update the string<br />
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

##### ElapseTime.start()
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
A class that represents a thread of control.
This class subclassed Thread class :
    class Thread(builtins.object)

We specify the activity by passing a callable object to the constructor.

Use:
    >>> import time
    >>> def mytask(): print("lorem ipsum dolor sit amet consectetur")
    >>> mthr = MultiThread(mytask, 0.1)
    >>> mthr.start() ; print("other task");time.sleep(0.3) ; mthr.stop()
    lorem ipsum dolor sit amet consectetur
    other task
    lorem ipsum dolor sit amet consectetur
    lorem ipsum dolor sit amet consectetur
```

##### @Property MultiThread.func
```python
@property
def MultiThread.func(self):
```
> <br />
> Returns the callable object defined by Thread constructor.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  callable object<br />
> <br />
##### MultiThread.run()
```python

def MultiThread.run(self):
```
> <br />
> Method (override) representing the thread's activity.<br />
> This method will raise a RuntimeError if called more than once on the<br />
> same thread object.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None.<br />
> <br />
##### MultiThread.stop()
```python

def MultiThread.stop(self):
```
> <br />
> Wait until the thread terminates.<br />
> This blocks the calling thread until the thread whose join() method is<br />
> called terminates -- either normally or through an unhandled exception.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None.<br />
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
    ValueError: Percent: "whole" cant be 0
    >>> #oups 2
    >>> p = Percent("az")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'az'
    >>> #oups 3
    >>> p = Percent(10)
    >>> p.value = 10
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> #oups 4
    >>> p.part = "rt"
    Traceback (most recent call last):
    ...
    TypeError: invalid literal for int() with base 10: 'rt'
    >>> #correct usage:
    >>> p = Percent(10)
    >>> p.part = 2
    >>> p.part
    2
    >>> p
     20.0%
    >>> str(p)
    ' 20.0%'
    >>> p.value
    0.2
    >>> p = Percent(8)
    >>> for i in range(9): p.part = i ; print("{}-{}".format(p, p.value))
      0.0%-0.0
     12.5%-0.125
     25.0%-0.25
     37.5%-0.375
     50.0%-0.5
     62.5%-0.625
     75.0%-0.75
     87.5%-0.875
    100.0%-1.0
```

##### @Property Percent.whole
```python
@property
def Percent.whole(self):
```
> <br />
> X% = 100 * (part / whole)<br />
> <br />
##### @Property Percent.part
```python
@property
def Percent.part(self):
```
> <br />
> X% = 100 * (part / whole)<br />
> <br />
##### @Property Percent.value
```python
@property
def Percent.value(self):
```
> <br />
> value = X%/100 = part / whole<br />
> <br />
#### SmoothProgressBar()
```python
class SmoothProgressBar(object):
```

```
This class use all others component to manage the progressbar.

Use:
```

##### @Property SmoothProgressBar.msg
```python
@property
def SmoothProgressBar.msg(self):
```
> <br />
> Message<br />
> <br />
##### SmoothProgressBar.start()
```python

def SmoothProgressBar.start(self, max_value):
```
> <br />
> start the progress bar<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  init percent(), screen size, elapse & multithreading<br />
> <br />
##### SmoothProgressBar.stop()
```python

def SmoothProgressBar.stop(self):
```
> <br />
> stop the progress bar<br />
> <br />
##### SmoothProgressBar.update()
```python

def SmoothProgressBar.update(self, value, msg=):
```
> <br />
> update the progressbar<br />
> <br />

