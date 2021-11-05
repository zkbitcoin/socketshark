#!/bin/bash
source .venv/bin/activate
PYTHONPATH=. .venv/bin/socketshark -c config
