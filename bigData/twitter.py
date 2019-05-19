import tweepy
import pandas as pd
import os

# consumer keys and access tokens, used for OAuth
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# creation of the actual interface, using authentication
api = tweepy.API(auth)

diccionario = {}
columns = []
titulos = []
resultado = []


search = tweepy.Cursor(api.search, q="Mario Ferreiro", lang="es").items(5)

titulos.append('Tweet')
titulos.append('Autor')
titulos.append('Tiempo de Tweet')
titulos.append('Favs')
titulos.append('Retweets')


for item in search:
    contenido = []
    contenido.append(item.text)
    contenido.append(item.user.name)
    contenido.append(item.created_at)
    contenido.append(item.favorite_count)
    contenido.append(item.retweet_count)


    for i,e in enumerate(titulos):
        diccionario[titulos[i]] = contenido[i]

        resultado.append(diccionario)
        diccionario = {}

df = pd.DataFrame(
        resultado)
df.to_csv('tweets.csv', index=False)