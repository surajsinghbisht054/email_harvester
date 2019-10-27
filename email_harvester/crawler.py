#!/usr/bin/python3


#
# Author :
#         Surajsinghbisht054@gmail.com
#

# Import Module
import urllib.request, urllib.error, urllib.parse
import re
import sys

# Configuration
html_dump = "tempdump"  # Temp File Name

# Function For Extracting Html Link
def link(html_data):
    # Filtering Url links
    print("[*] Extracting Html Links ...")
    pattern = re.compile('(<a .*?>)')
    a_tag_captured = pattern.findall(html_data)
    for i in a_tag_captured:
        href_raw=i[str(i).find('href'):]
        href=href_raw[:href_raw.find(' ')]
        yield href[6:-1]
    return

# Function For Downloading Html
def main(url):
    try:
        print("[*] Downloading Html Codes ... ", end=' ')
        header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0'}
        req=urllib.request.Request(url, headers=header)
        page = urllib.request.urlopen(req).read()
    except Exception as e:
        page='None'
    return page
temp = open(html_dump, 'a')     # Open Temp File

if len(sys.argv)==1:
	print("[+] Please Enter Website Address As Argument")
	exit(0)
for i in link(main(sys.argv[1])):   # enter you website address  
	temp.write(main(i))        # Write Data On File

temp.close()                    # Closing File
