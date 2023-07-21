#!/bin/bash

set -euo pipefail
cd "$(dirname "$0")"

pushd rust-hyper
cargo build --release
popd

for i in */; do
    pm2 start "${i}start.sh" --name "host-of-troubles-${i%/}"
done

pm2 save
