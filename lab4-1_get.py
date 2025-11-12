#!/usr/bin/env python3
# lab4-1_get.py
# Name: Jamie Knowles 
# Student Number: C00307559  
# Date: 12/11/2025
# Purpose: Simple GET request and header display.

import requests, sys  # import requests for web requests, sys for command line args

# function to send a GET request and show key headers
def simple_get(url):
    try:
        # send request (5 second timeout and follow redirects)
        r = requests.get(url, timeout=5, allow_redirects=True)

        # print info about the page
        print("URL:", url)                        # show website URL
        print("Status:", r.status_code)           # show HTTP status code (e.g. 200 OK)
        print("Server:", r.headers.get("Server")) # show what server is used
        print("Content-Type:", r.headers.get("Content-Type"))  # show type of content
    except Exception as e:
        # if something goes wrong print the error
        print("Error:", e)

# main part of the program
if __name__ == "__main__":
    # check that the user entered a URL
    if len(sys.argv) < 2:
        print("Usage: python lab4-1_get.py <url>")  # message if no URL entered
    else:
        simple_get(sys.argv[1])  # run function with the given URL