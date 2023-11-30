#!/bin/sh
while true; do
    curl -H "X-Forwarded-For: 172.18.0.2" http://www.rebel-alliance.com
    sleep 30
done
