#!/bin/bash

set -euo pipefail
cd "$(dirname "$0")"

./manage.py runserver 3002
