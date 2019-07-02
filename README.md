[![Build Status](https://travis-ci.com/rattboi/asciilines.svg?branch=master)](https://travis-ci.com/rattboi/asciilines)

# asciilines
Copyright (c) 2019 Bradon Kanyid

## CS561 Mini-Project

This program is accepts a single .tvg file argument, which it then renders as ASCII on standard output

The TVG format is the "Text Vector Format". It defines a canvas size, and some horizontal/vertical lines to render in order on that canvas.

## Build and Run

Assuming you have python 3.7, you should be able to run this program just by running:

```
python3.7 asciilines.py tests/<testfile.tvg>
```

## Other Pertinent Information

Test cases can be found in tests/

## Continuous Integration

run-tests.sh contains a simple script to compare the output of asciiline tests against known-good output. 

Travis CI is used to auto-run these tests on every commit. 

You can see the most current build / test results [here](https://travis-ci.com/rattboi/asciilines)

## License

This program is licensed under the "MIT License".  Please
see the file `LICENSE` in the source distribution of this
software for license terms.
