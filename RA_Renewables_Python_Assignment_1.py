# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:54:21 2015

@author: DeclanRyan
"""


import sqlite3

conn = sqlite3.connect('renewable.db')
c = conn.cursor()
c.execute("SELECT * FROM renewable.db")
for item in c:
    print item



    