# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:54:21 2015

@author: DeclanRyan
"""

import sqlite3
import math
#Import and create list for Plant location longitudes
conn = sqlite3.connect('renewable.db')
c = conn.cursor()
c.execute("SELECT long FROM location")
longitude = []
for item in c:
    print item 
    longitude.append(item)    

#Import and create list for Plant location latitudes
c.execute("SELECT lat FROM location")
latitude = []
for item in c:
    print item 
    latitude.append(item)    

#Import and create list for each Plant's production in tonnes
conn = sqlite3.connect('renewable.db')
c = conn.cursor()
c.execute("SELECT production FROM location")
production = []
for item in c:
    print item 
    production.append(item)    

#Import and create list for Port location longitudes
conn = sqlite3.connect('renewable.db')
c = conn.cursor()
c.execute("SELECT long FROM ports")
portLongitude = []
for item in c:
    print item 
    portLongitude.append(item)    

#Import and create list for Port location latitudes
conn = sqlite3.connect('renewable.db')
c = conn.cursor()
c.execute("SELECT lat FROM ports")
portLatitude = []
for item in c:
    print item 
    portLatitude.append(item)    

# This is a function to calculate the distance between 2 points
# given the longitude and latitude of the two points
def distance(lat1, long1, lat2, long2):
# Convert latitude and longitude to spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0     
# phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians   
# theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
#Calculate spherical distance from spherical coordinates for two locations 
#in spherical coordinates (1, theta, phi) and (2, theta', phi')
#cosine(arc length) = sin phi sin phi' cos(theta-theta') + cos phi cos phi'
#distance = rho * arc length
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
    arc = math.acos(cos)
#Units are not important as we are only trying to find the 
#best option relative to all the others
    return arc

#Loops within a loop to call the distance function and calculate
#the best option re. distance between locations, production and
#the distance to the 3 ports
i = 0
k = 0
p = 0
portCostList = []
while i < 10:
    j = 0
    temp = 0
    while j < 10:    
        temp = temp + (production[j] * distance(longitude[i], latitude[i], longitude[j], latitude[j])        
        j += 1
    k = 0
    while k < 3:
        totalCost = temp * distance(longitude[i], latitude[i], portLongitude[k], portLatitude[k])
        portCostList[p] = totalCost  '''Creates a list of 30 floating point numbers representing each of 3 ports for each location'''
        p += 1
    i+=1
#We now have a list called portCostList with 30 entries
#so we need to find the lowest number in this list, find it's index
#and determine which location and which port is associated with this
#value based on the fact that indexes 0, 1 and 2 are from 
#ports 1, 2 and 3 with respect to location 1 etc.  '''

m = 0 '''Set counter variable m to 0 for first entry in portCostList'''
bestOption = 0  '''Sets first entry as the initial best option'''
while m < 30;
    if portCostList[m + 1] < portCostList[m]:
        bestOption = m + 1
    m += 1
#We need to add one to bestOption because the list index starts at 0
bestOption += 1    
print "The best option is number " bestOption, " of 30"

#Determine which location and which port this option corresponds to
locationNumber = (bestOption/3) + 1 
#To take into account that 3 will go into bestOption one less
#than the location number it refers to
portNumber = bestOption % 3
print "The very best option is to set up the production plant "
print "at location number ", locationNumber, " and transport "
print "the products from port number ", portNumber, "."
