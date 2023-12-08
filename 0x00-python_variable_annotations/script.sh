#!/bin/bash

for i in {0..102}; do
    if (( i >= 0 && i <= 9 )) || (( i >= 100 && i <= 102 )); then
        echo "#!/usr/bin/env python3" > "${i}-main.py"
    fi
done
