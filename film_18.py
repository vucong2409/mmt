import os
import json 
import requests

reqStr = "https://api.themoviedb.org/3/movie/"
apiKey = "?api_key=8d2cc10d6d30121c3ae4048743b64da3&language=en-US"

print ("Enter code film: ")
codeFilm = input()

# for codeFilm in range(791370, 791373):
res = requests.get(reqStr + str(codeFilm) + apiKey)

result_json = res.json()
list_genres = result_json["genres"]

print ("Film name: " + result_json["original_title"] + "\n")

genres_str = "Genres: "
for genres in list_genres:
    genres_str = genres_str + genres["name"] + " "

print(genres_str + "\n")

print("Overview: " + result_json["overview"] + "\n")

if (result_json["status"] == "Released"):
    print("Released Date: " + result_json["release_date"] + "\n")
else:
    print(result_json["status"] + "\n")

print("----------------------------------------------------")

