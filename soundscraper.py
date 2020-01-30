from selenium import webdriver
import requests
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import bs4
import os

#new&hot electronic 
new_hot = "https://soundcloud.com/charts/new?genre=electronic&country=all-countries"
top_url = "https://soundcloud.com/charts/top"
track_url = "https://soundcloud.com/search/sounds?q="
artist_url = "https://soundcloud.com/search/people?q="
mix_url_end = "&filter.duration=epic"


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
    print(">>> 4 - Top charts")
    print(">>> 0 - Exit")
    print()
    choice = int(input(">>> Your choice: "))
    if choice == 0:
        browser.quit()
        break
    print()

    # search for a track
    if choice == 1:
        name = input("Name of the track: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name)
        continue

    # search for an artist
    if choice == 2:
        name = input("Name of the artist: ")
        print()
        "%20".join(name.split(" "))
        browser.get(artist_url + name)
        continue
    # search for a mix
    if choice == 3:
        name = input("Name of the mix: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name + mix_url_end)
        continue


    # get the top 50 tracks for a genre   

    while True:
        print(">>> Genres Available:")
        print()

        # genre menu
        url = ''
        if choice == 4: url = top_url
        else: url = new_url

        # parse the html with beautiful soup
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        # print request.text

        genres = soup.select("a[href*=genre]")[2:]
        # print each genre

        genre_links = []

        # print out the available genres
        for index, genre in enumerate(genres):
            print(str(index) + ": " + genre.text)
            genre_links.append(genre.get("href"))

        print()
        choice = input(">>> Your choice (x to re-select chart type): ")
        print()

        if choice == 'x': break
        else: choice = int(choice)

        # print(genre_links[choice])

        url = "http://soundcloud.com" + genre_links[choice]
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")

        tracks = soup.select("h2")[3:]
        track_links = []
        track_names = []
        # print(tracks)

        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print(str(index+1) + ": " + track.text)
            print()

        # song selection loop
        while True:
            choice = input(">>> Your choice (x to go back to the main menu): ")
            print()
            if choice == 'x': break
            else: choice = int(choice)-1
            print("Now playing: " + track_names[choice])
            print()

            browser.get("http://soundcloud.com" + track_links[choice])

print()
print("Goodbye!")
print()
