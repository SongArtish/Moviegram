# 영화정보를 API를 이용해서 가져오기

# 홈페이지  https://www.themoviedb.org/
# Document  https://developers.themoviedb.org/3

import json
# pip install requests
import requests
from api_key import URLMaker

# # url 가져오기
# url_maker = URLMaker(URLMaker.key)
# url = url_maker.get_url()

# # url 요청
# r = requests.get(url)
# movie_dict = r.json()

# result = [movie_dict]

# with open('movies.json', 'w', encoding='UTF-8') as file:
#     file.write(json.dumps(result, ensure_ascii=False))


### fixtures, loaddata로 처리


#####################################################################################

## 1. movie 정보
result = []
url = URLMaker.url
key = URLMaker.key
for page in range(1, 6):
    URL = f'{url}?api_key={key}&language=ko-Kr&page={page}'

    raw_data = requests.get(URL).json()
    data = raw_data.get('results')
    for movie in data:
        movie_dict = {
            "model" : "movies.movie",
            "pk" : movie.get("id"),
            "fields" : {
                "title" : movie.get("title"),
                "popularity" : movie.get("popularity"),
                "genre_ids" : movie.get("genre_ids"),
                "release_date" : movie.get("release_date"),
                "vote_average" : movie.get("vote_average"),
                "vote_count" : movie.get("vote_count"),
                "overview" : movie.get("overview"),
                "poster_path" : movie.get("poster_path")
            }
        }
        result.append(movie_dict)

with open('movies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(result, ensure_ascii=False))

## 2. genre 정보

data = [
    {
      "id": 28,
      "name": "액션"
    },
    {
      "id": 12,
      "name": "모험"
    },
    {
      "id": 16,
      "name": "애니메이션"
    },
    {
      "id": 35,
      "name": "코미디"
    },
    {
      "id": 80,
      "name": "범죄"
    },
    {
      "id": 99,
      "name": "다큐멘터리"
    },
    {
      "id": 18,
      "name": "드라마"
    },
    {
      "id": 10751,
      "name": "가족"
    },
    {
      "id": 14,
      "name": "판타지"
    },
    {
      "id": 36,
      "name": "역사"
    },
    {
      "id": 27,
      "name": "공포"
    },
    {
      "id": 10402,
      "name": "음악"
    },
    {
      "id": 9648,
      "name": "미스터리"
    },
    {
      "id": 10749,
      "name": "로맨스"
    },
    {
      "id": 878,
      "name": "SF"
    },
    {
      "id": 10770,
      "name": "TV 영화"
    },
    {
      "id": 53,
      "name": "스릴러"
    },
    {
      "id": 10752,
      "name": "전쟁"
    },
    {
      "id": 37,
      "name": "서부"
    }
]

result = []

for genre in data:
    genre_dict = {
        "model" : "movies.genre",
        "pk" : genre.get("id"),
        "fields" : {
            "name" : genre.get("name")
        }
    }
    result.append(genre_dict)

with open('genres.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(result, ensure_ascii=False))