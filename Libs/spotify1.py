import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="35773aa6ef624da480451f164be3c785",
                                                           client_secret="f29f24c1365749e2b03df679face4544"))

results = sp.search(q='Moon Landing', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
