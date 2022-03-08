#!/bin/bash

filename=$1

firefox --headless --screenshot --window-size=600,448 $filename
../image.py screenshot.png
