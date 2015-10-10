# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:54:21 2015

@author: DeclanRyan
"""

import sqlite3

#Import and create list for Plant location longitudes
conn = sqlite3.connect('renewable.db')
c = conn.cursor()
c.execute("SELECT long FROM location")
longitude = []
print "Longitude coordinates for all 10 Plant locations:"
for item in c:
    print item 
    longitude.append(item)    
print
print "Plant 1's longitude coordinate is: ", longitude[0]
print


#Import and create list for Plant location latitudes
c.execute("SELECT lat FROM location")
latitude = []
print "Latitude coordinates for all 10 Plant locations:"
for item in c:
    print item 
    latitude.append(item)    
print
print "Plant 1's Latitude coordinate is: ", latitude[0]
print

#Import and create list for each Plant's production in tonnes
conn = sqlite3.connect('renewable.db')
c = conn.cursor()
c.execute("SELECT production FROM location")
production = []
print "Productiion numbers for all 10 Plant locations:"
for item in c:
    print item 
    production.append(item)    
print
print "Plant 1's Production is: ", production[0], " tonnes."
print


#Import and create list for Port location longitudes
conn = sqlite3.connect('renewable.db')
c = conn.cursor()
c.execute("SELECT long FROM ports")
portLongitude = []
print "Longitude coordinates for all 3 Port locations:"
for item in c:
    print item 
    portLongitude.append(item)    
print "Port 3's Longitude coordinate is: ", portLongitude[2]
print

#Import and create list for Port location latitudes
conn = sqlite3.connect('renewable.db')
c = conn.cursor()
c.execute("SELECT lat FROM ports")
portLatitude = []
print "Latitude coordinates for all 3 Port locations:"
for item in c:
    print item 
    portLatitude.append(item)    
print
print "Port 3's Latitude coordinate is:  ", portLatitude[2]
print

print "GitHub Test"
print "Why won't GitHub recognize that I've made changes to this file"



    