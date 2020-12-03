<template>
  <div>
    <h2>MovieList</h2>
    <br>
    <p>Swipe to see more</p>
    <!-- 로그인 했으면 조건 걸어주기 -->
    <div class="m-5">
      <vue-glide v-if="movies.length">
        <vue-glide-slide v-for="(movie, idx) in movies" :key="idx">
          <div class="px-4 py-5" @click="toDetail(movie)">
            <b-card class="text-dark font-weight-bold" :title="movie.title" :img-src="getImgUrl(movie.poster_path)" img-alt="Image" img-top>
              <b-card-text id="overview" class="text-dark">
                <!-- {{ movie.overview }} -->
              </b-card-text>
              <template #footer>
                <small class="text-muted">{{ movie.genre_ids.name }}</small>
              </template>
            </b-card>
          </div>
          <!-- <img :src="getImgUrl(movie.poster_path)" alt="" class="mb-5">
          <h2>{{ movie.title }}</h2> -->
        </vue-glide-slide>
      </vue-glide>
    </div>
  </div>

<!-- <b-card class="text-dark font-weight-bold" :title="movies[numbers[0]].title" :img-src="getImgUrl(movies[numbers[0]].poster_path)" img-alt="Image" img-top>
  <b-card-text class="text-dark">
    {{ movies[0].overview }}
  </b-card-text>
  <template #footer>
    <small class="text-muted">{{ movies[0].genre_ids.name }}</small>
  </template>
</b-card> -->

</template>

<script>
import axios from 'axios'
// import _ from 'lodash'
import { Glide, GlideSlide } from 'vue-glide-js'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components: {
      [Glide.name]: Glide,
      [GlideSlide.name]: GlideSlide
    },
  data: function () {
    return {
      movies: [],
      perPage: 3,
      currentPage: 1,
      genres: [
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
    }
  },
  computed: {
    rows() {
      return this.movies.length
    },
    hiMovie: function () {
      return this.movies
    }
  },
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
    // 리뷰 글자수 100자로 제한하는 함수 or filter 만들고 싶은데...
    filterOverview: function (num) {
      return num
    },
    // 장르id를 문자열로 표시하는 함수 만들고싶다!!!!!!!!!!
    getGenre: function (genre_ids) {
      var result = ''
      var dummy = ''
      for (var i=0; i < genre_ids.length; i++) {
        if (genre_ids[i] in this.genres) {
          const result = `${result} ${dummy}`
        }
      }
      if (result) {
        return result
      } else {
        const noGenreMessage = 'No Genre Defined'
        return noGenreMessage
      }
    },
    toDetail: function (movie) {
      this.$router.push({name: 'MovieDetail', query: {movie: movie}})
      // this.$router.push({name: 'MovieDetail', params: {movie: `${movie}`}})
    }
  },
  created: function () {
    this.getMovies()
  }
}
</script>

<style>
/* #overview {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
} */
</style>