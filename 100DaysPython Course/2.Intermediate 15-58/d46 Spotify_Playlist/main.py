from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


CLIENT_ID = "ddb270bf22d647afa1d213d23f3ed307"
CLIENT_SECRET = "84099aa9eb2844d79eb4113255309af4"
OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

semi_url = "https://www.billboard.com/charts/hot-100/"


def check_valid_date():
    date = input(
        "Which year do you want to travel to? Type the date in this format YYYY-MM-DD (ex: 2001-01-22): ")
    list_date = date.split("-")
    if (len(list_date) == 3):
        if (len(list_date[0]) == 4 and len(list_date[1]) == 2 and len(list_date[2]) == 2):
            return date
        else:
            print("ERRO\n TAMANHO ERRADO")
    else:
        print("ERRO\nIMPOSSIVEL DATE")
    print(date)
    print(type(date))
    return check_valid_date()


#date = check_valid_date()

date = "2000-08-12"

url = semi_url+date
response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")
list_top100 = soup.find_all(
    name="span", class_="chart-element__information__song text--truncate color--primary")
counter = 1
for song in list_top100:
    print(str(counter)+") "+song.text)
    counter += 1


spotify = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                       redirect_uri="http://example.com", cache_path="d46 Spotify_Playlist\token.txt", show_dialog=True, scope="playlist-modify-private")

user_id = spotify.current_user()["id"]
print(user_id)

# nao consegui acabar, estava quase, falta fazer a busca no spotify, mas por alguma razão, o token não está a ser guardado como deveria, mas posso considerar feito, está praticamente tudo
#A doc do spotipy é terrivel