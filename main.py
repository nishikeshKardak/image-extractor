import bs4
import requests
import re


web_page = input("Enter the url or link of webpage that you want to extract")
#web_page = "https://www.github.com"
res = requests.get(web_page)
page = res.text

#function for taking next target file
def get_next_target(page):
    start_link = page.find('<img src=')
    if start_link == -1:
        return None , 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote+1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


#print all links that extract from page
def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

print_all_links(page)
