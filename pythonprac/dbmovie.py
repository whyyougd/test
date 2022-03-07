from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.6hcta.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

#1 Quiz1 : 가버나움의 평점 가져오기
movie = db.movies.find_one({'title':'가버나움'})['star']
#print(movie)

#2 Quiz2 : 같은 평점의 영화 제목 가져오기
#same = db.movies.find_one({'rank':movie})#['title']
#print(same)

all_movies = list(db.movies.find({'star':movie},{'_id':False}))
for m in all_movies:
    #print(m['title'])

#3 Quiz3 : 가버나움 평점 0으로 만들기
    db.movies.update_one({'title': '가버나움'}, {'$set': {'star': '0'}})
    print(movie)