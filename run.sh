#!/bin/bash
TICKER=${1:-1810.HK}
uv run python -m cli.main analyze -t "$TICKER"