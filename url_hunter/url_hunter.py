import urllib2
import re

def visit_link(link):
    print("Visiting " + link)
    try:
        response = urllib2.urlopen(link)
    except:
        print("Failed to fetch URL")
        return ""
    html = response.read()
    return html

def get_links_from_html(html):
    links = re.findall("\"https?://[^\s]+\"", html)
    better_links = []
    for link in links:
      better_link = link.replace("\"", "")
      better_links = better_links + [better_link]
    return better_links


def get_neighbors_of_one_link(link):
    return get_links_from_html(visit_link(link))

def get_neighbors(links):
    neighbors = []
    for link in links:
        neighbors += get_neighbors_of_one_link(link)
    return neighbors


start_link = 'http://python.org/'
html = visit_link(start_link)
links_to_explore = get_links_from_html(html)

visited_links = [start_link]
while len(visited_links) < 30:
    # Visit one of the yet-to-be-explored links
    link_we_visit_now = links_to_explore[0]
    new_links_to_explore = get_neighbors_of_one_link(link_we_visit_now)
    visited_links += [link_we_visit_now]
    links_to_explore = links_to_explore[1:] + new_links_to_explore

print("You have explored a good chunk of the internet. Good job!")
print(visited_links)



# Queue of links to visit -- what order of pages do we want to crawl the web in?
#     Depth first -- start at python.org, go to the first link you find, visit that page, go to the first link on that page, etc.
#     Breadth first -- go to all links from python.org, then go to all links from the first link, then all links from the second link, etc.
#     Random walk -- what google does (or did in the beginning)
# This program uses breadth first.