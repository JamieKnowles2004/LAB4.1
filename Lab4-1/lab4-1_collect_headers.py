#!/usr/bin/env python3
# lab4-1_collect_headers.py
# Name: Jamie Knowles 
# Student Number: C00307559 
# Date: 12/11/2025
# Purpose: Collect headers from URLs and save to JSON.

import requests, json, sys   # requests = web access, json = save data, sys = command line

# function to go through each URL and collect header info
def collect(urls):
    data = []  # list to store info

    for u in urls:
        try:
            # send a GET request with a short timeout
            r = requests.get(u, timeout=5)

            # save url, status code and server header
            data.append({
                "url": u,
                "status": r.status_code,
                "server": r.headers.get("Server")
            })
        except Exception as e:
            # if something goes wrong, store the error
            data.append({"url": u, "error": str(e)})

    # write all results to headers.json (formatted nicely)
    with open("headers.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Saved headers.json")  # let the user know the file was saved

# only runs if script started directly
if __name__ == "__main__":
    # check that at least one URL was entered
    if len(sys.argv) < 2:
        print("Usage: python lab4-1_collect_headers.py <url1> <url2> ...")
    else:
        collect(sys.argv[1:])  # run the function with the URLs given