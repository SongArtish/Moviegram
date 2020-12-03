<template>
  <div>
    <h2>MovieRecommend</h2>
    <b-button @click="refresh">Refresh</b-button>
    <div class="m-5">
      <b-card-group>
        <b-card v-for="num in numbers" :key="num" class="text-dark font-weight-bold" :title="movies[num].title" :img-src="getImgUrl(movies[num].poster_path)" img-alt="Image" img-top  @click="toDetail(movies[num])">
          <b-card-text class="text-dark">
           <!-- {{ movies[num].overview }} -->
          </b-card-text>
          <template #footer>
            <small class="text-muted">{{ movies[num].genre_ids.name }}</small>
          </template>
        </b-card>
      </b-card-group>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieRecommend',
  data: function () {
    return {
      movies: [],
      numbers: [],
    }
  },
  methods: {
    getMovies: function () {
      axios.get(`${SERVER_URL}/movies/`)
        .then(res => {
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
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
      console.log('hello')
      console.log(result)
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
    this.getNumbers()
    this.getMovies()
  }
}
</script>

<style>

</style>