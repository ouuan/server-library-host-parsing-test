#!/bin/bash

set -euo pipefail
cd "$(dirname "$0")"

php -S 127.0.0.1:3006 index.php
