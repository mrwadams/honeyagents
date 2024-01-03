#!/bin/bash

# Step 1: Pipe the latest output from `docker logs honeypot` to cowrie_logs file
docker logs honeypot > ./honeypot/cowrie_logs.txt

# Step 2: Execute the agent.py script inside the autogen container to instruct the 
# agent to analyse the logs and update the configuration of the reverse proxy
docker exec autogen python agent.py