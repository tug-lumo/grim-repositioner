#!/bin/sh
# Build the deployable site into dist/: only what the browser needs (docs, .claude, serve.py stay private).
set -e
rm -rf dist
mkdir -p dist
cp index.html dist/
cp -r vendor brand dist/
cat > dist/_headers <<'H'
/vendor/*
  Cache-Control: public, max-age=31536000, immutable
/index.html
  Cache-Control: no-cache
/
  Cache-Control: no-cache
H
echo "Built dist/"
