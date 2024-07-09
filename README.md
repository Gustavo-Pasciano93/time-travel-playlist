# Time Travel Playlist

Este projeto viaja no tempo para criar uma playlist no Spotify com as músicas do Top 100 da Billboard de uma data específica. Usando Python, BeautifulSoup e Spotipy, você pode criar uma playlist personalizada que celebra momentos especiais, como o dia do seu nascimento, com as músicas mais populares daquela época.

## Funcionalidades

- Extrai as músicas do Top 100 da Billboard de uma data específica.
- Cria uma playlist no Spotify com essas músicas.
- Usa a API do Spotify para autenticação e manipulação de playlists.

## Pré-requisitos

- Python 3.6 ou superior
- Conta no Spotify
- Credenciais de desenvolvedor do Spotify (client_id, client_secret e redirect_uri)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/time-travel-playlist.git
   cd time-travel-playlist

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   git clone https://github.com/seu-usuario/time-travel-playlist.git
   cd time-travel-playlist

3.Instale as dependências:
  ```bash
  import requests
  from bs4 import BeautifulSoup
  import spotipy
  from spotipy.oauth2 import SpotifyOAuth



4.Instale as dependências:
  ```bash
  client_id = "seu_client_id"
  client_secret = "seu_client_secret"
  redirect_uri = "http://seu_redirect_uri"




## Exemplo: O exemplo abaixo cria uma playlist com as músicas do Top 100 da Billboard de 23 de novembro de 1993:

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

client_id = "seu_client_id"
client_secret = "seu_client_secret"
redirect_uri = "http://seu_redirect_uri"
scope = "playlist-modify-public"
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




