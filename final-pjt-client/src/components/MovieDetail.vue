<template>
  <b-container class="bv-example-row">
    <b-row>
      <b-col cols="2"></b-col>
      <b-col cols="8">
        <b-card no-body class="overflow-hidden text-dark" style="max-width: 800px;">
          <b-row no-gutters>
            <b-col md="6">
              <b-card-img :src="getImgUrl($route.query.movie.poster_path)" alt="Image" class="rounded-0"></b-card-img>
            </b-col>
            <b-col md="6">
              <b-card-body title="">
                <b-card-text>
                  <h2>{{  $route.query.movie.title }}</h2>
                  <br>
                  <div>출시일 : {{  $route.query.movie.release_date }}</div>
                  <br>
                  <h4>평점 : {{  $route.query.movie.vote_average }}</h4>
                  <Rating :movie="movie" />
                </b-card-text>
              </b-card-body>
            </b-col>
          </b-row>
        </b-card>
        <div>
          {{ $route.query.movie.overview }}
        </div>
      </b-col>
      <b-col cols="2"></b-col>
    </b-row>
  </b-container>
</template>

<script>
import Rating from '@/components/Rating'

export default {
  name: 'MovieDetail',
  components: {
    Rating
  },
  data: function () {
    return {
    }
  },
  computed: {
    movie: function () {
      return this.$route.query.movie

    }
  },
  methods: {
    getImgUrl: function (url) {
      const imgUrl = `https://image.tmdb.org/t/p/w185${url}`
      return imgUrl
    },
  },
  created: function () {
  }
}
</script>

<style>

</style>