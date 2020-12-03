<template>
  <div>
    <h2>검색어 : {{$route.query.keyword}}</h2>
    <h3>hi: {{ keyword }}</h3>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'SearchMovieList',
  data: function () {
    return {
      keyword: '',
      movies: [],
      result: []
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
    findMovie: function () {
      for(var i=0; i<this.movies.length; i++) {
        if (this.keyword in this.movies[i].title) {
          this.result.push(this.movies[i])
        }
      }
      console.log(this.result)
    }
  },
  created: function () {
    this.keyword = this.$route.query.keyword
    console.log(this.keyword)
    this.getMovies()
    // async, await..................
    this.findMovie()
    // console.log(this.movies)
    // console.log(this.result)

  }
}
</script>

<style>

</style>