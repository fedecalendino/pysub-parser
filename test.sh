#!/usr/bin/env bash

# Activating virtualenv
source $(find . -name 'activate')

# Running tests with coverage
coverage run ./test.py
result="$?"

echo ''

# Printing report
coverage report --include="pysubparser/*"

if [[ $1 == "-html" ]];
then
    # Generating html report
    coverage html  --include="pysubparser/*" -d coverage

    # Opening html report
    open ./coverage/index.html
else
    rm -rf coverage
fi

# Deactivating virtualenv
deactivate

echo ''
exit ${result}
