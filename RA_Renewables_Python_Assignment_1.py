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

# This is a function to calculate the distance between 2 points
# that I found on the Internet
def distance(lat1, long1, lat2, long2):
 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
         
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
         
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
         
    # Compute spherical distance from spherical coordinates.
         
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta', phi')
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
     
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc
#I don't think I need this function
#Function to determine which port is best for each location
'''def cheapestPortFunction(List):
    n = 1
    bestOption = (cheapestPort[n-1].index) + 1 '''Representing the first port'''
    while n < 3:    
        if cheapestPort[n] < cheapestPort[n-1]:
            bestOption = (cheapestPort[n].index) + 1
        n += 1
    return bestOption
'''

#Loops within a loop to call the distance function 
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
#    cheapestPort = cheapestPortFunction(portCostList)
    i+=1
'''We now have a list called portCostList with 30 entries
so we need to find the lowest number in this list find it's index
and determine which location and which port is associated with this
value based on the fact that indexes 0, 1 and 2 are from 
ports 1, 2 and 3 with respect to location 1 etc.  '''

k = 0
bestOption = 0
while k < 30;:
    if portCostList[k + 1] < portCostList[k]:
        bestOption = k
    k += 1
#We need to add one to bestOption because the list index starts at 0
bestOption =bestOption +1    
print "The best option is number " bestOption, " of 30"
#Determine which location and which port this option gives us

locationNumber = (bestOption/3) + 1 
'''To take into account that 3 will go into bestOption 
one less than the location number it refers to'''
portNumber = bestOption % 3

print "The very best option is to set up the plant "
print "at location number ", locationNumber, " and "
print "transport the products from port number ", portNumber
