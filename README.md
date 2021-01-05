# 2020 Movie Website Project

> SSAFY 1학기 최종 프로젝트로 영화 추천 사이트를 구현하는 과정을 README로 작성한다.

---

[TOC]

---

## Project Period
2020.11.19 - 2020.11.27

## Contributors
- 이송영 (팀장)
- 이민정

## :exclamation: 시작 전 CHECK_LIST

### :ballot_box_with_check: pip 설치

> 프로젝트에 필요한 pip를 설치한다. 

- `final-pjt-server/requirements.txt` 파일을 참조한다.

### :ballot_box_with_check: npm 설치

- npm 사용을 위해서 `node.js`와 `Vue Cli`가 설치되어 있는지 확인한다.
- `final-pjt-client` 폴더 안에서 아래의 명령어를 실행해본다.

```bash
$ node -v
```

```bash
$ vue --version
```

- 이후 아래의 npm을 설치한다.

```bash
$ npm install
```

- 기본 Vue 프로젝트 생성 이후, 추가적으로 설치한 npm은 아래와 같다.

```bash
$ npm install axios
$ npm install lodash
$ npm install vue bootstrap-vue bootstrap
```

- vue bootstrap 설치 후, 해당 패키지를 등록한다. 자세한 내용은 [공식홈페이지](https://bootstrap-vue.org/docs)를 참조한다.

```markdown
 # vue bootstrap 사용예시

<template>
  <div id="app">
    <b-button>Button</b-button>
    <b-button variant="danger">Button</b-button>
    <b-button variant="success">Button</b-button>
    <b-button variant="outline-primary">Button</b-button>
  </div>
</template>
```

### :ballot_box_with_check: API 키 관리

- 프로젝트의 영화 데이터를 수집하는 API의 url과 key는 `final-pjt-server/movies/get_movie_data/api_key.py`에서 관리한다.
- gitignore로 관리되기 때문에 데이터 수집을 위해서는 해당 폴더에서 새로운 `api_key.py`를 작성하여 사용할 수 있도록 한다.
- `api_key.py`의 코드는 다음과 같다.

```python
# api_key.py

class URLMaker:
    url = 'https://api.themoviedb.org/3/movie/popular'
    key = '<API 키 값>'

    def __init__(self, key):
        self.key = key
        self.url = url
```

### :ballot_box_with_check: .env.local

> Vue 클라이언트 프로젝트의 최상위 폴더에는 `.env.local` 파일이 작성되어 있으며, 이것은 gitignore로 관리되어 있기 때문에 반드시 해당 파일을 생성하고 프로젝트를 진행하도록 한다.

- `.env.local` 파일에는 다음과 같은 데이터가 저장되어 있다.
  - `서버 url`

```
VUE_APP_SERVER_URL=http://127.0.0.1:8000
```



## 1 .팀원 정보 및 업무 분담 내역

### 팀장 : 이송영

- **Vue 클라이언트 구현**
- front-end

### 팀원 : 이민정

- **DRS 서버 로직 구현**
- back-end



## 2. 목표 서비스 구현 및 실제 구현 정도

### 2.1 목표 서비스

> 우리 팀이 처음에 기획한 서비스는 다음과 같다.

```markdown
## 1. 영화 조회 서비스
- 전체 영화 조회
- 장르별 영화 조회
- 영화 상세 조회
- Youtube trailor 영상 제공
- 배우별 영화 조회
## 2. 영화 추천 서비스
- 오늘의 추천 : 날씨 API, 사용자 관심장르 등의 데이터를 가져와서 추천
- 장르별 추천
## 3. community 기능
- 영화 리뷰 및 평점
```



### 2.2 실제 구현 서비스

- 컴포넌트 구조 

![image-20201126161941179](img/components.png)

```markdown
## 1. 영화 조회 서비스
- 전체 영화 조회
- 영화 상세 조회
- 영화 평점 서비스
## 2. 영화 추천 서비스
- 랜덤 추천
## 3. community 기능
- 영화 리뷰 작성
- 댓글 작성
```



## 3. 데이터베이스 모델링(ERD)

![image-20201126144015570](img/components.png)

### 1. Articles app의 Models.py 

- Article Model - User와 Article (1:N 관계)  
- Comment Model  - User와 Comment (1:N관계)
- Comment Model - article 와 comment (1:N관계)

```python
from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100)
    # rate = models.IntegerField()
    genre = models.TextField()
    rate = models.CharField(max_length=2)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=100)
```



### 2. Movies app의 Models.py 

- Rating Model - User와 rating (1:N 관계)  

- Rating Model- User와 movie (1:N 관계)  
- rates는 양수만 가능 (PositiveIntegerField)

```python
class Genre(models.Model):
    name = models.TextField()

class Movie(models.Model):
    title = models.CharField(max_length=50)
    popularity = models.FloatField()
    genre_ids = models.ManyToManyField(Genre, related_name='movie_genre')
    release_date = models.DateField()
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.TextField()

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rates = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])
```



## 4. 필수 기능에 대한 설명

### 4.1  영화목록 조회 

- MovieList.vue 

```javascript
 methods: {
    getMovies: function () {
      axios.get(`${SERVER_URL}/movies/`)
        .then(res => {
          this.movies = res.data
          this.movies.reverse()
        })
        .catch(err => {
          console.log(err)
        })
    },
    getImgUrl: function (url) {
      const imgUrl = `https://image.tmdb.org/t/p/w185${url}`
      return imgUrl
    },
