from selenium import webdriver
import request
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import bs4
import os

#new&hot electronic 
new_hot = "https://soundcloud.com/charts/new?genre=electronic&country=all-countries"
top_50_classical = "https://soundcloud.com/charts/top?genre=classical&country=all-countries"
track_url = "https://soundcloud.com/search/sounds?q="
artist_url = "https://soundcloud.com/search/people?q="
mix_url = "&filter.duration=epic"

#selenium browser
browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
browser.get("http://soundcloud.com")


 #main menu
print()
print(">>> Welcome to the python Soundcloud scraper!")
print(">>> Explore Cool Tracks, artists, and mixes")
print(">>> Search for tracks, artists, and mixes")
print()

while True:

	print(">>> Menu")
	print(">>> 1 - Search for a track")
	print(">>> 2 - Search for an artist")
	print(">>> 3 - Search for a mix")
	print(">>> 4 - Top 50 classical")
	print(">>> 5 - New & Hot")
	print(">>> 0 - Exit")
	print()

	choice = int(input(">>> Your choice: "))

	if choice == 0:
 		browser.quit()
 		break
	print()

	if choice == 1:
 		name = input('Name of the track: ')
 		print()
 		"%20".join(name.split(" ")) 
 		browser.get(track_url + name)
 		continue 

	if choice == 2:
 		name = input('Name of the artist: ')
 		print()
 		"%20".join(name.split(" ")) 
 		browser.get(artist_url + name)
 		continue

	if choice == 3:
 		name = input('Name of the mix: ')
 		print()
 		"%20".join(name.split(" ")) 
 		browser.get(track_url + name + mix_url_end)
 		continue   

print()
print("Goodbye!")
print()

