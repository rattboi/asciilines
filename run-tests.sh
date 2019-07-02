#!/bin/bash

somefail=0

for i in $(find tests/ -name '*.tvg' | sort); do
  diff <(python asciilines.py $i) <(cat ${i%.*}.out) > /dev/null
  if [[ $? == 0 ]]; then
    result="PASS"
  else
    result="FAIL"
    somefail=1
  fi
  printf "Test %s:\t%s\n" "$i" "$result"
done

exit $somefail
