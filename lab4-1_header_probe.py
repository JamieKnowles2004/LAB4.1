#!/usr/bin/env python3
# lab4-1_header_probe.py
# Jamie Knowles 
# Student Number: C00307559 
# Date: 12/11/2025
# Purpose: Check how site reacts to different User-Agents.
import requests, sys

# list of user-agents to try (browsers and common scanners)
agents = ["Mozilla/5.0", "curl/7.68.0", "sqlmap/1.5.4"]

# loop each agent and make a request with that User-Agent
for a in agents:
    try:
        # send request with custom User-Agent, short timeout to avoid hanging
        r = requests.get(sys.argv[1], headers={"User-Agent": a}, timeout=5)
        # print which agent, the HTTP status, and Server header (if present)
        print(a, "->", r.status_code, r.headers.get("Server"))
    except Exception as e:
        # if request fails print the agent and the error
        print(a, "-> error", e)