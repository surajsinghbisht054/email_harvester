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
import re

# Configuration
html_dump = "tempdump"				# Temp File Name
temp_file = open(html_dump, 'r')	# Open File
data = temp_file.read()				# Read Data
temp_file.close()					# Close File

# Function For Extracting Email Address
def email(data):
    # Filtering Url links
    pattern = re.compile('[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', re.MULTILINE)
    captured = pattern.findall(data)
    return captured

email_list = []					# LIst For Collecting Emails

# Collecting Emails
for i in email(data):
	if i not in email_list:
		email_list.append(i)
		
# Print Collected Emails
print email_list
