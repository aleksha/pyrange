#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

mat_no_blacklist = ["011"]
# 011 is Sodium

print("Parsing the form")

# step 1: parse the material numbers and names
url = "https://physics.nist.gov/PhysRefData/Star/Text/PSTAR-t.html"
form_page_source = requests.get(url).text
soup = BeautifulSoup(form_page_source, "html.parser")
# dictionary that contains pairs
# material number : material name
mat_dict = {i["value"]: i.text for i in soup.find_all("option")}
# change material names to be valid filenames
allowed_symbols = "()-_ "
for mat_no in mat_dict:
    mat_name = mat_dict[mat_no]
    mat_name = (
        "".join(x for x in mat_name if x.isalnum() or x in allowed_symbols) + ".txt"
    )
    split = mat_name.split()
    mat_name = " ".join(split[1:]) if split[0].isnumeric() else mat_name
    mat_dict[mat_no] = mat_name

# remove materials from the blacklist by number
for mat_no in mat_no_blacklist:
    del mat_dict[mat_no]

print("Parsing materials")

# step 2: get the tables for each material
# set the url for post request
url = "https://physics.nist.gov/cgi-bin/Star/ap_table-t.pl"
# set the basic request body
data = {"matno": None, "prog": "PSTAR", "ShowDefault": "on", "Energies": ""}
for mat_no in mat_dict:

    print(mat_no + ": " + mat_dict[mat_no] + " started")

    # change the material number in the body
    data["matno"] = mat_no

    # make the request
    table_page_source = requests.post(url=url, data=data).text

    # get the useful part of the source
    soup = BeautifulSoup(table_page_source, "html.parser")
    raw_table_text = str(soup.body.pre)

    lines = raw_table_text.split("<br/>")
    # make sure the table is there
    assert len(lines)>100, 'Table is too short'
    # cut the junk
    lines = lines[3:-1]
    # comment everything but the table
    for line_num in range(11):
        lines[line_num] = "#" + lines[line_num]
    result_table_text = "\n".join(lines)

    # save to file
    with open(mat_dict[mat_no], "w") as file:
        file.write(result_table_text)

    print(mat_no + ": " + mat_dict[mat_no] + " done")