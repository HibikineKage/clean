#!/bin/sh
script_dir=$(cd $(dirname $0); pwd)
python3 $script_dir/clean.py "$@"