#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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

"""

import smoothprogressbar.__about__
from smoothprogressbar.progressbar import *
