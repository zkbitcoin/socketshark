#!/bin/bash
source .venv/bin/activate
PYTHONPATH=. .venv/bin/socketshark -c config > run.out 2>&1  </dev/null &
#PYTHONPATH=. .venv/bin/socketshark -c config 
