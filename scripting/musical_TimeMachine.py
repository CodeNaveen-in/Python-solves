from bs4 import BeautifulSoup
import lxml
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()  # To Load variables from .env file

# For authorisation
client_id_yours = os.getenv("SPOTIPY_CLIENT_ID")
client_secret_yours = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri_yours = os.getenv("SPOTIPY_REDIRECT_URI")

sp= spotipy.Spotify(
    auth_manager=SpotifyOAuth( #Opens tab to verify
        client_id=client_id_yours,
        client_secret=client_secret_yours,
        redirect_uri=redirect_uri_yours,
        scope="playlist-modify-public"
        #,show_dialog=True - Overrules captcha and verify everytime 
    )
)

user_id = sp.current_user()["id"]
if (user_id):
    print("Successful authorisation and Login!")

# For getting data
header = {"USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"}
date = input("Enter your required date to search in YYYY-MM-DD :\t")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date, headers=header)
#working without the header, but header added because sites deny requests without header (i.e. bot use on site)
#Special thanks to Billboard for letting me use code

billy_page = response.text
songlist = BeautifulSoup(billy_page, "lxml")
list_name = songlist.select("li.o-chart-results-list__item > h3")

print(f"\nThe top 100 songs of the {date} are: ")
num = 1
for i in list_name:
    print(f"{num}.",i.getText().strip())
    num+=1

# Create a new playlist - (Helped by AI will practice later on)
playlist = sp.user_playlist_create(user=user_id, name=f"Billboard Top 100 - {date}", public=True)
playlist_id = playlist["id"]
print(f"\nCreated Playlist: {playlist['name']}")

# Search each song and collect track URIs - (Helped with AI will practice later on)
track_uris = []
for song in list_name:
    result = sp.search(q=song, limit=1, type="track")
    if result['tracks']['items']:
        track_uri = result['tracks']['items'][0]['uri']
        track_uris.append(track_uri)
    else:
        print(f"Track not found on Spotify: {song}")

# Add all found tracks to the playlist in chunks of 100 (Spotify’s API limit) - (Helped with AI will practice later on)
for i in range(0, len(track_uris), 100):
    sp.playlist_add_items(playlist_id, track_uris[i:i + 100])

print("\n🎧 Playlist created and populated successfully!")
