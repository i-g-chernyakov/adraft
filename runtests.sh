#!/bin/bash

#
# Run as follows:
#   ./runtests.sh
#   ./runtests.sh novenv
#

if [[ $1w != 'novenv' ]]; then

    echo "Trying to use virtual environment adraft "

    workon adraft

else

    echo "Not using virtual environment ..."

fi

py.test
