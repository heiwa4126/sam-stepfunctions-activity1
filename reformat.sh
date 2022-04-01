#!/bin/sh -ue

# reformat shell scripts
find . -name \*.sh \
  -not -path './.aws-sam/*' \
  -exec shfmt -i 2 -w {} \+

# reformat python scripts
find . -name \*.py \
  -not -path './.aws-sam/*' \
  -exec black {} \+ \
  -exec isort {} \+
