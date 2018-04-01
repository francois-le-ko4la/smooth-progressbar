# smooth-progressbar
## Description:

This package provide a simple progress bar.

The following files comprise the `smooth-progressbar` package:
* `LICENSE`: The license file. `smooth-progressbar` is released under the terms
of the GNU General Public License (GPL), version 3.
* `README.md`: This readme file.
* `Makefile`: Generic management tasks.
* `setup.py`: Package and distribution management.
* `setup.cfg`: The setuptools setup file.
* `tests/test_smooth_progressbar.py`: Test.

The package contents itself are in the `smooth_progressbar` directory:
* `__ init __`.py: Initialization file for the Python package.
* `smooth_progressbar/smooth_progressbar.py` : The code of interest.

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
from smooth_progressbar import SmoothProgressBar
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

## Note:

This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Dev docstring
### Class SmoothProgressBar:
This Class provides a progressbar

#### Function SmoothProgressBar.__get_bar(self):

```
This function provides the string to print the progress and
informations

Call __get_percentbar(), self.__get_infosbar and provides a complete
progress bar

Args:
    None

Returns:
    string: Processing (70.0%): |///////////////     | 0:00:01 | task 1
```

#### Function SmoothProgressBar.__get_elapse(self):

```
This function provides elapse time between start() and now.

self.__update_time-self.__start_time

Args:
    None

Returns:
    datetime object
```

#### Function SmoothProgressBar.__get_infosbar(self):

```
This function provides an information to print.

Provides : Elapse and description.

Args:
    None

Returns:
    string: "{elapse} | {description}"
```

#### Function SmoothProgressBar.__get_percentbar(self):

```
This function provides the string to print the progress

Provides progress and bar according to the screen size.

Args:
    None

Returns:
    string: Processing (70.0%): |///////////////     |
```

#### Function SmoothProgressBar.__refresh(self):

```
This function refresh the progress bar

Call __get_bar(), print the string, call Timer functions to recall

Args:
    None

Returns:
    None
```

#### Function SmoothProgressBar.__set_percent(self):

```
This function provides current percent.

current_percent=round(self.__current_value/float(self.__max_value), 1)

Args:
    None

Returns:
    None
```

#### Function SmoothProgressBar.__init__(self):

```
Init the smoothProgressBar Class
This function define attributes.

Args:
    None

Attributes:
    self.__interval (float) : refresh time
    self.__rows (float): screen size
    self.__columns (float): screen size
    self.__text (str): text to print
    self.__bar_length (int): progressbar size
    self.__start_time (datetime): start time
    self.__update_time (datetime): update time
    self.__max_value (int): maximum value (100%)
    self.__description (str):
    self.__current_value (int):
    self.__current_percent (float)
    self.__is_running (bool)
    self.__is_updated (bool)
    self.__previous_percent (str)

Returns:
    obj
```

#### Function SmoothProgressBar.start(self, max_value):

```
This function start the progress bar

Test if the progress is already running, set _startTime,
call Timer functions to refresh

Args:
    max_value (int): the value at 100%.

Returns:
    None
```

#### Function SmoothProgressBar.stop(self):

```
This function stop the progress bar.

Args:
    None

Results:
    None
```

#### Function SmoothProgressBar.update(self, current_value, description=None):

```
This function update currentValue, description, __update_time
and call __set_percent().

Args:
    current_value (int): current value
    description (string): current description

Returns:
    None
```


