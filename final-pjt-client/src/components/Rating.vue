<template>
  <div>
    <div>
      <!-- <div v-if="hiUserinRatings">
        <b-form-rating @click="ratingUpdate" v-model="rate.rates" variant="warning" class="mb-2" inline value="4" stars="10" show-value></b-form-rating>
      </div> -->
      <div @click="ratingCreate">
        <b-form-rating v-model="rate.rates" variant="warning" class="mb-2" inline value="4" stars="10" show-value></b-form-rating>
      </div>
      <br>
      <hr>
      <br>
      <!-- 평점 목록 -->
      <div v-if="!hiRatings.length">
        <span>No ratings yet</span>
      </div>
      <div v-else v-for="(rating, idx) in hiRatings" :key="idx">
        <span v-if="hiUser.pk===rating.user">나의 평점: {{ rating.rates }}    <b-button @click="ratingDelete(rating)" variant="outline-danger" pill>DELETE</b-button></span>
        <span v-else>{{rating.user}}의 평점: {{ rating.rates }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Rating',
  props: {
    movie: String
  },
  computed: {
    hiRatings: function () {
      return this.ratings
    },
    hiUser: function () {
      return this.user
    },
    // hiUserinRatings: function () {
    //   this.isUserInRatings()
    //   return this.isUserInRating
    // }
  },
  data: function () {
    return {
      rate: {
        rates: ''
      },
      ratings: [],
      user: '',
      // isUserInRating: false
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getRatings: function () {
      const config = this.getToken()
      const id = this.$route.query.movie.id
      axios.get(`${SERVER_URL}/movies/detail/${id}/rating_list_create/`, config)
        .then((res) => {
          this.ratings = res.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    ratingCreate: function () {
      const config = this.getToken()
      const id = this.$route.query.movie.id
      axios.post(`${SERVER_URL}/movies/detail/${id}/rating_list_create/`, this.rate, config)
        .then(() => {
          this.getRatings()
          // console.log(res)
          // this.$router.push({ name:'Articles' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    ratingDelete: function (rating) {
      const config = this.getToken()
      axios.delete(`${SERVER_URL}/movies/detail/${rating.id}/rating_delete/`, config)
        .then(res => {
          this.getRatings()
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getUser: function () {
    const config = this.getToken()
    axios.get(`${SERVER_URL}/profile/`, config)
      .then((res) => {
        this.user = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    },
    // isUserInRatings: function () {
    //   for (var i=0; i<this.ratings.length; i++) {
    //     if (this.user === this.ratings[i].user) {
    //       this.isUserInRating = true
    //       return
    //     }
    //   }
    // },
    // ratingUpdate: function () {
    //   const config = this.getToken()
    //   const id = this.$route.query.movie.id
    //   axios.put(`${SERVER_URL}/movies/detail/${id}/rating_update/`, this.rate, config)
    //     .then(() => {
    //       this.getRatings()
    //       // console.log(res)
    //       // this.$router.push({ name:'Articles' })
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // }
  },
  created: function () {
    this.getRatings()
    this.getUser()
  }
}
</script>

<style>

</style>