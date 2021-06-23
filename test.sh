#!/bin/bash
# Testing the decorator can't be done (to my knowledge) very easily in regular testing frameworks,
#   since it by definition involves two executions. So, we have a shell script instead, for this "integration" test.

mkdir test_int_noarg
mkdir test_object_noarg
mkdir test_int_arg
mkdir test_object_arg

python ./integration_test.py 1
python ./integration_test.py 2

rm -rf test_int_noarg
rm -rf test_object_noarg
rm -rf test_int_arg
rm -rf test_object_arg