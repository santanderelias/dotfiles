#!/usr/bin/env bash
DIR="$HOME/Pictures/Screenshots"
FILE="$DIR/screenshot_$(date +'%Y-%m-%d_%H-%M-%S').png"
grim -g "$(slurp)" - | tee "$FILE" | wl-copy
