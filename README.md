# smooth-progressbar.
[![badge](https://forthebadge.com/images/badges/made-with-python.svg)]()
![](./doc/pycodestyle-passing.svg)
![](./doc/pylint-passing.svg)
![](./doc/mypy-passing.svg)


## Description:

![](./doc/demo.gif)
This progress bar is a tool that allows users to monitor the progress of
long-running tasks, such as data loading and cleaning, and make sure that 
the task is progressing as expected.
The progress bar can also be set to display a message or a comment alongside
the progress, providing more information about the current stage of the task.
This can be especially useful for debugging or troubleshooting. The library
includes examples, which can be found in the tests folder, that demonstrate 
how to use the progress bar in different contexts.
Additionally, the size of the progress bar is calculated according to the
terminal environment, so it will always fit the available space and be easy
to read. This feature makes it easy to integrate the progress bar into
different environments, whether you're working on a local machine or a 
remote server. Overall, this Python progress bar project is a useful tool 
for  anyone who wants to track the progress of a task or process, and make 
sure that it's running smoothly.

## Use:
```python
import time
from smoothprogressbar import SmoothProgressBar
my_progressbar = SmoothProgressBar()
my_progressbar.start(10)

for i in range(1, 11):
    my_progressbar.update(i, "task "+str(i))
    time.sleep(2)
my_progressbar.stop()
```

## Result:

    Processing (10.0%): |//                  | 0:00:01 | task 1
    Processing (20.0%): |////                | 0:00:03 | task 2
    Processing (30.0%): |//////              | 0:00:05 | task 3
    ...

# Setup:
- User:

Get the package:
```shell
git clone https://github.com/francois-le-ko4la/smooth-progressbar.git
```
Enter in the directory:
```shell
cd smooth-progressbar
```
Install with make on Linux/Unix/MacOS or use pip3 otherwise:
```shell
make install
```

- Dev environment:

Get the package:
```shell
git clone https://github.com/francois-le-ko4la/smooth-progressbar.git
```
Enter in the directory:
```shell
cd smooth-progressbar
```
Create your environment with all dev prerequisites and install the package:
```shell
make venv
source venv/bin/activate
make dev
```

# Test:
This module has been tested and validated on Ubuntu.
Test is available if you set up the package with dev environment.
```shell
make test
```

# License:
This package is distributed under the [GPLv3 license](./LICENSE)

# Todo:
- [X] Create the project
- [X] Write code and tests
- [X] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [X] Validate features
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [X] Clean & last check
- [X] Release

# Dev Notes
```mermaid
classDiagram
  class TextIOWrapper {
    close()
    detach()
    fileno()
    flush()
    isatty()
    read()
    readable()
    readline()
    readlines()
    reconfigure()
    seek()
    seekable()
    tell()
    truncate()
    writable()
    write()
    writelines()
  }
  class _IOBase {
    close()
    fileno()
    flush()
    isatty()
    readable()
    readline()
    readlines()
    seek()
    seekable()
    tell()
    truncate()
    writable()
    writelines()
  }
  class _TextIOBase {
    close()
    detach()
    fileno()
    flush()
    isatty()
    read()
    readable()
    readline()
    readlines()
    seek()
    seekable()
    tell()
    truncate()
    writable()
    write()
    writelines()
  }
  class RLock {
    acquire()
    release()
  }
  class deque {
    iterable : list
    maxlen : int
    append(x)
    appendleft(x)
    clear()
    copy()
    count(x)
    extend(iterable)
    extendleft(iterable)
    index(x, start, end)
    insert(i, x)
    pop()
    popleft()
    remove(value)
    reverse()
    rotate(n)
  }
  class date {
    day
    month
    year
    ctime()
    fromisocalendar(year, week, day)
    fromisoformat(date_string)
    fromordinal(n)
    fromtimestamp(t)
    isocalendar()
    isoformat()
    isoweekday()
    replace(year, month, day)
    strftime(fmt)
    timetuple()
    today()
    toordinal()
    weekday()
  }
  class datetime {
    fold
    hour
    microsecond
    minute
    second
    tzinfo
    astimezone(tz)
    combine(date, time, tzinfo)
    ctime()
    date()
    dst()
    fromisoformat(date_string)
    fromtimestamp(t, tz)
    isoformat(sep, timespec)
    now(tz)
    replace(year, month, day, hour, minute, second, microsecond, tzinfo)
    strptime(date_string, format)
    time()
    timestamp()
    timetuple()
    timetz()
    tzname()
    utcfromtimestamp(t)
    utcnow()
    utcoffset()
    utctimetuple()
  }
  class Console {
    size
    addmsg(msg)
    addtab()
    emptyline()
    goback()
    newline()
    print()
  }
  class ConsolePrgBr {
    progress_label : str
    size_widgt_label_label : int
    size_widgt_percent : int
    get()
    update(size, percent, msg, elapse)
  }
  class ConsoleProgress {
    max_size
    tag_beg : str
    tag_end : str
    text
    update(size, ratio)
  }
  class ConsoleString {
    current_text_size
    enable
    max_size
    max_size : int
    max_text_size
    tag_beg : str
    tag_end : str
    tag_size
    text
    align_left()
    align_right()
    update(text, max_size, tag_beg, tag_end)
  }
  class ElapseTime {
    start()
  }
  class MultiThread {
    func
    run()
    stop()
  }
  class Percent {
    part
    part
    value
    whole
  }
  class SmoothProgressBar {
    msg
    start(max_value)
    stop()
    update(value, msg)
  }
  class Condition {
    acquire
    release
    notify(n)
    notifyAll()
    notify_all()
    wait(timeout)
    wait_for(predicate, timeout)
  }
  class Event {
    clear()
    isSet()
    is_set()
    set()
    wait(timeout)
  }
  class Thread {
    daemon
    daemon
    ident
    name
    name
    native_id
    getName()
    isDaemon()
    is_alive()
    join(timeout)
    run()
    setDaemon(daemonic)
    setName(name)
    start()
  }
  class Timer {
    args : NoneType, list
    finished
    function
    interval
    kwargs : dict, NoneType
    cancel()
    run()
  }
  class _RLock {
    acquire(blocking, timeout)
    release()
  }
  class lock {
    acquire(blocking, timeout)
    locked()
    release()
  }
  TextIOWrapper --|> _TextIOBase
  _TextIOBase --|> _IOBase
  datetime --|> date
  ConsoleProgress --|> ConsoleString
  MultiThread --|> Thread
  Timer --|> Thread
  TextIOWrapper --* Thread : _stderr
  RLock --* Condition : _lock
  deque --* Condition : _waiters
  datetime --* ElapseTime : __start_time
  datetime --* ElapseTime : __update_time
  Console --* SmoothProgressBar : __console
  ConsolePrgBr --* SmoothProgressBar : __prgbr
  ConsoleProgress --* ConsolePrgBr : __widgt_progress
  ConsoleString --* ConsolePrgBr : __widgt_label
  ConsoleString --* ConsolePrgBr : __widgt_percent
  ConsoleString --* ConsolePrgBr : __widgt_elapse
  ConsoleString --* ConsolePrgBr : __widgt_msg
  ElapseTime --* SmoothProgressBar : __elapse
  MultiThread --* SmoothProgressBar : __mthr
  Percent --* SmoothProgressBar : __percent
  Condition --* Event : _cond
  Event --* Thread : _started
  Event --* Timer : finished
  Timer --* MultiThread : __timer
  _RLock --* Condition : _lock
  lock --* SmoothProgressBar : __lock
```

