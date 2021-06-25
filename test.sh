#!/bin/bash
# Testing the decorator can't be done (to my knowledge) very easily in regular testing frameworks,
#   since it by definition involves two executions. So, we have a shell script instead, for this "integration" test.

mkdir cache_dir

python ./integration_test.py 1
python ./integration_test.py 2

rm -rf cache_dir