#!/bin/bash
# Launcher script for Gesture Meme Tracker
# This ensures we use the correct Python interpreter

PYTHON_PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin/python3"

echo "Starting Gesture Meme Tracker..."
echo "Using Python: $PYTHON_PATH"
echo ""

$PYTHON_PATH gesture_meme_tracker.py

