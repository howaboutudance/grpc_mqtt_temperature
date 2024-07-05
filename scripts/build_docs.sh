#!/usr/bin/env bash

set +x

# build readme.md
pandoc -f markdown -t gfm doc/readme/readme_source.md -o README.md