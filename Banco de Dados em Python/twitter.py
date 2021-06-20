from pymongo import MongoClient
# Importando os módulos Tweepy, Datetime e Json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json
# Importando o módulo Scikit Learn
from sklearn.feature_extraction.text import CountVectorizer
import sklearn
sklearn.__version__


# Adicione aqui sua Consumer Key
consumer_key = "Bqof1YM1IOJRdzjAJZcgBcqpd"

# Adicione aqui sua Consumer Secret 
consumer_secret = "BScSn8Ii2vZp2f4TO0CCSkMbtqkWxX61T7u9dLq3OZ39EKnDiB"

# Adicione aqui seu Access Token
access_token = "983015635277041665-77FbncBcktxrw3hE8O5EIMNNFpiITwf"

# Adicione aqui seu Access Token Secret
access_token_secret = "R00IDVzasjpX1XssTHAyQYniAOc2umhD2kzOmX4uYV04G"

# Criando as chaves de autenticação
auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

# Criando uma classe para capturar os stream de dados do Twitter e 
# armazenar no MongoDB
class MyListener(StreamListener):
    def on_data(self, dados):
        tweet = json.loads(dados)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at,"id_str":id_str,"text":text,}
        tweetind = col.insert_one(obj).inserted_id
        print (obj)
        return True

mylistener = MyListener()
mystream = Stream(auth, listener = mylistener)

client = MongoClient()
db = client.twitterdb
col = db.tweets 
keywords = ['BigData', 'Python','Data Mining','Data Science']

#mystream.filter(track=keywords)

mystream.disconnect()   

# Verificando um documento no collection
col.find_one()

# criando um dataset com dados retornados do MongoDB
dataset = [{"created_at": item["created_at"], "text": item["text"],} for item in col.find()]

# Importando o módulo Pandas para trabalhar com datasets em Python
import pandas as pd
pd.__version__

# Criando um dataframe a partir do dataset 
df = pd.DataFrame(dataset)

print(df)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df.text)

# Contando o número de ocorrências das principais palavras em nosso dataset
word_count = pd.DataFrame(cv.get_feature_names(), columns=["word"])
word_count["count"] = count_matrix.sum(axis=0).tolist()[0]
word_count = word_count.sort_values("count", ascending=False).reset_index(drop=True)
print(word_count[:50])