```

- 영화클릭 시 MovieDetail  보여주기 

```vue
<div class="px-4 py-5" @click="toDetail(movie)">
```

```javascript
toDetail: function (movie) {
      this.$router.push({name: 'MovieDetail', query: {movie: movie}})
      // this.$router.push({name: 'MovieDetail', params: {movie: `${movie}`}})
    }
```



### 4.2 추천 서비스

- MovieRecommend.vue에서 Random으로 추천 
  - random으로 4개 뽑아서 정렬 

```javascript
getNumbers: function () {
      const population = _.range(100)
      this.numbers = _.sampleSize(population, 4)
    },
getImgUrl: function (url) {
    const imgUrl = `https://image.tmdb.org/t/p/w185${url}`
    return imgUrl
},
refresh: function () {
    this.getNumbers()
},
```



### 4.3  커뮤니티 기능 

- Articles.vue 에서 article 쓰기, 수정, 삭제 기능 구현 

  - 쓰기 (getArticles)

  ```javascript
    getArticles: function () {
        const config = this.getToken()
        axios.get(`${SERVER_URL}/articles/`, config)
          .then((res) => {
            // console.log(res.data)
            this.articles = res.data
            this.articles.reverse()
          })
          .catch((error) => {
            console.log(error)
          })
      },
  ```

  - 삭제(delete)

  ```javascript
      deleteArticle: function (article) {
        const config = this.getToken()
        // console.log(article)
        axios.delete(`${SERVER_URL}/articles/${article.id}/`, config)
          .then(res => {
            const idx = this.articles.findIndex(article => {
              return article.id === res.data.id
            })
            this.articles.splice(idx, 1)
          })
          .catch(err => {
            console.log(err)
          })
      },
  ```

  - 수정(update)

  ```javascript
      updateArticle: function (article) {
        const config = this.getToken()
        const articleItem = {
          title: article.title,
          rate: article.rate,
          content: article.content
        }
        axios.put(`${SERVER_URL}/articles/${article.id}/`, articleItem, config)
          .then((res) => {
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
      },
  ```

- CreateArticle.vue 

  ```javascript
      createArticle: function () {
        const config = this.getToken()
        axios.post(`${SERVER_URL}/articles/`, this.article, config)
          .then(() => {
            this.$router.push({ name:'Articles' })
          })
          .catch((err) => {
            console.log(err)
          })
          }
  ```



## 5. 배포 서버 URL

> [AWS S3](https://velog.io/@lllen/AWS-S3와-Cloudfront를-사용한-프론트엔드-배포)로 배포할 예정



## 6. 배운점

### 6.1 API를 DB로 저장하기

- API를 DB로 저장하기 위해서는 먼저 모델을 작성한다.

```python
# movies/models.py

from django.db import models

class Genre(models.Model):
    name = models.TextField()

class Movie(models.Model):

    title = models.CharField(max_length=50)
    popularity = models.FloatField()
    genre_ids = models.ManyToManyField(Genre, related_name='movie_genre')
    release_date = models.DateField()
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.TextField()
```

- DB로 저장하기 위해서는 아래의 `DB JSON 예제`와 같은 형식으로 데이터를 저장해야 한다.

```json
// DB JSON 예제
[
  {
    "model": "<APP명>.<MODEL명>",
    "pk": <pk값>,
    "fields": {
      "<필드명1>": "<필드명1 값>",
      "<필드명2>": "<필드명2 값>"
    }
  },
  {
    "model": "myapp.person",
    "pk": 2,
    "fields": {
      "first_name": "Paul",
      "last_name": "McCartney"
    }
  }
]
```

- 데이터를 가져오기 위한 패키지 모듈은 다음과 같다.
  - `api_key`의 `URLMaker`라는 함수에서 api 주소와 api 키 값을 관리한다.

```python
# dumpdata.py > 0. import

# 영화정보를 API를 이용해서 가져오기
# 홈페이지  https://www.themoviedb.org/
# Document  https://developers.themoviedb.org/3

import json
# pip install requests
import requests
from api_key import URLMaker
```

- 영화 정보는 페이지별로 가져와서 for문을 돌려 위의 `DB JSON 예제`의 형식대로 새로운 `movies.json` 파일에 저장해준다.

```python
# dumpdata.py > 1. movie 정보
result = []
url = URLMaker.url
key = URLMaker.key
for page in range(1, 21):
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
```

- 장르정보는 데이터를 사이트에서 직접 가져와서 `DB JSON 예제`의 형태로 저장해준다.

```python
# dumpdata.py > 1. genre 정보

data = [
    {
      "id": 28,
      "name": "액션"
    },
    ...
    <장르정보>
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
```

- 이렇게 `movies.json`, `genres.json`에 저장된 데이터를 아래의 `loaddata` 명령을 통해 DB를 가져온다.
  - :heavy_check_mark: `Movie` 모델이 `Genre` 모델을 참조하고 있으므로, `loaddata` 명령은 반드시 `Genre -> Movie` 순서대로 시행한다!!

```bash
$ python manage.py loaddata movies/get_movie_data/movies.json
```

### 6.2 CreateArticle 작성하기

**CreativeArticle.vue** 

> [사이트](https://bootstrap-vue.org/docs/components/form/#form) 참고
>
> 필드 : title, content, genre 

- Vue bootstrap에서 `form`을 가져와서 Article을 작성하는 양식을 만들었다.

```vue
<template>
  <div class="mx-5 px-5">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Title:"
        label-for="input-1"
        description="솔직한 리뷰는 환영입니다!!!"
      >
        <b-form-input
          id="input-1"
          v-model="article.title"
          type="text"
          required
          placeholder="Please write title"
          autofocus
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="content:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="article.rate"
          required
          placeholder="Please write review"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Genre" label-for="input-3">
        <b-form-select
          id="input-3"
          v-model="article.content"
          :options="genres"
          required
        ></b-form-select>
      </b-form-group>


      <b-button variant="primary" @click="createArticle">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>

  </div>

</template>
```

- Article 모델의 필드값을 딕셔너리 형태로 입력하였다.
- 추가적으로 게시물을 작성할 때 영화의 장르를 입력할 수 있는 `dropdown`을 만들어주었다.

```vue

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data() {
    return {
      article: {
        title: '',
        rate: '',
        content: '',
    
      },
      genres: [{ text: 'Select One', value: null }, 'Horror', 'Romance', 'Comedy', 'Adventure', 'Fantasy', 'Animation','Drama','Action','History','Western','Thriller','Crime','Documentary','SF','Mystery','Music','Family','War','TVmovie'],
      show: true
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault()
      alert(JSON.stringify(this.article))
    },
    onReset(evt) {
      evt.preventDefault()
      // Reset our form values
      this.article.title = ''
      this.article.rate = ''
      this.article.content = null
      
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    
  getToken: function () {
    const token = localStorage.getItem('jwt')
    const config = {
      headers: {
        Authorization: `JWT ${token}`
      }
    }
    return config
  },

createArticle: function () {
const config = this.getToken()
axios.post(`${SERVER_URL}/articles/`, this.article, config)
  .then(() => {
    this.$router.push({ name:'Articles' })
  })
  .catch((err) => {
    console.log(err)
  })
  }
  }
}
</script>

<style>

</style>
```

- 중간에 `401 Eroor`  가 발생하였다.
  - 서버를 껐다켜니 해결되었다.



### 6.3  Vue Router로 데이터 전달하기

> `MovieDetail`과 `ArticleDetail` 페이지를 만들 때 다음의 로직을 사용하였다. 자세한 내용은 [인터넷 블로그](https://velog.io/@skyepodium/vue-router%EB%A1%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%84%EB%8B%AC%ED%95%98%EA%B8%B0-eskrsmr3)를 참고하였다.
>
> Vue Router로 데이터를 전달하는 방법은 아래 2가지가 있다.
>
> - query
>
>   ```
>   {name: 'Query', query: {name: 'cat', age: 3}}
>   ```
>
> - params
>
>   ```
>   {name: 'Params', params: {name: 'dog', age:4}}
>   ```

- 먼저 특정 article/movie를 클릭하면 detail로 `router.push`해주는 함수를 작성한다.

```javascript
methods: {
            clickList () {
                this.$router.push({name: 'Query', query: {name: 'cat', age: 3}})
            },
            clickParams () {
                this.$router.push({name: 'Params', params: {name: 'dog', age:4}})
            }
        }
```

- :exclamation: **params를 사용할 경우**
  - `index.js`(라우터)에서 prop를 추가해주어야한다.

```javascript
// index.js

{
    path: '/params',
    component: Params,
    name: 'Params',
    // true로 설정하면 데이터를 props로도 받습니다.
    props: true
}     
```

- **query의 경우** 다음과 같이 push한 템플릿에서 데이터를 받을 수 있다.

```vue
<!-- Query.vue -->
<h1>Query</h1>
<h2>name: {{ $route.query.name }}</h2>
<h2>age: {{ $route.query.age }}</h2>
```

- **params의 경우** props로 데이터를 받을 후, 템플릿에서 데이터를 표시할 수 있다.

```javascript
// Params.vue

props: {
    name: {
        type: String,
            default : ''
    },
        age: {
            type: Number,
                default: 0
        }
}
```

- 템플릿에서는 props로 받은 데이터를 표시한다.

```vue
<!-- Params.vue -->
<h1>Params</h1>

<h2>params로 받은 데이터</h2>
<h2>name: {{ $route.params.name }}</h2>
<h2>age: {{ $route.params.age }}</h2>

<h2>props로 받은 데이터</h2>
<h2>name: {{ name }}</h2>
<h2>age: {{ age }}</h2>
```

- 끝!!!



## 7. 오류 디버깅

### 7.1 Vue 환경변수 호출 문제

> Vue에서 `.env.local` 파일을 생성해 환경변수를 관리하려고 했는데, 해당 변수를 호출하면 `undefined`로 반환하는 문제가 있었다.

**문제상황**

- 처음에 환경 변수 명을 `VUE_APP_BASIC_URL`로 정의했다가 후에 `VUE_APP_SERVER_URL`로 이름을 변경하였다.
- `process.env`를 출력해보니 해당 데이터 내에는 여전히 `VUE_APP_BASIC_URL`이라는 변수명으로 데이터가 저장되어 있었다.

**해결방안**

- 이를 발견하고 데이터가 최신화가 되지 않았다는 사실을 발견했다.

- 그래서 우선 npm을 다시 설치해보았다.

  ```bash
  $ npm install
  ```

- 그리고 `process.env`를 다시 출력해보니 변수명이 `VUE_APP_SERVER_URL`로 변경되어 있었다.

### 7.2 동기화 문제

> Vue의 Life Cycle의 `created`에서 아래와 같이 순서대로 함수를 실행해줄 때,
>
> ```javascript
> created: function () {
>     this.functionA()
>     this.functionB()
>     this.functionC()
> }
> ```
>
> functionB가 functionA가 실행되어야만 데이터를 받아 실행을 할 수 있지만, functionA가 실행 완료되기 전에 functionB가 실행이 되어 오류가 나는 현상이 있었다.

- `async`와 `await`를 통해서 해결하려고 했으나, 잘 되지 않았다.



## 8. 기타(느낀점)

```
  영화 추천 사이트를 만들면서  vue.js와 django의 사용법을 더욱 잘 알게 되었다.  이론만 배웠지 어떻게 활용할지 잘 몰랐는데 직접 명세서를 보면서 하나씩 구현해보니 익숙해졌다. 

  데이터 모델링 부분 부터 어려움이 많았지만 데이터간 관계를 생각해보며 하나씩 해 보니 해결되었고 이 과정은 프로그램 전체 구조에 대해 생각해볼 수 있는 좋은 경험이었다. 

  특히 Vue.js 를 쓸 때 어려움을 많이 느꼈는데 부모 요소의 정보를 자식에게 전달하거나 렌더링 시 이를 고려하는게 복잡해서 생각보다 많은 시간을 쓰게 되었는데 나중에 이부분을 더욱 보완해서 빠르게 작업할 수 있도록 노력해야겠다. 

  또한 vue bootstrap을 쓸 때 어떻게 적용해야할지 어려움이 있었는데 사이트를 참고하면서 하나씩 따라하니까  해결할 수 있었다. 

웹의 처음부터 끝까지 제작하면서 쉬운 것이 하나도 없다는 것을 느꼈고 계획 단계부터 배포까지 해보면서 전체 과정을 알 수 있어 뿌듯하고 보람찬 경험이었다. 
```

***Copyright* © 2020 Song_Artish**
