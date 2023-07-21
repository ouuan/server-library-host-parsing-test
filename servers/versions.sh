#!/bin/bash

set -euo pipefail

echo Node
node --version
echo

echo Python
python --version
echo

echo Django
python -m django --version
echo

echo Rust
cargo --version
echo

echo Go
go version
echo

echo Ruby
ruby --version
gem list sinatra webrick
echo

echo PHP
php --version
