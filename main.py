import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth



print("Vamos viajar para 23/11/1993")

URL = "https://www.billboard.com/charts/hot-100/1993-11-27/"


response = requests.get(URL)

website = response.text

soup = BeautifulSoup(website, "html.parser")

song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]

#print(song_names)


client_id = "e4f0d17064534e2686be09f215f6cb45"

client_secret ="6d0da5018db741e2b562e5ef12047f10"

redirect_uri ="http://example.com"


scope = "playlist-modify-public"

#client_credential_manager = SpotifyClientCredentials(client_id= client_id, client_secret= client_secret)

#sp = spotipy.Spotify(client_credentials_manager= client_credential_manager)

sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)
token_info = sp_oauth.get_access_token(as_dict=False)
sp = spotipy.Spotify(auth=token_info)


user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user=user_id, name="Musicas do dia do nascimento", public=True)
playlist_id = playlist['id']


track_uris = []

for song in song_names:
    result = sp.search(q=f"track:{song}", type="track", limit=1)
    tracks = result.get('tracks', {}).get('items', [])
    
    
    if tracks:
        track_uris.append(tracks[0]['uri'])
        
if track_uris:
    sp.playlist_add_items(playlist_id, track_uris)
    
    

print(f"Playlist criada: {playlist['external_urls']['spotify']}")