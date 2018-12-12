#!/bin/bash

CONFIG_PATH=/data/options.json

version=$(node -v)
echo "[fbx-addon] Checking node version : $version"

echo "[fbx-addon] Generating freebox plugin configuration file..."
python3 config_builder.py "$CONFIG_PATH"

echo "[fbx-addon] Starting Freebox Assistant Config Add-on..."
node index.js
