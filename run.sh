#!/bin/bash
TICKER=$1
if [ -z "$TICKER" ]; then
    read -p "Please enter the ticker (e.g. 1810.HK): " TICKER
    if [ -z "$TICKER" ]; then
        echo "Error: No ticker provided. Exiting..."
        exit 1
    fi
fi
uv run python -m cli.main analyze -t "$TICKER"