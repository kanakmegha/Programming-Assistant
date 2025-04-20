#!/bin/bash

# Run the container
docker run -d -p 8001:5000 --name programming-assistant programming-assistant

# Give Docker a few seconds to boot up
sleep 3

# Open in default browser (macOS)
open http://localhost:8001

# For Linux (uncomment below if on Linux)
# xdg-open http://localhost:8001

# For Windows Git Bash (uncomment below)
# start http://localhost:8001
