#!/bin/bash

cat << EOF | python - > __version.txt
import version
print(version.VERSION)
EOF

VERSION=$(cat __version.txt)
rm __version.txt

echo $VERSION