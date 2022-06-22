# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:23:35 2022

@author: c_con
"""

# importing the module
from pytube import YouTube

#ask for the link from user
link = "https://youtu.be/7YavzuAwjfg"
print('here')
yt = YouTube(link)
print('here')
#Showing details
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download(r'C:\Users\c_con\Videos\Tampa')
print("Download completed!!")
