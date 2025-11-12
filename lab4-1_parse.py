#!/usr/bin/env python3
# lab4-1_parse.py
# Name: Jamie Knowles 
# Student Number:C00307559 
# Date: 12/11/2025
# Purpose: Parse title and meta info using BeautifulSoup

from bs4 import BeautifulSoup   # for reading and searching HTML
import requests, sys, json       # requests = web access, sys = command line, json = clean output

# function to download the page and look for info
def parse(url):
    # get the web page (timeout 5 seconds so it doesn’t hang)
    r = requests.get(url, timeout=5)

    # load page into BeautifulSoup for easy HTML reading
    s = BeautifulSoup(r.text, "html.parser")

    # find title text (if page has one)
    title = s.title.string if s.title else None

    # count how many <form> tags exist
    forms = len(s.find_all("form"))

    # put results into a small JSON object
    result = {
        "url": url,
        "title": title,
        "forms_found": forms
    }

    # print the result neatly in JSON format
    print(json.dumps(result, indent=2))

# only runs if script started directly
if __name__ == "__main__":
    # check if URL entered
    if len(sys.argv) < 2:
        print("Usage: python lab4-1_parse.py <url>")  # message if no link typed
    else:
        parse(sys.argv[1])  # run the function with the given URL