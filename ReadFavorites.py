# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:01:25 2021

@author: Spiros
"""
def ReadEdgeFavorites(readFile, writeFile, delimiter = "'"):
    '''
    Parameters
    ----------
    readFile : String
        The xml file that contains edge favorites.
    writeFile : String
        The converted file.
    delimiter : String, optional
        The .csv fields delimiter. The default is "'".

    Returns
    -------
    None.

    '''
    fileContents = []
    with open(readFile, encoding='utf8') as f:
        for line in f:
            fileContents.append(line)
    
    categoryStr = linkStr = titleStr =""
    allLines = []

    for x in fileContents:
        if (x.find("<DT><H3") > 0):         # Get category name
            categoryStr = (x[x.find("LAST_MODIFIED") + 27 : x.find("</H3>")])
        if (x.find('<DT><A HREF="') > 0):
            pos1 = x.find('<DT><A HREF="')  # Address start position
            pos2 = x.index('"', pos1 + 15)  # Address end position
            pos3 = x.find("ADD_DATE=") + 22 # Title start position
            if (x.find("ICON=", pos3) > 0): # If icon exists, change title start
                pos3 = x.index('">', x.find("ICON=", pos3 -1)) + 2
            pos4 = x.index("</A>", pos3)    # Title end position
            linkStr = x[pos1 + 13 : pos2]   # Get link address
            titleStr = x[pos3: pos4]        # Get link title
        if (linkStr != ""):                 # If link is empty, do not write it
            allLines.append(f'{categoryStr}{delimiter}{linkStr}{delimiter}{titleStr}') # Python 3.6+
        linkStr = ""
        titleStr = ""

    f = open(writeFile, "w", encoding='utf8')
    for line in allLines:
        f.write(line + "\n")
    f.close()

ReadEdgeFavorites(r'C:\temp\Favorites\edge.html', 'edgeFavorites.csv')