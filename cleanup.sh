#!/bin/bash

# Step 1: Bring down the Docker containers
docker-compose down

# Step 2: Delete Cowrie log files
rm ./honeypot/*

# Step 3: Delete NGINX log files
rm ./nginx_logs/*

# Step 4: Delete AutoGen output files
rm ./autogen/var/bad_ips.csv
rm ./autogen/var/report.md

# Step 5: Remove volumes
docker volume rm honeyagents-autogen_nginx_config
docker volume rm honeyagents_cowrie_logs
docker volume rm honeyagents_nginx_config

# Step 6: Remove unused local volumes
docker volume prune -f

# Print confirmation
echo "Clean-up completed."
