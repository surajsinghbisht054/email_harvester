#!/usr/bin/python
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For https://bitforestinfo.blogspot.in
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    https://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
# Import Module
import urllib2
import re
import sys

# Configuration
html_dump = "tempdump"  # Temp File Name

# Function For Extracting Html Link
def link(html_data):
    # Filtering Url links
    print "[*] Extracting Html Links ..."
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
        print "[*] Downloading Html Codes ... ",
        header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0'}
        req=urllib2.Request(url, headers=header)
        page = urllib2.urlopen(req).read()
    except Exception as e:
        page='None'
    return page
temp = open(html_dump, 'a')     # Open Temp File

if len(sys.argv)==1:
	print "[+] Please Enter Website Address As Argument"
	exit(0)
for i in link(main(sys.argv[1])):   # enter you website address  
	temp.write(main(i))        # Write Data On File

temp.close()                    # Closing File
